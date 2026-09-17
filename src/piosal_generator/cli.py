from __future__ import annotations

import argparse
from .generator import GenerationConfig, generate_project


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate synthetic embedded OSAL source files")
    parser.add_argument("module_name")
    parser.add_argument("--templates", default="examples/templates")
    parser.add_argument("--output", default="generated")
    parser.add_argument("--feature", action="append", default=[])
    args = parser.parse_args()
    config = GenerationConfig(args.module_name, frozenset(args.feature))
    output = generate_project(args.templates, args.output, config)
    print(f"Generated sources in: {output.resolve()}")


if __name__ == "__main__":
    main()
