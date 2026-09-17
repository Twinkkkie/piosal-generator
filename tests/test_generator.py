import tempfile
import unittest

from piosal_generator.generator import GenerationConfig, generate_project, render_template


class PiOSALGeneratorDemoTests(unittest.TestCase):
    def test_feature_filtering_and_prefixes(self):
        template = "TEMPLATE_UPPER\n// <FEATURE:X>\nint template_lower_x;\n// </FEATURE:X>\n"
        enabled = render_template(template, GenerationConfig("Pi Demo", frozenset({"X"})))
        disabled = render_template(template, GenerationConfig("Pi Demo", frozenset()))
        self.assertIn("PI_DEMO", enabled)
        self.assertIn("pi_demo_x", enabled)
        self.assertNotIn("pi_demo_x", disabled)

    def test_project_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = generate_project("examples/templates", tmp, GenerationConfig("Pi Demo", frozenset({"DIAGNOSTICS"})))
            self.assertTrue((out / "pi_demo_osal.c").exists())
            self.assertTrue((out / "CMakeLists.txt").exists())


if __name__ == "__main__":
    unittest.main()
