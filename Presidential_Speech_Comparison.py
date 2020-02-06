import nltk

# open and read files
w_file = open('1789-Washington.txt')
o_file = open('2009-Obama.txt')
t_file = open('2017-Trump.txt')
w_text = w_file.read()
o_text = o_file.read()
t_text = t_file.read()

### WORD COUNT ###
# tokenize each word
w_tokens = nltk.word_tokenize(w_text)
o_tokens = nltk.word_tokenize(o_text)

# create frequency dist and list most common
# NB: add padding above 20 to account for punctuation
w_freq_dist = nltk.FreqDist(w_tokens)
w_20_common = w_freq_dist.most_common(25)
o_freq_dist = nltk.FreqDist(o_tokens)
o_20_common = o_freq_dist.most_common(25)

# print word results
print('WASHINGTON')
for el in w_20_common:
    print(el)

print('\n')
print('****************************************************')
print('\n')

print('OBAMA')
for el in o_20_common:
    print(el)

##############################################################################################################

### SENTENCE LENGTH ###
# tokenize each sentence
# I originally did this:
# w_sent_tokens = w_text.split('.')
# but then I found sent_tokenize() in the NLTK docs:
w_sent_tokens = nltk.sent_tokenize(w_text)
o_sent_tokens = nltk.sent_tokenize(o_text)
t_sent_tokens = nltk.sent_tokenize(t_text)

def sentence_length(sent_tokens):
    sent_arr = []
    for el in sent_tokens:
        individual_sent = nltk.word_tokenize(el)
        sent_len = len(individual_sent)
        sent_arr.append(sent_len)
    avg_sent_len = int(sum(sent_arr) / len(sent_arr))
    print('Average sentence length:', avg_sent_len, 'words')

print('WASHINGTON')
sentence_length(w_sent_tokens)
print('OBAMA')
sentence_length(o_sent_tokens)
print('TRUMP')
sentence_length(t_sent_tokens)
