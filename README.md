# Utils

This repository contains utility scripts for generating LaTeX templates and working with academic subjects.

## Contents

- `subject.py`: Defines the `Subject` Enum and stores the fields and subjects in a nested dictionary.
- `sheet_template_creator.py`: Generates a LaTeX template for a specific subject and exercise sheet using the `Subject`
  Enum from `subject.py`.

Runnning python `sheet_template_creator.py will generate a `current_sheet_template.txt` file in the same directory with
the LaTeX template for the specified subject and exercise sheet.

