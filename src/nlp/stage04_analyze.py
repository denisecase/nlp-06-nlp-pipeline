"""stage04_analyze.py.

(MODIFY YOUR VERSION OF THIS FILE)

Source: analysis-ready Pandas DataFrame (from Transform stage)
Sink:   visualizations saved to data/processed/

======================================================================
THE ANALYST WORKFLOW: Analyze means look, not just calculate
======================================================================

Engineered features have no value until someone looks at them.

The Analyze stage makes the data visible:

  - frequency distributions show which words dominate the text
  - word clouds give an immediate gestalt of the content
  - bar charts allow comparison across documents or categories

In a single-document pipeline like this one, analysis is exploratory:
you are asking "what is in here?" before deciding what to do with it.

In a multi-document pipeline (Module 7 and beyond), analysis becomes
comparative: "how does this document differ from others?"

The same tools apply in both cases. The questions change.

======================================================================
PURPOSE AND ANALYTICAL QUESTIONS
======================================================================

Purpose

  Compute frequency distributions and produce visualizations
  that surface patterns in the cleaned text.

Analytical Questions

  - Which words appear most frequently in the cleaned abstract?
  - Does the frequency distribution look meaningful or noisy?
  - Does the word cloud reflect the actual topic of the paper?
  - What does the type-token ratio tell us about vocabulary richness?
  - Would a different cleaning strategy change the results?

Edit your Python file to:
  - adjust the number of top tokens shown
  - add additional visualizations
  - compare results across multiple documents
  - document what the visualizations reveal about your data
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

from collections import Counter
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# ============================================================
# Section 2. Define Helper Functions
# ============================================================


def _plot_top_tokens(
    tokens: list[str],
    top_n: int,
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Plot a horizontal bar chart of the top N most frequent tokens.

    Args:
        tokens (list[str]): List of tokens from the cleaned abstract.
        top_n (int): Number of top tokens to display.
        output_path (Path): Path to save the chart image.
        title (str): Chart title.
        LOG (logging.Logger): The logger instance.
    """
    # Count token frequencies
    # Counter returns a dictionary-like object mapping each token to its count.
    # .most_common(top_n) returns the top_n most frequent tokens as a list of
    # (token, count) tuples: [("agents", 3), ("language", 2), ...]
    counter = Counter(tokens)
    most_common = counter.most_common(top_n)

    if not most_common:
        LOG.warning("No tokens to plot.")
        return

    # Unpack the list of tuples into two separate lists using zip()
    # words will be the list of tokens, counts will be the list of their frequencies.
    # strict=False allows zip to handle cases where there are fewer than top_n tokens without raising an error.
    words, counts = zip(*most_common, strict=False)

    # Create horizontal bar chart
    # Reversing the order puts the most frequent token at the top

    # Use plt.subplots to create a figure and axis object.
    # figsize sets the size of the figure in inches.
    _, ax = plt.subplots(figsize=(10, 6))

    # barh creates a horizontal bar chart.
    # The y-values are the tokens (words),
    # and the x-values are their corresponding counts (frequencies).
    ax.barh(list(reversed(words)), list(reversed(counts)), color="steelblue")

    # Set labels and title
    ax.set_xlabel("Frequency")
    ax.set_title(title)

    # Adjust layout to prevent clipping of labels and title
    plt.tight_layout()

    # Save the figure to the specified output path with a resolution of 150 DPI.
    plt.savefig(output_path, dpi=150)

    # After saving, close the figure to free up memory and avoid displaying it in interactive environments.
    plt.close()

    LOG.info(f"  Saved bar chart to {output_path}")


def _plot_wordcloud(
    text: str,
    output_path: Path,
    title: str,
    LOG: logging.Logger,
) -> None:
    """Generate and save a word cloud from cleaned text.

    Word size reflects token frequency.
    More frequent words appear larger.

    Args:
        text (str): Space-joined cleaned token string.
        output_path (Path): Path to save the word cloud image.
        title (str): Title logged with the output.
        LOG (logging.Logger): The logger instance.
    """
    if not text or text == "unknown":
        LOG.warning("No text available for word cloud.")
        return

    # WordCloud generates the image from a string of space-separated words.
    # width/height set the image dimensions in pixels.
    # background_color sets the canvas color.
    # max_words limits the number of words shown.
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        max_words=80,
        colormap="viridis",  # or "plasma", "inferno", "magma", etc.
    ).generate(text)

    # Use plt.subplots to create a figure and axis object.
    # figsize sets the size of the figure in inches.
    _, ax = plt.subplots(figsize=(12, 6))

    # imshow displays the generated word cloud image on the axis.
    ax.imshow(wc, interpolation="bilinear")

    # axis("off") hides the axes for a cleaner look.
    ax.axis("off")

    # Set the title of the plot using the provided title argument.
    ax.set_title(title, fontsize=14)

    # Adjust layout to prevent clipping of labels and title
    plt.tight_layout()

    # Save the figure to the specified output path with a resolution of 150 DPI.
    plt.savefig(output_path, dpi=150)

    # After saving, close the figure to free up memory and avoid displaying it in interactive environments.
    plt.close()

    LOG.info(f"  Saved word cloud to {output_path}")


# ============================================================
# Section 3. Define Run Analyze Function
# ============================================================


def run_analyze(
    df: pd.DataFrame,
    LOG: logging.Logger,
    output_dir: Path = Path("data/processed"),
    top_n: int = 20,
) -> None:
    """Analyze the transformed DataFrame and produce visualizations.

    Args:
        df (pd.DataFrame): Analysis-ready DataFrame from Transform stage.
        LOG (logging.Logger): The logger instance.
        output_dir (Path): Directory to save visualization outputs.
        top_n (int): Number of top tokens to show in frequency chart.
    """
    LOG.info("========================")
    LOG.info("STAGE 04: ANALYZE starting...")
    LOG.info("========================")

    output_dir.mkdir(parents=True, exist_ok=True)

    # ============================================================
    # Phase 4.1: Extract token list and summary stats from DataFrame
    # ============================================================
    # The tokens column was stored as a space-joined string for CSV
    # compatibility. Split it back into a list for frequency analysis.
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.1: Extract tokens and summary statistics")
    LOG.info("========================")

    # Get the first (and only) row
    row = df.iloc[0]

    title: str = str(row.get("title", "unknown"))
    tokens_str: str = str(row.get("tokens", ""))
    token_count: int = int(row.get("token_count", 0))
    unique_token_count: int = int(row.get("unique_token_count", 0))
    type_token_ratio: float = float(row.get("type_token_ratio", 0.0))
    abstract_word_count: int = int(row.get("abstract_word_count", 0))
    author_count: int = int(row.get("author_count", 0))

    # Split the space-joined token string back into a list
    tokens: list[str] = tokens_str.split() if tokens_str else []

    LOG.info(f"  Paper: {title}")
    LOG.info(f"  Abstract word count (raw):    {abstract_word_count}")
    LOG.info(f"  Token count (clean):          {token_count}")
    LOG.info(f"  Unique token count:           {unique_token_count}")
    LOG.info(f"  Type-token ratio:             {type_token_ratio}")
    LOG.info(f"  Author count:                 {author_count}")

    # ============================================================
    # Phase 4.2: Frequency distribution - bar chart
    # ============================================================
    # A bar chart of the top N tokens gives an immediate sense of
    # what the text is about.
    #
    # Inspect: do the top tokens reflect the actual topic?
    # If common domain words (e.g. "model", "data") dominate,
    # consider whether they add signal or should be removed.
    # ============================================================

    LOG.info("========================")
    LOG.info(f"PHASE 4.2: Top {top_n} token frequency - bar chart")
    LOG.info("========================")

    _plot_top_tokens(
        tokens=tokens,
        top_n=top_n,
        output_path=output_dir / "case_top_tokens.png",
        title=f"Top {top_n} Tokens: {title}",
        LOG=LOG,
    )

    # ============================================================
    # Phase 4.3: Word cloud
    # ============================================================
    # A word cloud gives a gestalt view of the text.
    # Larger words appear more frequently.
    # It is less precise than a bar chart but easier to read at a glance.
    #
    # Inspect: does the word cloud match your expectation of the topic?
    # Surprises here are worth investigating in the token frequency list.
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.3: Word cloud")
    LOG.info("========================")

    _plot_wordcloud(
        text=tokens_str,
        output_path=output_dir / "case_wordcloud.png",
        title=f"Word Cloud: {title}",
        LOG=LOG,
    )

    # ============================================================
    # Phase 4.4: Log top tokens for inline inspection
    # ============================================================
    # Even without opening the chart files, the log output lets you
    # inspect the top tokens directly in the terminal.
    # This is the text equivalent of looking at the bar chart.
    # ============================================================

    LOG.info("========================")
    LOG.info("PHASE 4.4: Top token summary (inline)")
    LOG.info("========================")

    counter = Counter(tokens)
    top_tokens = counter.most_common(top_n)

    LOG.info(f"  Top {top_n} tokens by frequency:")
    for rank, (word, count) in enumerate(top_tokens, start=1):
        LOG.info(f"    {rank:>3}. {word:<30} {count}")

    LOG.info("Sink: visualizations saved to data/processed/")
    LOG.info("Analysis complete.")
