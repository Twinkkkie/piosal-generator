from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


FEATURE_BLOCK = re.compile(
    r"// <FEATURE:(?P<name>[A-Z0-9_]+)>\n(?P<body>.*?)// </FEATURE:(?P=name)>",
    re.DOTALL,
)


@dataclass(frozen=True, slots=True)
class GenerationConfig:
    module_name: str
    enabled_features: frozenset[str]

    @property
    def upper(self) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "_", self.module_name).upper()

    @property
    def lower(self) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "_", self.module_name).lower()


def render_template(text: str, config: GenerationConfig) -> str:
    def feature_replacer(match: re.Match[str]) -> str:
        return match.group("body") if match.group("name") in config.enabled_features else ""

    rendered = FEATURE_BLOCK.sub(feature_replacer, text)
    rendered = rendered.replace("TEMPLATE_UPPER", config.upper)
    rendered = rendered.replace("template_lower", config.lower)
    rendered = re.sub(r"\n{3,}", "\n\n", rendered)
    return rendered.strip() + "\n"


def generate_project(template_dir: str | Path, output_dir: str | Path, config: GenerationConfig) -> Path:
    template_root = Path(template_dir)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    generated_files: list[str] = []
    for source in sorted(template_root.glob("*.tmpl")):
        target_name = source.stem.replace("template", config.lower)
        target = output / target_name
        target.write_text(render_template(source.read_text(encoding="utf-8"), config), encoding="utf-8")
        generated_files.append(target_name)
    cmake = [
        "cmake_minimum_required(VERSION 3.20)",
        f"project({config.lower}_osal C)",
        "",
        "add_library(${PROJECT_NAME}",
        *[f"    {name}" for name in generated_files if name.endswith('.c')],
        ")",
        "",
    ]
    (output / "CMakeLists.txt").write_text("\n".join(cmake), encoding="utf-8")
    return output
