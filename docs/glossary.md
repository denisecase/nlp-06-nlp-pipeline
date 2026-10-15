# Glossary

This module focuses on integrated NLP pipelines,
linguistic features, text analysis,
and connections to modern language models.

## Quick Lookup

### NLP Pipeline and Features

- **EVTAL** - Extract, Validate, Transform, Analyze, Load.
- **NLP Feature** - a measurable property derived from text.
- **Feature Engineering** - constructing useful variables from existing data.
- **Token Count** - the number of tokens in a text.
- **Unique Token Count** - the number of distinct tokens.
- **Vocabulary Size** - the number of distinct tokens in a document or corpus.
- **Type-Token Ratio (TTR)** - the proportion of distinct tokens.
- **Linguistic Tokenization** - dividing text using language-aware rules.

### Linguistic Analysis and spaCy

- **Linguistic Annotation** - information assigned to language units.
- **POS Tagging** - assigning grammatical categories to tokens.
- **NER** - identifying and classifying named entities.
- **spaCy** - a Python library for natural language processing.
- **spaCy Pipeline** - trained components for linguistic analysis.
- **spaCy Doc** - a container for processed text and linguistic annotations.

### Python Analysis and Visualization

- **Counter** - a Python class for counting occurrences.
- **Matplotlib** - a Python library for creating visualizations.
- **WordCloud** - a Python library for generating word clouds.
- **Bar Chart** - a chart comparing values using bars.
- **Word Cloud** - a visualization emphasizing frequent words.

### Neural Networks and Language Models

- **Neural Network** - a computational model that learns patterns from data.
- **Embedding** - a numerical vector representation.
- **Static Embedding** - a fixed learned representation of a word.
- **Contextual Embedding** - a representation influenced by surrounding context.
- **Attention Mechanism** - a method for weighting relationships between representations.
- **Transformer** - a neural network architecture based on attention.
- **Large Language Model (LLM)** - a large-scale model trained to process and generate language.

## NLP Pipeline and Features

### EVTAL (Extract, Validate, Transform, Analyze, Load)

**EVTAL** extends the EVTL pipeline architecture
by introducing an explicit Analyze stage.

The five stages are:

- **Extract** - acquire data from a source.
- **Validate** - check data against defined requirements.
- **Transform** - prepare data and create analytical features.
- **Analyze** - examine features and produce analytical results.
- **Load** - persist the resulting data or artifacts.

Separating analysis from transformation
makes the analytical workflow easier
to inspect, test, and interpret.

### NLP Feature

An **NLP feature** is a measurable
or derived property of text
used for analysis or modeling.

Examples include:

- Token counts.
- Vocabulary size.
- Word frequencies.
- Grammatical annotations.
- Numerical text representations.

Features provide a way to represent
properties of language as data.

### Feature Engineering

**Feature engineering** is the process
of constructing useful variables
from existing data.

In NLP, feature engineering may involve:

- Calculating text statistics.
- Extracting linguistic properties.
- Counting words or tokens.
- Creating numerical representations.
- Combining existing features.

Feature engineering makes selected
properties of text available
for analysis or modeling.

### Token Count

**Token count** is the number
of tokens in a text.

Token counts depend on the tokenizer
and any preprocessing operations applied.

Counts produced by different tokenizers
are not necessarily comparable.

For example, the same text may produce
different token counts when processed
by a word tokenizer or a subword tokenizer.

### Unique Token Count

**Unique token count** is the number
of distinct tokens in a text.

Repeated occurrences of the same token
are counted only once.

Comparing unique token count
to total token count reveals
how much vocabulary repetition exists.

### Vocabulary Size

**Vocabulary size** is the number
of distinct tokens in a document or corpus.

It provides one measure
of lexical diversity.

Vocabulary size depends on tokenization
and preprocessing decisions.

### Type-Token Ratio (TTR)

**Type-token ratio** is the proportion
of distinct tokens in a token sequence.

```text
TTR = unique token count / total token count
```

For a nonempty token sequence,
TTR is greater than zero and at most one.

- Values close to 1.0 indicate a high proportion of unique tokens.
- Lower values indicate more repetition.

TTR is sensitive to document length
and preprocessing choices.

Short texts often have higher TTR values
than longer texts, even when the underlying
language patterns are similar.

Comparisons therefore require care.

### Linguistic Tokenization

**Linguistic tokenization** divides text
into units using language-aware rules.

Simple whitespace tokenization
separates text at spaces and other whitespace.

For example:

```python
text = "NLP is fun"

tokens = text.split()

# ["NLP", "is", "fun"]
```

This approach is simple and fast
but does not account for punctuation,
contractions, or language-specific conventions.

Linguistic tokenizers may recognize:

- Words and punctuation.
- Contractions.
- Abbreviations.
- Hyphenated expressions.
- Language-specific token boundaries.

For example, an English tokenizer
may split `"don't"` into `"do"` and `"n't"`.

spaCy uses language-specific tokenization rules
that can be customized.

Linguistic tokenization is distinct
from subword tokenization,
which is commonly used by large language models.

Neither approach guarantees
that individual tokens correspond
to complete words or semantic units.

## Linguistic Analysis and spaCy

### Linguistic Annotation

**Linguistic annotation** assigns
descriptive information to language units.

Annotations may identify:

- Grammatical roles.
- Named entities.
- Sentence boundaries.
- Syntactic relationships.
- Other linguistic properties.

Annotations may be created manually
or by automated NLP systems.

They provide structured information
for subsequent analysis.

### Part-of-Speech (POS) Tagging

**Part-of-speech tagging** assigns
grammatical categories to tokens.

Common categories include:

- Noun.
- Verb.
- Adjective.
- Adverb.
- Pronoun.
- Preposition.

POS tagging supports linguistic analysis,
information extraction,
and text classification.

In spaCy, a token's predicted
part-of-speech category is available through:

```python
token.pos_
```

The assigned category depends
on the context and the linguistic model.

### Named Entity Recognition (NER)

**Named entity recognition (NER)** identifies
and classifies references to entities in text.

Common entity categories include:

- People.
- Organizations.
- Locations.
- Dates.
- Products.
- Events.

NER supports information extraction
and structured analysis of documents.

In spaCy, detected named entities
are available through:

```python
doc.ents
```

NER results depend on the model,
training data, and context.

A detected entity is a model prediction,
not independent verification
of the entity's existence or identity.

### spaCy (Python Library)

**spaCy** is a Python library
for natural language processing.

It provides tools for:

- Linguistic tokenization.
- Stopword identification.
- Part-of-speech tagging.
- Named entity recognition.
- Dependency parsing.
- Linguistic feature extraction.

spaCy supports reusable processing pipelines
and is widely used for applied NLP.

See [spaCy Documentation](https://spacy.io/).

### spaCy Pipeline

A **spaCy pipeline** is a package
containing configuration and components
used to process language.

Depending on the pipeline, components may provide:

- Part-of-speech predictions.
- Syntactic dependency analysis.
- Named entity recognition.
- Other linguistic annotations.
- Word vectors for similarity analysis.

The small `en_core_web_sm`
provides a relatively small English pipeline.

Other English packages include:

- `en_core_web_md` - medium-sized pipeline with static word vectors.
- `en_core_web_lg` - larger pipeline with static word vectors.
- `en_core_web_trf` - transformer-based processing components.

Capabilities and resource requirements vary.

Tokenization itself does not necessarily
require a trained statistical model.

### spaCy Doc

A **spaCy Doc** is an object
representing processed text.

It contains tokens and may contain
linguistic annotations produced
by pipeline components.

For example:

```python
doc = nlp("Natural language processing is useful.")
```

The `Doc` object can provide access to:

- Individual tokens.
- Part-of-speech tags.
- Named entities.
- Sentence boundaries.
- Syntactic information.

Iterating over a Doc
produces individual `Token` objects.

```python
for token in doc:
    print(token.text, token.pos_)
```

The available annotations depend
on the processing components
included in the pipeline.

## Python Analysis and Visualization

### collections.Counter (Python Library Class)

**Counter** is a Python standard library class
that counts occurrences of items
in an iterable or collection.

It is useful for calculating
token frequency distributions.

Example:

```python
from collections import Counter

counts = Counter(["cat", "dog", "cat"])

print(counts.most_common(2))

# [("cat", 2), ("dog", 1)]
```

The `.most_common(n)` method returns
the N most frequent items
as a list of `(item, count)` tuples.

Counter is convenient for frequency analysis
without requiring a separate tabular data structure.

### Matplotlib (Python Library)

**Matplotlib** is a Python library
for creating static and interactive visualizations.

Common visualizations include:

- Bar charts.
- Line charts.
- Histograms.
- Scatter plots.

Matplotlib can display figures
or save them as image files.

For example:

```python
import matplotlib.pyplot as plt

plt.savefig("token_frequencies.png")
```

Saving figures to files is useful
for automated pipelines
that run without an interactive display.

See [Matplotlib Documentation](https://matplotlib.org/).

### WordCloud (Python Library)

**WordCloud** is a Python library
that generates word cloud visualizations
from text or word frequencies.

Word size typically reflects frequency.

Word clouds provide a quick visual impression
of frequently occurring terms.

They are less precise than frequency tables
or bar charts for comparing exact counts.

See [WordCloud Documentation](https://amueller.github.io/word_cloud/).

### Bar Chart (Visualization)

A **bar chart** uses horizontal or vertical bars
to represent the values of categories.

Bar length or height
corresponds to the measured value.

In text analysis, bar charts can display
the most frequently occurring tokens.

Bar charts support direct comparison
of token frequencies
and are useful when numerical precision matters.

### Word Cloud (Visualization)

A **word cloud** is a visualization
that displays words using visual properties
such as size to represent frequency or importance.

Larger words typically indicate
greater frequency or assigned weight.

Word clouds help provide
an overall impression of vocabulary.

However, word size is less precise
for quantitative comparison
than a frequency table or bar chart.

Word clouds should be interpreted
alongside other analytical results.

## Neural Networks and Language Models

### Neural Network (NN)

A **neural network** is a computational model
composed of interconnected processing units
organized into layers.

Neural networks learn patterns from data
by adjusting numerical parameters,
commonly called weights and biases.

During supervised training,
the model typically adjusts its parameters
to reduce a defined loss function
that measures prediction error.

Neural networks are loosely inspired
by biological neural systems,
but their computational behavior
is not equivalent to biological reasoning.

Different neural network architectures
support different kinds of tasks.

Examples include:

- Feedforward neural networks.
- Recurrent neural networks.
- Convolutional neural networks.
- Transformer networks.

Neural networks are foundational
to many modern NLP systems.

Earlier neural language models
used relatively shallow architectures.

Deep neural networks enabled
more expressive learned representations,
including contextual language representations.

Transformer-based language models
are examples of deep neural networks.

Unlike entirely rule-based systems,
neural networks learn statistical relationships
from training data.

Their predictions still require evaluation,
and training alone does not establish
that their outputs are reliable or correct.

### Embedding

An **embedding** is a numerical vector
representing an item in a learned space.

In NLP, embeddings may represent:

- Tokens.
- Words.
- Sentences.
- Documents.

Embeddings provide numerical representations
that can be used in statistical analysis
and machine learning.

Relationships between vectors
may capture patterns learned from data.

For example, embeddings of words
used in similar contexts
may have similar vector representations.

The meaning of similarity depends
on the embedding method,
training data, and comparison metric.

### Static Word Embedding

A **static word embedding** assigns
a fixed learned vector to a word
regardless of the context in which it appears.

Static embeddings capture
distributional relationships
learned from text corpora.

For example, the word `"bank"`
receives the same static representation
in these phrases:

- River bank.
- Bank account.

A static representation cannot directly
distinguish the meaning of each occurrence
using its surrounding sentence.

Examples of static embedding approaches include:

- Word2Vec.
- GloVe.
- FastText.

Some spaCy pipelines
also include static word vectors.

Static embeddings remain useful
for many similarity and classification tasks.

### Contextual Embedding

A **contextual embedding** represents
a token or other language unit
using information from its surrounding context.

The same word may receive
different representations
in different sentences.

For example, a contextual model
can produce different representations
for `"bank"` in:

- River bank.
- Bank account.

Contextual embeddings help models
represent differences in usage
and linguistic context.

They are important components
of modern transformer-based language models.

### Attention Mechanism

An **attention mechanism** computes
weighted combinations of representations
using relationships among input elements.

In NLP, attention allows
token representations to incorporate
information from other tokens.

The weights are calculated
from learned transformations
of the input representations.

For example, a model processing
a sentence may use information
from several surrounding tokens
when constructing a contextual representation.

Attention supports context-dependent
language representations.

Unlike fixed static embeddings,
contextual representations can vary
with the surrounding input.

Attention is a foundational mechanism
in transformer architectures.

However, attention weights are computational quantities
and should not automatically be interpreted
as explanations of model decisions.

See [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

### Transformer

A **transformer** is a neural network architecture
that uses attention mechanisms
to process relationships among sequence elements.

Transformers support
context-dependent representations
and can model relationships
between tokens across a sequence.

The original transformer architecture
introduced in *Attention Is All You Need*
used an encoder-decoder structure.

Common transformer configurations include:

- Encoder-based models for representing and analyzing text.
- Decoder-based models for generating text.
- Encoder-decoder models for sequence transformation.

Transformer architectures are widely used
in modern natural language processing.

They provide the foundation
for many contemporary large language models.

### Large Language Model (LLM)

A **large language model (LLM)** is a language model
with substantial learned capacity,
typically trained on large collections
of text or other language-related data.

Many contemporary LLMs
use transformer architectures.

LLMs learn statistical patterns
that support tasks such as:

- Text generation.
- Summarization.
- Question answering.
- Information extraction.
- Text transformation.
- Classification.

Transformer-based LLMs use learned representations
and attention mechanisms
to process contextual relationships.

Their outputs depend on:

- Training data and objectives.
- Model architecture.
- Input context.
- Generation settings.
- Additional training or adaptation.

LLMs generally do not require
traditional preprocessing operations
such as stopword removal or explicit POS tagging.

However, they still use tokenization
and may benefit from appropriate
data cleaning, formatting, and validation.

LLMs can produce fluent text
without guaranteeing factual correctness.

Their outputs require evaluation
against the intended task and context.

## Relationship to Traditional NLP

Traditional NLP methods and modern language models
provide different approaches to processing language.

Traditional approaches often use
explicit preprocessing,
linguistic annotations,
and engineered features.

Modern language models learn
many representations directly
from training data.

These approaches are not mutually exclusive.

Explicit preprocessing and feature engineering
remain useful when requirements include:

- Inspectability.
- Reproducibility.
- Computational efficiency.
- Clearly defined measurements.
- Structured information extraction.
- Domain-specific validation.

Understanding traditional NLP concepts
helps explain the foundations
and limitations of modern language models.

The choice of methods should depend
on the analytical task,
available resources,
and requirements for verification.

---

[◄ Back to 🏠 Home](index.md)
