# From Rules to Attention: The Evolution of NLP Tools (Optional)

## Introduction

Understanding _how_ NLP tools work (and how they differ) separates
an analyst who can apply a library
from one who can choose the right tool,
diagnose failures, and explain results to stakeholders.

This document traces the evolution from
count-based and rule-based NLP approaches
(as implemented in tools like **spaCy**)
to modern large language models (**LLMs**).
The progression is a conceptual ladder to understanding
why modern AI NLP works the way it does.

The goal is to understand how each step
**improves the ability to represent meaning in text**.
There is no need to master this evolution,
it's offered as optional background for those interested
in how modern NLP evolved.

## Generation 1: Count-Based and Rule-Based NLP

Early NLP systems (1950s–1980s) primarily relied on counting, matching,
and applying hand-crafted linguistic rules.
These systems are not considered "machine learning" as they did not learn from data.
Their behavior was _explicitly programmed_.

A **stopword list** is a manually curated list of common words
(the, a, is, of) that carry little analytical signal.
Removing them reduces noise before analysis.

A **POS tagger** assigns grammatical roles to words
(noun, verb, adjective) using pre-trained statistical patterns learned from labeled text.
The word "run" is tagged differently in "I run every day" vs "a run of bad luck"
based on surrounding words in a fixed window.

A **named entity recognizer (NER)** identifies and classifies named things in text:
people, organizations, locations, dates, products.
spaCy's NER model learns statistical patterns in labeled text
(e.g., titles like "Dr." often precede person names).

These tools work well and remain fast, cheap, and auditable.
Their limitation is that meaning is determined by local context,
i.e., a fixed window of surrounding words, rather than
by the full sentence or document.

The word "bank" in "river bank" and "bank account" looks identical
to a count-based or rule-based system.
The tool cannot distinguish them without additional rules.

## Generation 2: Word Vectors and Static Embeddings

Word vector models (
[Word2Vec](https://www.tensorflow.org/text/tutorials/word2vec),
[GloVe](https://nlp.stanford.edu/projects/glove/)
) introduced a fundamentally different idea:
represent
**each word as a point in a high-dimensional vector space**,
where **semantically similar words are geometrically close**.

"King" and "queen" are near each other.
"Paris" and "France" are near each other in the same way
"Berlin" and "Germany" are.

The famous demonstration:

```text
king - man + woman ≈ queen
```

This works because the model learns from large numbers
(e.g., billions) of word **co-occurrences**
and **encodes the relationships between words**
as **directions in vector space**.

spaCy's `en_core_web_md` and `en_core_web_lg` models include static word vectors.
They are called **static**
because each word has one fixed vector regardless of context.
"Bank" in "river bank" and "bank account" still gets the same vector:
an average of all the contexts
the word appears in across the training corpus.

Static embeddings are a major step forward from count-based models
but still cannot resolve meaning from context.

## Generation 3: Attention and Contextual Meaning (~2017)

The transformer architecture, introduced in the 2017 paper
[Attention Is All You Need](https://arxiv.org/abs/1706.03762),
solved the context problem.

The key mechanism is **attention**.
For every word in a sentence,
the model computes weighted relationships between tokens to determine:
_which other words in this sentence matter most_
for understanding this word right now?

In "I went to the river bank to fish,"
the word "bank" assigns higher attention weight to
"river" and "fish."
In "I went to the bank to deposit a check,"
the same word "bank" assigns higher attention weight to
"deposit" and "check."

The result is a **dynamic contextual representation**:
the same word gets a different numeric representation depending on
the full sentence it appears in.
This is how LLMs resolve ambiguity, understand metaphor,
and answer questions about complex text.

This is fundamentally different from **positional adjacency (Generation 1)**
and **static similarity (Generation 2)**.
The meaning is not stored in a fixed vector.
It is computed fresh for each occurrence based on everything around it.

## The Progression Illustrated

A [Toy GPT model](https://toy-gpt.github.io/toy-gpt-chat/)
([repo](https://github.com/toy-gpt/toy-gpt-chat))
demonstrates the conceptual ladder:

| Model                | What it learns              | Limitation                |
| -------------------- | --------------------------- | ------------------------- |
| Unigram              | Overall word frequency      | No context at all         |
| Bigram               | What word follows this word | One-word window           |
| Context-2, Context-3 | Short positional patterns   | Fixed, small window       |
| Embeddings           | Static semantic similarity  | No contextual adjustment  |
| Attention            | Dynamic contextual meaning  | Computationally expensive |

Each step resolves a limitation of the previous one.
Attention resolves the limitation that embeddings could not.

## spaCy Preprocessing Still Matters

LLMs understand language contextually and
**do not require explicit preprocessing steps**
such as stopword removal or POS tagging to process text.

So why do production pipelines still use tools like spaCy?

### Cost and speed

Calling an LLM API costs money per input token processed.
Preprocessing with spaCy to remove boilerplate, normalize text,
and extract only the relevant fields reduces the number of tokens sent to the LLM,
reducing cost and latency.

### Auditability

spaCy pipelines are deterministic and inspectable.
Every cleaning decision is visible in code.
LLM outputs are probabilistic and harder to audit.
In regulated industries (healthcare, finance, legal) this matters.

### Scale

Processing millions of documents with an LLM is slow and expensive.
A spaCy pipeline can process large volumes of documents quickly
(often thousands per second, depending on hardware).

### Structured extraction

Pulling named entities, dates, or POS patterns at scale
is faster and cheaper with spaCy than with an LLM.

Pipeline processing skills (e.g., inspect, clean, engineer features, validate)
help prepare data for LLMs; they do not describe how LLMs work internally.
These preparation skills help maintain and enhance analyst value
as NLP models become increasingly automated.

## Summary

| Generation        | Representative tools         | How meaning is determined           |
| ----------------- | ---------------------------- | ----------------------------------- |
| Count/rule-based  | spaCy (sm), NLTK, TF-IDF     | Frequency and local adjacency       |
| Static embeddings | spaCy md/lg, Word2Vec, GloVe | Geometric proximity in vector space |
| Contextual / LLMs | BERT, GPT, Claude            | Dynamic attention over full context |

spaCy spans capabilities associated with Generations 1 and 2.
It is fast, auditable, and sufficient for most preprocessing tasks.
Modern LLMs operate at Generation 3,
but work best when their input data has been
carefully prepared using pipelines built on foundational NLP principles.

---

[◄ Back to 🏠 Home](index.md)
