# PiOSAL Generator

Python desktop utility for generating embedded C/C++ source files and build configuration from reusable templates.

> **Portfolio case study.** Proprietary embedded templates and internal company-specific source code are intentionally excluded.

## What the application does

The tool transforms reusable OS abstraction layer templates into module-specific source files based on user-selected configuration parameters.

### Core capabilities

- Conditional removal of inactive code blocks
- Module-prefix substitution across naming conventions
- Cleanup of template comments and redundant whitespace
- Generation of modified `.c` and `.h` files
- Automatic generation of CMake configuration
- Desktop UI for selecting generation options

## Technology stack

- Python
- PyQt5
- C / C++ templates
- CMake
- FreeRTOS-oriented embedded workflow
- Regular expressions / text transformation
- Git

## My contribution

- Developed the Python source-code generation utility
- Implemented template processing and code-block filtering
- Implemented naming/prefix transformations
- Generated C/C++ output files and CMake configuration automatically
- Built a PyQt desktop interface for the generator workflow

## Public demo implementation

The repository includes a **clean-room public demo** of the generation workflow using synthetic C templates. It demonstrates conditional source blocks, naming/prefix transformation, `.c/.h` generation, and automatic `CMakeLists.txt` output without publishing the original company templates.

```bash
python -m pip install -e .
piosal-demo "Pi Demo" --feature DIAGNOSTICS --output generated
python -m unittest discover -s tests -v
```
