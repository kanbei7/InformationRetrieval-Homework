# 554 Information Retrieval hwk1
# @Author: eric
# @Date: Oct 11, 2017
# REMOVING PUNC MARKS
# NOT DOING STEMING
# NOT REMOVING STOP WORDS

import os
import math
import pandas as pd

input_path = './transcripts/'
log = math.log
punclst = ['\"', ',' , '.' , '?' , '!' , ':' , ';' , '|' , '\\' , '/' , '<' , '>' \
,'[' , ']' , '{' ,'}' , '-' , '_' , '+' , '=' , '(' , ')' , '*' , '&' , '^' , '$' , '#' \
,'@' ,'!' , '~' , '`']

flst = os.listdir(input_path)
flst = [x for x in flst if x.endswith('.txt')]

def clean_str(string):
	for c in punclst:
		string = string.replace( c , ' ')
	return ' '.join(string.strip().lower().split())

def getIdf(w,flst):
	N = 1.0
	for fname in flst:
		with open(input_path + fname, 'r') as f:
			N += int( w in clean_str(' '.join(f.readlines())).split() )	
	return log(len(flst)/N , 2)

#+++++ Q1 +++++#
ans1 = 0  
for fname in flst:
	with open(input_path + fname, 'r') as f:
		ans1 += len( clean_str(' '.join(f.readlines())).split() )

print ('Number of tokens: %d'%ans1)

#+++++ Q2 +++++#
ans2 = 0
s = []
for fname in flst:
	with open(input_path + fname, 'r') as f:
		s += clean_str(' '.join(f.readlines())).split()
ans2 = len(pd.Series(s).unique())
print ('Number of unique words: %d'%ans2)

#+++++ Q3 +++++#
ans3 = 0
s = []
for fname in flst:
	with open(input_path + fname, 'r') as f:
		s += clean_str(' '.join(f.readlines())).split()
cnt = pd.Series(s).value_counts().to_dict()
ans3 = len([w for w in cnt.keys() if cnt[w]==1] )
print ('Number of words occurred only once: %d'%ans3)

#+++++ Q4 +++++#
output = 'hwk1.csv'
s = []
for fname in flst:
	with open(input_path + fname, 'r') as f:
		s += clean_str(' '.join(f.readlines())).split()
cnt = pd.Series(s).value_counts().to_dict()
top30 = sorted([(w , cnt[w]) for w in cnt.keys() if cnt[w]>1] , key = lambda x:x[1] , reverse = True)[:30]

with open(output,'w') as fout:
	for t in top30:
		w = t[0]
		tf = cnt[w]
		idf = getIdf(w , flst)
		p = 1.0 * tf/ans1
		ctxt = [w , tf , idf , tf*idf , p]
		fout.writelines(','.join([str(x) for x in ctxt])+'\n')

#+++++ Q5 +++++#
ans5 = 1.0 * ans1 / len(flst)
print ('Average number of word tokens per doc: %.2f'%ans5)
