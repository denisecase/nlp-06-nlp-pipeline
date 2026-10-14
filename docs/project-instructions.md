# Project Instructions

## Goal

Apply **natural language processing**
to extract, clean, analyze, and interpret
text from a web document.

Combine web acquisition, text preprocessing,
feature engineering, and visualization
in an integrated NLP pipeline.

Use an Extract, Validate, Transform, Analyze, Load (EVTAL) pipeline.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Retrieves and validates an HTML document.
- Extracts document text and metadata.
- Uses spaCy for linguistic text processing.
- Applies cleaning and stopword removal.
- Calculates token counts and vocabulary measures.
- Computes token frequency distributions.
- Creates a frequency bar chart and word cloud.
- Saves the processed data and visualizations.

Consider how preprocessing choices
affect the resulting token frequencies
and type-token ratio.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**nlp-06-nlp-pipeline-custom**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Investigate the vocabulary
and linguistic patterns of an academic paper
using an integrated NLP pipeline.

Use the academic paper selected
for your Module 05 custom project.

Build on your previous work with
HTML extraction and structured data.

Keep the original `.py` files as working examples.
Create and modify copies for your custom processing stages.

Update the pipeline imports as needed
so your custom implementation executes.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Change one feature of the NLP analysis.

For example, change the number of top tokens
displayed in the frequency bar chart.

Run the pipeline again
and verify that the visualization changes.

Explain how the modification
affects the presentation of the results.

### Progression 3. Apply to a New Problem

Adapt the EVTAL pipeline
to analyze your selected academic paper.

- Reuse the document extraction techniques from Module 05.
- Verify the HTML structure and extracted information.
- Inspect the raw abstract text.
- Apply appropriate cleaning and tokenization.
- Calculate total and unique token counts.
- Calculate and interpret the type-token ratio.
- Identify the most frequently occurring tokens.
- Generate a token frequency chart and word cloud.
- Save the processed dataset and visualizations.
- Interpret what the results reveal about the document.

Investigate one preprocessing decision.

For example, compare results
with and without selected stopwords.

Explain:

- How the cleaning decision changed the results.
- Whether useful information may have been removed.
- What the most frequent tokens suggest about the topic.
- What the type-token ratio reveals about vocabulary diversity.
- What limitations affect your interpretation.

The goal is to integrate the skills from earlier modules
into a complete, interpretable NLP workflow.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Selected document and analytical question.
- Data acquisition and validation.
- Text preprocessing and cleaning decisions.
- NLP features and calculations.
- Token frequencies and vocabulary measures.
- Frequency chart and word cloud.
- Interpretation, tradeoffs, and limitations.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**.
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**.
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/nlp` folder reflects your authorship and custom work.
- [ ] The custom EVTAL pipeline processes your selected document.
- [ ] The processed dataset and visualization artifacts are available.
- [ ] The preprocessing choices and NLP results are interpreted.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
