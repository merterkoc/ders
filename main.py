import nltk as n
#nltk.download('gutenberg')
gb = n.corpus.gutenberg
whitman = n.corpus.gutenberg.words('whitman-leaves.txt')
print(len(whitman))
print(whitman[:10])
#whitman_sents = n.corpus.gutenberg.sents('whitman-leaves.txt')
text = n.Text(whitman)
text.concordance('Stage')
print('---------')
text.common_contexts(['Stage'])
fd = n.FreqDist(whitman)
print(fd.most_common(10))
sw = set(n.corpus.stopwords.words('english'))
print(len(sw))
whitman_filtered=[w for w in whitman if w.lower() not in sw]
fd = n.FreqDist(whitman_filtered)
print('----*---')
print(fd.most_common(10))
import string
p=set(string.punctuation)
whitman_filtered =[w for w in whitman if w.lower() not in sw and w.lower() not in p]
fd = n.FreqDist(whitman_filtered)
print('----*---')
print(fd.most_common(10))