# From Rules to Attention: The Evolution of NLP Tools (Optional)

## Introduction

Understanding _how_ NLP tools work (and how they differ) separates
an analyst who can apply a library
from one who can choose the right tool,
diagnose failures, and explain results to stakeholders.

This document traces a conceptual progression from
count-based and rule-based NLP approaches,
through statistical language processing and word embeddings,
to modern large language models (**LLMs**).

Tools such as **spaCy** combine several of these approaches,
including linguistic rules, trained statistical models,
and optional word vectors or transformer components.

The progression is a conceptual ladder for understanding
how NLP systems increasingly represent and use linguistic context.

The goal is to understand how each step
**improves the ability to represent meaning in text**.
There is no need to master this evolution,
it's offered as optional background for those interested
in how modern NLP evolved.

## Generation 1: Count-Based and Rule-Based NLP

Early NLP systems (1950s-1980s) often relied on counting,
pattern matching, and hand-crafted linguistic rules.

Rule-based systems follow explicitly programmed instructions
rather than learning their rules from training data.
Statistical methods also developed during this period
and became increasingly important in later NLP systems.

A **stopword list** identifies common words
(the, a, is, of) that may contribute little to
some frequency-based analyses.
Removing them can reduce noise,
but may also remove useful information.

A simple rule-based system can identify words,
match patterns, or recognize known names.
More advanced systems use statistical models
trained on examples of language.

A **POS tagger** assigns grammatical roles to words
(noun, verb, adjective).
Modern POS taggers commonly use trained statistical models
that consider the surrounding context.

A **named entity recognizer (NER)** identifies and
classifies entities such as people, organizations,
locations, and dates.
Modern NER systems also use trained models to predict
entity labels from linguistic context.

For example, spaCy's `en_core_web_sm` pipeline
includes trained statistical components for
POS tagging, dependency parsing, and NER.
These components are not simply hand-coded rules.

Count-based and rule-based approaches remain useful
because they can be efficient, inspectable, and reproducible.

However, simple frequency counts cannot distinguish
the meaning of "bank" in "river bank" and "bank account."
Rules can address specific cases, but require those
distinctions to be explicitly represented.

Statistical and neural approaches learn patterns
from training data and can use surrounding context
to make predictions.

## Generation 2: Word Vectors and Static Embeddings

Word vector models such as
[Word2Vec](https://www.tensorflow.org/text/tutorials/word2vec)
and [GloVe](https://nlp.stanford.edu/projects/glove/)
popularized learned numerical representations of words.

These models represent words as
**points in a high-dimensional vector space**,
where words used in similar contexts
often have related representations.

"King" and "queen" are near each other.
"Paris" and "France" are near each other in the same way
"Berlin" and "Germany" are.

The famous demonstration:

```text
king - man + woman ≈ queen
```

Note: This analogy illustrates relationships
that some embedding models learn and is not
guaranteed for every model or corpus.

This works because the model learns from large numbers
(e.g., billions) of word **co-occurrences**
and **encodes the relationships between words**
as **directions in vector space**.

spaCy's `en_core_web_md` and `en_core_web_lg` models include static word vectors.

They are called **static** because a given word
has the same learned vector regardless of the sentence.

For example, "bank" in "river bank" and "bank account"
uses the same static word vector.

That vector reflects patterns learned across
the word's occurrences in the training corpus.
It is not necessarily a literal average of those contexts.

Static embeddings capture useful statistical relationships,
but the embedding itself **does not change** according
to the word's current context.

Other model components can still use surrounding words
to interpret that fixed representation.

## Generation 3: Attention and Contextual Meaning (~2017)

Neural language models developed increasingly powerful ways
to represent words using surrounding context.

Recurrent neural networks and other contextual models
could already use information from neighboring words.

The transformer architecture, introduced in the 2017 paper
[Attention Is All You Need](https://arxiv.org/abs/1706.03762),
made self-attention central to a highly influential
neural network architecture.

The key mechanism is **attention**.

Attention computes weighted relationships between token
representations, allowing a model to combine information
from different parts of the available context.

Consider two sentences:

- "I went to the river bank to fish."
- "I went to the bank to deposit a check."

A contextual model can produce different representations
of "bank" because the surrounding words differ.

The resulting **contextual representation**
depends on the word's occurrence and the context
available to the model.

Unlike a static word embedding,
this representation can change between sentences.

Transformer architectures differ in how much context
each token can access.
For example, many generative LLMs use causal attention,
which prevents a token from attending to future tokens.

Contextual representations help language models
handle ambiguity and relationships within text.
They do not guarantee correct interpretation or reasoning.

Transformers substantially advanced contextual modeling,
but attention and contextual language processing
existed before 2017.

## The Progression Illustrated

A [Toy GPT model](https://toy-gpt.github.io/toy-gpt-chat/)
([repo](https://github.com/toy-gpt/toy-gpt-chat))
demonstrates the conceptual ladder:

| Model                 | What it represents                    | Limitation                            |
| --------------------- | ------------------------------------- | ------------------------------------- |
| Unigram               | Overall token frequency               | No sequence context                   |
| Bigram                | Adjacent token relationships          | Very limited context                  |
| Context-2, Context-3  | Short token sequences                 | Fixed context size                    |
| Static embeddings     | Learned word relationships            | Fixed word representation             |
| Transformer attention | Context-dependent token relationships | Computational cost and context limits |

Each approach adds capabilities for representing
patterns and relationships in language.

Attention is a mechanism within a model,
not a complete language model.

Later approaches do not make earlier techniques obsolete.
They address different problems and involve different
tradeoffs in cost, complexity, and interpretability.

## spaCy Preprocessing Still Matters

LLMs process language contextually and generally
do not require traditional preprocessing steps
such as stopword removal or POS tagging.

Aggressive cleaning may remove useful information,
including punctuation, negation, formatting,
and relationships between words.

So why do production pipelines still use tools like spaCy?

### Cost and speed

LLM API costs often depend on the number of input
and output tokens processed.

Extracting relevant content, removing unrelated
boilerplate, and selecting appropriate documents
can reduce the amount of text sent to an LLM.

Traditional NLP tools can support these operations,
although unnecessary preprocessing adds work
and may reduce input quality.

### Auditability

Rule-based preprocessing steps can be explicitly
documented and reproduced.

spaCy's trained statistical components also produce
inspectable outputs, but their predictions may be incorrect.

Keeping model versions, configuration, and processing
decisions consistent supports reproducibility.

LLM-generated outputs require their own validation,
particularly when accuracy and traceability matter.

### Scale

Traditional NLP pipelines can process large collections
of documents efficiently.

For operations such as tokenization, pattern matching,
and structured extraction, these approaches may require
fewer computational resources than large generative models.

The appropriate choice depends on the task,
required accuracy, and available resources.

### Structured extraction

spaCy provides tools for extracting entities,
linguistic annotations, and rule-based patterns.

For well-defined extraction tasks, these methods
can be practical alternatives to generative LLMs.

More complex extraction tasks may benefit from
LLMs or hybrid approaches.

Pipeline processing skills
(e.g., inspect, clean, engineer features, validate)
help prepare data for analysis and downstream applications.

These skills remain relevant as NLP systems evolve,
but preprocessing decisions should be evaluated
against the requirements of the intended model or task.

## Summary

| Approach          | Representative tools                                 | Primary capability                           |
| ----------------- | ---------------------------------------------------- | -------------------------------------------- |
| Count/rule-based  | Frequency counts, regex, spaCy rule-based components | Explicit counts and rules                    |
| Statistical NLP   | spaCy trained taggers and NER                        | Learned predictions using linguistic context |
| Static embeddings | Word2Vec, GloVe, spaCy md/lg word vectors            | Fixed learned word representations           |
| Contextual models | RNNs, BERT, transformer-based LLMs                   | Context-dependent representations            |

These approaches are not mutually exclusive.

spaCy combines rule-based and statistical NLP
and supports multiple types of language representations,
including static vectors and transformer-based components.

Modern transformer-based LLMs use attention
to compute contextual representations.
They can process text without many traditional
preprocessing steps, but still benefit from
appropriate data selection, extraction,
validation, and quality controls.

Understanding these approaches helps analysts
choose methods that fit a problem,
rather than assuming that a newer model
is always the most appropriate tool.

---

[◄ Back to 🏠 Home](index.md)
