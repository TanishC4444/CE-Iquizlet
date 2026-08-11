# CE-I Quizlet Generator

A small Python utility that converts study material into structured, browser-ready Quizlet-style study data.

## Overview

The generator reads source material from `input.txt`, transforms it into structured study data, and produces JSON/JavaScript output that can be viewed through the included `index.html` page.

## Features

- Text-to-study-data conversion
- Structured JSON output
- Browser-ready JavaScript output
- Included HTML viewer
- Simple local workflow

## Prerequisites

- Python 3
- pip

## Installation

```bash
git clone https://github.com/TanishC4444/CE-Iquizlet.git
cd CE-Iquizlet
```

## Quick Start

1. Put the study material you want to convert in `input.txt`.
2. Run the generator:

```bash
python test.py
```

3. Open `index.html` in a browser to view the generated result.

## Project Structure

```text
CE-Iquizlet/
├── test.py
├── input.txt
├── quiz_output.json
├── quiz_output.js
└── index.html
```

## Responsible Use

Remove private or copyrighted study material before publishing generated outputs. Keep generated artifacts intentionally selected and review them for accuracy.

## Status

Educational utility.

## License

No separate license is currently specified in the repository.
