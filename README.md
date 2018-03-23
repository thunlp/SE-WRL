# SE-WRL
This the the lab code for **Improved Word Representation Learning with Sememes** (ACL2017). Sememes are minimum semantic units of word meanings, and the meaning of each word sense is typically composed by several sememes. Since sememes are not explicit for each word, people manually annotate word sememes and form linguistic common-sense knowledge bases. In this paper, we present that, word sememe information can improve word representation learning (WRL), which maps words into a low-dimensional semantic space and serves as a fundamental step for many NLP tasks. The key idea is to utilize word sememes to capture exact meanings of a word within specific contexts accurately. More specifically, we follow the framework of Skip-gram and present three sememe-encoded models to learn representations of sememes, senses and words, where we apply the attention scheme to detect word senses in various contexts. We conduct experiments on two tasks including word similarity and word analogy, and our models significantly outperform baselines. The results indicate that WRL can benefit from sememes via the attention scheme, and also confirm our models being capable of correctly modeling sememe information.

## How to Run

Using the following command to train word-sense-sememe embeddings.

```sh
cp SSA.c[SSA.c/MST.c/SAC.c/SAT.c] word2vec/word2vec.c
cd word2vec
make
./word2vec -train TrainFile -output vectors.bin -cbow 0 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 30 -binary 1 -iter 1 -read-vocab VocabFile -read-meaning SememeFile -read-sense Word_Sense_Sememe_File -min-count 1 -alpha 0.025
```

``TrainFile`` is train data set. The following three files can be found in directory ``datasets``. ``VocabFile`` is the word vocabulary file, and ``SememeFile`` is the sememe vocabulary file. ``Word_Sense_Sememe_File`` is a file recording group information of word-sense-sememe.

Before training, you should replace ``word2vec/word2vec.c`` with one of the four files ``SSA.c/MST.c/SAC.c/SAT.c``.

## Data Set

``HowNet.txt`` is an Chinese knowledge base with annotated word-sense-sememe information.

``Sogou-T(sample).txt`` is a sample dataset extracted from ``Sogou-T``.

Complete training dataset ``Clean-SogouT`` is released in [https://pan.baidu.com/s/1kXgkyJ9](https://pan.baidu.com/s/1kXgkyJ9)(password: f2ul).

## Evaluation Set

``wordsim-240.txt`` and ``wordsim-297.txt`` in this files are utilized to evaluate the quality of word representations.

``analogy.txt`` in this file is utilized to evaluate models' capability of word analogy inference.

## Annotation Information

The annotation information is for the four files ``SSA.c/MST.c/SAC.c/SAT.c``. Annotation of the common code is only included in file ``SSA.c``.

## Errata

We are sorry that we have found some bugs in our algorithm implementation, and have fixed them in the github version. The new experiment results are released on GitHub as follows and we have also updated the [paper] (http://thunlp.org/~lzy/publications/acl2017_sememe.pdf). The new results still confirm the general idea and conclusion of our paper.

#### Word Similarity

|   Model   | Wordsim-240 | Wordsim-297 |
| :-------: | :---------: | :---------: |
|   CBOW    |    57.7     |    61.1     |
|   GloVe   |    59.8     |    58.7     |
| Skip-gram |    58.5     |    63.3     |
|    SSA    |    58.9     |  **64.0**   |
|    MST    |    59.2     |    62.8     |
|    SAC    |    59.1     |    61.0     |
|    SAT    |  **61.2**   |    63.3     |

#### Word Analogy

|   Model   | Capital  |   City   | Relationship |   All    |
| :-------: | :------: | :------: | :----------: | :------: |
|   CBOW    |   49.8   |   85.7   |   **86.0**   |   64.2   |
|   GloVe   |   57.3   |   74.3   |     81.6     |   65.8   |
| Skip-gram |   66.8   |   93.7   |     76.8     |   73.4   |
|    SSA    |   62.3   |   93.7   |     81.6     |   71.9   |
|    MST    |   65.7   |   95.4   |     82.7     |   74.5   |
|    SAC    |   79.2   |   97.7   |     75.0     |   81.0   |
|    SAT    | **82.6** | **98.9** |     80.1     | **84.5** |

