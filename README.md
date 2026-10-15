# nlp-06-nlp-pipeline

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/denisecase/nlp-06-nlp-pipeline/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/denisecase/nlp-06-nlp-pipeline/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://denisecase.github.io/nlp-06-nlp-pipeline/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Build a reproducible NLP pipeline for acquiring, processing, and analyzing web text.

## Project Overview

Author: Denise Case

Date: 2026 October

Sixth project in the Web Mining and Applied NLP course.

This project introduces a complete natural language
processing pipeline for working with web documents.

The goal is to retrieve HTML,
validate document structure,
extract and clean text,
engineer NLP features,
visualize patterns,
and persist the results.

The project extends the EVTL approach
from earlier modules by adding an explicit
Analyze stage.

Specifically, it reuses frequency and charts from 01,
cleaning from 02,
the stage pattern from 04, and
extraction from 05.
Co-occurrence and bigrams were covered in 03,
but are not required for this project.

The resulting architecture is
Extract, Validate, Transform, Analyze, Load (EVTAL).

The project is configured in
[pyproject.toml](pyproject.toml).

## Data

The example retrieves an academic paper's abstract page
from [arXiv](https://arxiv.org/abs/2602.20021).

The source document contains:

- Paper title.
- Authors.
- Abstract text.
- Subject categories.
- Submission information.
- arXiv identifier.

The pipeline preserves the original HTML,
extracts document metadata,
and produces a structured dataset
with derived NLP features.

## Approach

The project uses a modular Python pipeline
to acquire, validate, transform, analyze,
and save web document data.

The pipeline has five stages:

- **Extract** - retrieve HTML from a web page.
- **Validate** - verify required HTML elements.
- **Transform** - extract metadata, clean text, and calculate NLP features.
- **Analyze** - examine token frequencies and create visualizations.
- **Load** - save the processed dataset to a CSV file.

The example uses Requests for HTTP acquisition,
BeautifulSoup for HTML parsing,
spaCy for linguistic text processing,
Pandas for tabular data,
and Matplotlib and WordCloud for visualization.

The Transform stage demonstrates:

- Tokenization and text normalization.
- Punctuation and stopword removal.
- Abstract word counts.
- Cleaned token counts.
- Unique token counts.
- Type-token ratios.
- Author counts.

Explore these important project components:

- [pyproject.toml](pyproject.toml) - project identity, dependencies, and tool configuration.
- [src/nlp/pipeline_web_html.py](src/nlp/pipeline_web_html.py) - main EVTAL pipeline orchestrator.
- [src/nlp/config.py](src/nlp/config.py) - example web page and path configuration.
- [src/nlp/stage01_extract.py](src/nlp/stage01_extract.py) - retrieve HTML.
- [src/nlp/stage02_validate.py](src/nlp/stage02_validate.py) - validate HTML structure.
- [src/nlp/stage03_transform.py](src/nlp/stage03_transform.py) - clean text and engineer NLP features.
- [src/nlp/stage04_analyze.py](src/nlp/stage04_analyze.py) - analyze token frequencies and generate visualizations.
- [src/nlp/stage05_load.py](src/nlp/stage05_load.py) - save processed results.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated testing and documentation deployment.
- [docs/](docs/) - project documentation.
- [zensical.toml](zensical.toml) - documentation configuration.

The goal is to understand how an NLP pipeline
transforms raw web content into structured,
analysis-ready data with interpretable features.

## spaCy Pipeline

The project uses [spaCy](https://spacy.io/)
for tokenization and for flagging
stopwords and punctuation.

The example uses the `en_core_web_sm`
small English trained pipeline.

The package is declared in
[pyproject.toml](pyproject.toml)
and installs with the project dependencies.

The example uses spaCy to split text into tokens
and remove stopwords and punctuation.
The same pipeline also provides part-of-speech tagging,
dependency parsing, and named entity recognition.
This example does not use those components.

Text preprocessing remains useful in modern NLP,
particularly when creating inspectable,
repeatable analysis pipelines.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
to set up your machine and project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m nlp.pipeline_web_html
```

## Results

The pipeline retrieves an HTML document,
validates its structure,
extracts bibliographic information,
and cleans the abstract text.

It calculates NLP features,
produces frequency visualizations,
and writes the results to a CSV file.

Successful execution produces:

```shell
========================
Pipeline executed successfully!
========================
```

The following files are created:

- `project.log` - pipeline execution log.
- `data/raw/case_raw.html` - original HTML document.
- `data/processed/case_processed.csv` - processed NLP dataset.
- `data/processed/case_top_tokens.png` - token frequency bar chart.
- `data/processed/case_wordcloud.png` - word cloud visualization.

These artifacts provide evidence of successful
data acquisition, validation, transformation,
analysis, and persistence.

### Example Visualizations

![Top Tokens](docs/images/case_top_tokens.png)

![Word Cloud](docs/images/case_wordcloud.png)

## Verification

Run the automated tests:

```shell
uv run python -m pytest
```

## Project Documentation

The [hosted documentation site](https://denisecase.github.io/nlp-06-nlp-pipeline/)
is published using Zensical and GitHub Pages.

The documentation site is used to present the project report,
covering such sections as data, methods, results, visualizations,
interpretation, and conclusions.

For additional context about traditional NLP
and modern language-model approaches,
see [NLP Evolution](docs/nlp-evolution.md).

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD)
to check project files and publish the docs.

GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/denisecase/nlp-06-nlp-pipeline/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/denisecase/nlp-06-nlp-pipeline/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
for **detailed instructions and troubleshooting**.

### Initialize and Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uv run prek install --force
uv run prek update --freeze --cooldown-days 7

git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Developer Tools

This project uses professional Python tools to support development,
testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://denisecase.github.io/nlp-06-nlp-pipeline/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
