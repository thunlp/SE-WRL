
bound = [':', '}']
r = open('HowNet.txt', 'r')
word_sememe_dict = {}

def readItem():
	while r.readline()[:2] != 'NO':
		pass
	word = r.readline()[:-1].split('=')[1]
	while r.readline()[:3] != 'E_E':
		pass
	DEF = r.readline()[:-1].split('=')[1]
	sememes = []
	sememe = ''
	begin = False
	for x in DEF:
		if x == '|':
			begin = True
			continue
		if x in bound:
			begin = False
			sememes.append(sememe)
			sememe = ''
			continue
		if begin:
			sememe += x
	sememes = sorted(sememes)
	if word_sememe_dict.has_key(word):
		word_sememe_dict[word].append(sememes)
	else:
		word_sememe_dict[word] = [sememes]


for key, value in word_sememe_dict.items():
	word_sememe_dict[key] = list(set(value))
w = open('Word_Sense_Sememe.txt', 'w')
for key, values in word_sememe_dict.items():
	w.write(key)
	w.write(' ')
	w.write(len(values))
	w.write(' ')
	for value in values:
		w.write(len(value))
		w.write(' ')
		for sememe in value:
			w.write(sememe)
			w.write(' ')
	w.write('\n')
w.close()
