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

## TODO

Because of the size of train data is too large, I do not upload it. In the future, some eclectic measure will be conducted.

We will update the result embeddings of our models on GitHub.