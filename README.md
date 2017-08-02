# SE-WRL
The code for **Improve word representation learning with sememes**(ACL2017).

## How to Run

Using the following command to train word-sense-sememe embeddings.

```sh
cp SSA.c[SSA.c/MST.c/SAC.c/SAT.c] word2vec/word2vec.c
cd word2vec
make
./word2vec -train TrainFile -output vectors.bin -cbow 0 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 30 -binary 1 -iter 1 -read-vocab VocabFile -read-meaning SememeFile -read-sense Word_Sense_Sememe_File -min-count 1
```

``TrainFile`` is train data set. The following three files can be found in directory ``datasets``. ``VocabFile`` is the word vocabulary file, and ``SememeFile`` is the sememe vocabulary file. ``Word_Sense_Sememe_File`` is a file recording group information of word-sense-sememe.

Before training, you should replace ``word2vec/word2vec.c`` with one of the four files ``SSA.c/MST.c/SAC.c/SAT.c``.

## Data Set

``HowNet.txt`` is an Chinese knowledge base with annotated word-sense-sememe information.

``Sougo-T(sample).txt`` is a sample dataset extracted from ``Sougo-T``.

## Evaluation Set

``wordsim-240.txt`` and ``wordsim-297.txt`` in this files are utilized to evaluate the quality of word representations.

``analogy.txt`` in this file is utilized to evaluate models' capability of word analogy inference.

## Annotation Information

The annotation information is for the four files ``SSA.c/MST.c/SAC.c/SAT.c``. Annotation of the common code is only included in file ``SSA.c``.

## Revise

I'm sorry that we found bugs in programs. We have revised them. The new experiment results will be released on GitHub and new version of paper will be given. 

#### Word Similarity

|   Model   | Wordsim-240 | Wordsim-297 |
| :-------: | :---------: | :---------: |
|   CBOW    |    57.7     |    61.1     |
|   GloVe   |    59.8     |    58.7     |
| Skip-gram |    58.5     |    63.3     |
|    SSA    |    58.9     |  **64.0**   |
|    MST    |    59.2     |    62.8     |
|    SAC    |    58.1     |    60.5     |
|    SAT    |  **60.7**   |    62.5     |

#### Word Analogy

|   Model   | Capital  |   City   | Relationship |   All    |
| :-------: | :------: | :------: | :----------: | :------: |
|   CBOW    |   49.8   |   85.7   |   **86.0**   |   64.2   |
|   GloVe   |   57.3   |   74.3   |     81.6     |   65.8   |
| Skip-gram |   66.8   |   93.7   |     76.8     |   73.4   |
|    SSA    |   62.3   |   93.7   |     81.6     |   71.9   |
|    MST    |   65.7   |   95.4   |     82.7     |   74.5   |
|    SAC    |   76.5   |   97.7   |     80.1     |   80.7   |
|    SAT    | **82.1** | **98.9** |     80.1     | **84.3** |

