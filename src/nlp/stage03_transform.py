"""stage03_transform.py.

(EDIT YOUR VERSION OF THIS FILE)

Source: validated BeautifulSoup object
Sink:   analysis-ready Pandas DataFrame

NOTE: We use Pandas for consistency with Module 5.
You may use Polars or another library if you prefer.
The pipeline pattern is identical; only the DataFrame API differs.

======================================================================
THE ANALYST WORKFLOW: Transform is not a single step
======================================================================

In a real NLP project, Transform is an iterative loop, not a
linear sequence of operations.

The loop looks like this:

  inspect → clean → inspect → engineer → inspect → clean → repeat

We need to inspect the data to know what cleaning is needed.
We inspect the cleaner data and begin to engineer additional features.
We inspect again to see how the cleaning worked and do more as needed.

This loop continues until the data is analysis-ready,
meaning a model or analyst could use the data without being misled
by noise, inconsistency, or missing signal.

This transform module is the SETTLED VERSION of that loop.
It captures decisions that survived inspection.
It does not show the full iterative process.
You should run it, inspect the logged output at each substage,
and ask yourself:

  - Does this look cleaner than the previous step?
  - Is there still noise I should remove?
  - Am I losing signal I want to keep?
  - What derived features would help a model or analyst?

The answers often suggest more work and that increases value.
That's the analyst workflow in action.

======================================================================
MODERN LLM Tools
======================================================================

Modern LLM tools are powerful, but only as good as the data provided.

`Garbage in, garbage out` is not a cliche.
It's why good data analysts are still very much needed.

A valuable analyst is one who understands:
  - why text needs cleaning before analysis
  - what signal looks like vs what noise looks like
  - how to inspect, iterate, and improve data quality
  - how to document those decisions so they are reproducible

The goal in this stage is not just to produce a clean DataFrame.
The goal is to develop the judgment to know when a DataFrame
is ready for use, and to professionally document why choices were made.

Judgment is what makes an analyst irreplaceable.

======================================================================
THIS STAGE
======================================================================

This stage runs three substages, each logged separately:

  03a. Extract fields from the validated HTML into a raw DataFrame.
       Inspect: does the raw data look right?

  03b. Clean and normalize the text fields.
       Inspect: is the text cleaner? Did we lose anything we needed?

  03c. Engineer derived features (tokens, word count, frequency).
       Inspect: do the derived fields add signal for downstream analysis?

The final DataFrame is the settled result of these three passes.

======================================================================
PURPOSE AND ANALYTICAL QUESTIONS
======================================================================

Purpose

  Transform validated HTML into a clean, analysis-ready DataFrame.

Analytical Questions

  - What does the raw extracted text look like before cleaning?
  - What noise is present and how should it be removed?
  - What derived features would support NLP analysis?
  - How does the cleaned text differ from the raw text?
  - Is the DataFrame genuinely ready for downstream use?

Edit your Python file to:
  - inspect your own extracted text carefully
  - apply cleaning steps appropriate to the data
  - engineer features that support the analytical goals
  - document every decision with a comment explaining why
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
import re
import string

from bs4 import BeautifulSoup, Tag
import pandas as pd
import spacy

# Load the spaCy English model.
# This model provides tokenization, stopword lists, and linguistic annotations.
# It must be downloaded once before use:
#   uv run python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# ============================================================
# Section 2. Define Helper Functions
# ============================================================


def _get_text(element: Tag | None, strip_prefix: str = "", separator: str = "") -> str:
    """Return element text or 'unknown' if element is None.

    Args:
        element (Tag | None): A BeautifulSoup Tag or None.
        strip_prefix (str): Text prefix to remove from the result.
        separator (str): Separator for get_text(); empty string by default.

    Returns:
        str: Extracted and cleaned text, or 'unknown' if element is None.
    """
    if element is None:
        return "unknown"
    text = element.get_text(separator=separator, strip=True)
    return text.replace(strip_prefix, "").strip() if strip_prefix else text


def _clean_text(text: str, nlp_model: spacy.language.Language) -> str:
    """Clean and normalize a text string for NLP analysis.

    Cleaning steps applied in order:
      1. Lowercase
      2. Remove punctuation
      3. Normalize whitespace
      4. Remove stopwords using spaCy

    Each step has a tradeoff documented below.

    Args:
        text (str): Raw text string to clean.
        nlp_model: Loaded spaCy language model.

    Returns:
        str: Cleaned text string.
    """
    # Step 1: Lowercase.
    # WHY: "The" and "the" are the same word for analysis purposes.
    # TRADEOFF: Proper nouns lose their case signal.
    text = text.lower()

    # Step 2: Remove punctuation.
    # str.maketrans creates a translation table that maps each punctuation
    # character to None (removes it).
    # WHY: Punctuation adds noise for frequency analysis.
    # TRADEOFF: Sentence boundary information is lost.
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Step 3: Normalize whitespace.
    # re.sub replaces one or more whitespace characters (\s+) with a single space.
    # WHY: Multiple spaces and newlines are artifacts of HTML extraction.
    text = re.sub(r"\s+", " ", text).strip()

    # Step 4: Remove stopwords using spaCy.
    # spaCy processes the text and returns a Doc object.
    # Each token has an is_stop attribute that is True for stopwords.
    # We keep only tokens that are not stopwords and not whitespace-only.
    # WHY: Common words (the, a, is) carry little semantic signal.
    # TRADEOFF: Some stopwords matter in certain contexts (e.g., "not").
    doc = nlp_model(text)
    text = " ".join(
        [token.text for token in doc if not token.is_stop and not token.is_space]
    )

    return text


# ============================================================
# Section 3. Define Run Transform Function
# ============================================================


def run_transform(
    soup: BeautifulSoup,
    LOG: logging.Logger,
) -> pd.DataFrame:
    """Transform HTML into a clean, analysis-ready DataFrame.

    Args:
        soup (BeautifulSoup): Validated BeautifulSoup object.
        LOG (logging.Logger): The logger instance.

    Returns:
        pd.DataFrame: The transformed and analysis-ready dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    LOG.info("Extracting metadata from HTML")
    LOG.info(
        "We must manually inspect the HTML structure to identify the fields we want to extract."
    )
    LOG.info(
        "For this arXiv page, we can extract:"
        "\n- Title from <h1 class='title'>"
        "\n- Authors from <div class='authors'>"
        "\n- Abstract from <blockquote class='abstract'>"
        "\n- Primary subject from <div class='subheader'>"
        "\n- Submission date from <div class='dateline'>"
        "\n- ArXiv ID from canonical link"
    )
    LOG.info("Replace any missing content with `unknown` to ensure all are strings.")

    LOG.info("========================")
    LOG.info("PHASE 3.1: Extract raw fields from HTML")
    LOG.info("========================")

    # Extract fields using the same approach as Module 5.
    # See nlp-06-nlp-pipeline/src/nlp/stage03_transform.py for full explanation.
    # Code is refactored to use the internal function _get_text() helper.

    LOG.info("Inspect: does the raw data look right?")
    LOG.info("Look at the logged output. Does anything look surprising?")
    LOG.info("That is the first signal that cleaning is needed.")
    LOG.info("========================")

    # Extract fields using the same approach as Module 5.
    # See nlp-06-nlp-pipeline/src/nlp/stage03_transform.py for full explanation.

    LOG.info("------------------------")
    LOG.info("Project specific: Extract title, authors, abstract")
    LOG.info("------------------------")

    title_tag: Tag | None = soup.find("h1", class_="title")
    title: str = _get_text(title_tag, strip_prefix="Title:")
    LOG.info(f"Extracted title: {title}")

    authors_tag: Tag | None = soup.find("div", class_="authors")
    author_tags_list: list[Tag] = authors_tag.find_all("a") if authors_tag else []
    authors: str = (
        ", ".join([tag.get_text(strip=True) for tag in author_tags_list])
        .replace("Authors:", "")
        .strip()
        if authors_tag
        else "unknown"
    )
    LOG.info(f"Extracted authors: {authors}")

    abstract_tag: Tag | None = soup.find("blockquote", class_="abstract")
    abstract_raw: str = _get_text(abstract_tag, strip_prefix="Abstract:")
    LOG.info(f"Extracted abstract: {abstract_raw[:100]}...")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract subjects from subheader")
    LOG.info("------------------------")

    # Primary subject from <div class="subheader">
    subheader: Tag | None = soup.find("div", class_="subheader")

    # Subjects may be in the format "Subjects: cs.AI (primary); cs.LG; stat.ML"
    subjects: str = _get_text(subheader, strip_prefix="Subjects:")
    LOG.info(f"Extracted subjects: {subjects}")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract submission date from dateline")
    LOG.info("------------------------")

    # Submission date from <div class="dateline">
    dateline: Tag | None = soup.find("div", class_="dateline")
    date_submitted_str: str = _get_text(dateline)
    LOG.info(f"Extracted submission date: {date_submitted_str}")

    LOG.info("------------------------")
    LOG.info("Project specific: Extract arxiv_id from canonical link")
    LOG.info("------------------------")

    # The canonical link looks like this in the HTML <head>:
    #   <link rel="canonical" href="https://arxiv.org/abs/2602.20021"/>"
    canonical: Tag | None = soup.find("link", rel="canonical")

    if canonical is None:
        LOG.warning("Canonical link not found, setting arXiv ID to 'unknown'")
        arxiv_id: str = "unknown"
    else:
        href: str = str(canonical["href"])
        arxiv_id: str = href.split("/abs/")[-1]

    LOG.info(f"Extracted arxiv_id: {arxiv_id}")

    LOG.info("========================")
    LOG.info("PHASE 3.2: Clean and normalize text fields")
    LOG.info("========================")
    # This phase cleans the raw abstract text.
    # The _clean_text() helper documents each cleaning decision and
    # its tradeoffs. Read it before modifying.

    LOG.info("Inspect: compare abstract_raw to abstract_clean in the log.")
    LOG.info("Did we remove anything we should have kept?")
    LOG.info("Is there still noise that cleaning missed?")
    LOG.info("========================")

    abstract_clean: str = (
        _clean_text(abstract_raw, nlp) if abstract_raw != "unknown" else "unknown"
    )

    # Log before and after to make the cleaning effect visible
    LOG.info(f"  abstract (raw):   {abstract_raw[:120]}...")
    LOG.info(f"  abstract (clean): {abstract_clean[:120]}...")
    LOG.info(
        f"  characters removed: {len(abstract_raw) - len(abstract_clean)} "
        f"({100 * (1 - len(abstract_clean) / max(len(abstract_raw), 1)):.1f}%)"
    )

    LOG.info("========================")
    LOG.info("PHASE 3.3: Engineer derived features")
    LOG.info("========================")
    # This phase adds derived fields that support NLP analysis.
    # These fields do not exist in the source HTML:
    # they are computed from the cleaned text.
    #
    # Derived features added here:
    #
    # abstract_word_count: number of words in the raw abstract.
    #   WHY: Consistent with Module 5; allows comparison across modules.
    #
    # tokens: list of individual words in the cleaned abstract.
    #   WHY: Tokenization is the foundation of all NLP analysis.
    #
    # token_count: number of tokens after cleaning and stopword removal.
    #   WHY: Useful for comparing document length across papers.
    #
    # unique_token_count: number of distinct tokens.
    #   WHY: Combined with token_count gives vocabulary richness.
    #
    # type_token_ratio: unique_tokens / total_tokens.
    #   WHY: Measures vocabulary richness (diversity of words used).
    #   A ratio close to 1.0 means almost every word is unique.
    #   A ratio close to 0.0 means many words are repeated.
    #
    # author_count: number of authors.
    #   WHY: Consistent with Module 5; allows comparison.
    #
    LOG.info("Inspect: do these derived fields look meaningful?")
    LOG.info("Would any additional features help the analysis?")
    LOG.info("========================")

    # Calculate derived field: abstract word count
    abstract_raw_word_count: int = (
        len(abstract_raw.split()) if abstract_raw != "unknown" else 0
    )
    LOG.info(f"  abstract_word_count: {abstract_raw_word_count}")

    # Calculate derived field: author count
    author_count: int = (
        len([a.strip() for a in authors.split(",")]) if authors != "unknown" else 0
    )
    LOG.info(f"  author_count:        {author_count}")

    # Tokenize the cleaned abstract
    tokens: list[str] = abstract_clean.split() if abstract_clean != "unknown" else []
    token_count: int = len(tokens)
    LOG.info(f"  token_count:         {token_count}")

    unique_token_count: int = len(set(tokens))
    LOG.info(f"  unique_token_count:  {unique_token_count}")

    # Type-token ratio: vocabulary richness
    type_token_ratio: float = (
        round(unique_token_count / token_count, 4) if token_count > 0 else 0.0
    )
    LOG.info(f"  type_token_ratio:    {type_token_ratio}")
    LOG.info(f"  top 10 tokens:       {tokens[:10]}")

    LOG.info("========================")
    LOG.info("PHASE 3.4: Build record and create DataFrame")
    LOG.info("========================")

    record = {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "subjects": subjects,
        "submitted": date_submitted_str,
        "abstract_raw": abstract_raw,
        "abstract_clean": abstract_clean,
        "tokens": " ".join(tokens),
        "abstract_word_count": abstract_raw_word_count,
        "token_count": token_count,
        "unique_token_count": unique_token_count,
        "type_token_ratio": type_token_ratio,
        "author_count": author_count,
    }

    df = pd.DataFrame([record])

    LOG.info(f"Created DataFrame with {len(df)} row and {len(df.columns)} columns")
    LOG.info(f"Columns: {list(df.columns)}")

    LOG.info("DataFrame Details")
    LOG.info(f"  Title: {title}")
    LOG.info(f"  Author count: {record['author_count']}")
    LOG.info(f"  Abstract word count: {record['abstract_word_count']}")
    LOG.info(f"  Token count (clean): {record['token_count']}")
    LOG.info(f"  Type-token ratio: {record['type_token_ratio']}")
    LOG.info(
        f"  DF preview:\n{
            df[
                ['arxiv_id', 'title', 'token_count', 'type_token_ratio', 'author_count']
            ].head()
        }"
    )

    LOG.info("Sink: Pandas DataFrame created")
    LOG.info("Transformation complete.")

    # Return the transformed DataFrame for use in the Load stage.
    return df
