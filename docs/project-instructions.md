# Project Instructions (Module 6: NLP Pipeline)

## WEDNESDAY: Complete Workflow Phase 1

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run** - copy the project and confirm it runs

## FRIDAY/SUNDAY: Complete Workflow Phases 2-4

Again, follow the instructions above to complete:

1. Phase 2. **Change Authorship** - update the project to your name and GitHub account
2. Phase 3. **Read & Understand** - review the project structure and code
3. Phase 4. **Make a Technical Modification** - make a change and verify it still runs.

## Phase 4 Suggestions

Make a small technical change that does not break the pipeline.
Choose any one of these (or a different modification as you like):

- Change the target URL to a different arXiv paper
  (find a paper you find interesting at https://arxiv.org)
- Add a new derived column in the Transform stage
  (e.g., sentence count in the abstract, or average word length)
- Adjust the number of top tokens shown in the frequency bar chart
- Add a new visualization in the Analyze stage
  (e.g., a histogram of word lengths)
- Adjust logging messages to provide more detail about the pipeline stages

Confirm the script still runs successfully after your change.

## Phase 5 Suggestions

### Phase 5 Suggestion 1. New arXiv Paper (Directed)

Apply the same EVTAL pipeline to a different arXiv abstract page.

Steps:

- Find an arXiv paper that interests you at https://arxiv.org
- Copy the abstract page URL (e.g., `https://arxiv.org/abs/XXXX.XXXXX`)
- Update `PAGE_URL` in your copied `config` file with the new URL
- Run the pipeline
- Inspect the extracted fields, cleaned text, and visualizations
- Confirm the pipeline runs successfully

Then:

- Identify the title, authors, and primary subject of your chosen paper
- Describe how the cleaned abstract differs from the raw abstract
- Compare the type-token ratio and token count to the case example
- Describe what the word cloud and bar chart reveal about the paper's topic

### Phase 5 Suggestion 2. New Web Page (Original Selection)

Apply this pipeline to a different web page of your choice.

Good options include:

- Another arXiv listing page (e.g., `https://arxiv.org/list/cs.AI/recent`)
  to extract and analyze multiple abstracts at once
- A Wikipedia article to extract and analyze the introduction
- A Project Gutenberg page to extract text from a literary work
  (e.g., https://www.gutenberg.org/files/1342/1342-h/1342-h.htm Pride and Prejudice)

Steps:

- Open the target page in your browser
- Right-click and select "View Page Source" to inspect the HTML structure
- Identify the tags and class names that wrap the content you want
- Update your copied `config` file with the new URL
- Update your copied `stage02_validate` file to check for the new structure
- Update your copied `stage03_transform` file to extract and clean the new fields
- Run the pipeline and confirm success

Then:

- Describe the HTML structure of your chosen page
- Identify the tags and attributes you used to extract each field
- Explain one challenge you encountered in cleaning the text and how you resolved it
- Describe what the frequency analysis reveals about the content

## Key Skill Focus

As you work, focus on:

- how Transform is an iterative loop: inspect, clean, inspect, engineer, repeat
- how cleaning decisions involve tradeoffs (what signal might be lost?)
- how to compute and interpret token frequency, vocabulary richness, and type-token ratio
- how visualizations (bar charts, word clouds) surface patterns that numbers alone do not
- how data moves through the EVTAL pipeline

Your goal is to produce a clean, analysis-ready corpus and interpret what the analysis reveals.

## Optional Enhancements

If time allows, consider:

- extracting and analyzing multiple abstracts into a multi-row DataFrame
- comparing type-token ratios across two different papers
- experimenting with different stopword lists or cleaning strategies
- adding POS-filtered tokens (nouns only, verbs only) to the analysis

## Professional Communication

Remove instructor-provided content you no longer need in your project.

Make sure the title and narrative reflect your presentation.
Verify key files:

- README.md
- docs/ (source and hosted on GitHub Pages)
- src/ (pipeline and stage files)

Ensure your project clearly demonstrates:

- correct EVTAL pipeline execution
- understanding of text cleaning and its tradeoffs
- ability to compute and interpret NLP features
- meaningful visualizations with written interpretation
