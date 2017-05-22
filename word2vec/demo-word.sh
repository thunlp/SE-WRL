make
time ./word2vec -train /data/disk1/private/nyl/copus2.txt -output baseline_cbow.bin -cbow 1 -size 200 -window 8 -negative 25 -hs 0 -sample 1e-4 -threads 30 -binary 0 -iter 1 -min-count 50 -read-vocab ../ReadVocab2700000000
