
# coding: utf-8

# In[1]:

from spacy.en import English
parser = English()
import collections


# In[4]:

def POS(text):
    parsedData = parser(text)
    sents = []
    sent = []
    tagged_sents = []
        # the "sents" property returns spans
        # spans have indices into the original string
        # where each index value represents a token
    for span in parsedData.sents:
            # go from the start to the end of each span, returning each token in the sentence
            # combine each token using join()
        sent = ''.join(parsedData[i].string for i in range(span.start, span.end)).strip()
        sents.append(sent)

        # Let's look at the part of speech tags of the first sentence
    for span in parsedData.sents:
        sent = [parsedData[i] for i in range(span.start, span.end)]
        temp = []
        for token in sent:
            i = (token.orth_, token.pos_)
            temp.append(i)
        tagged_sents.append(temp)
    
    return tagged_sents


# In[ ]:

from unicodeCSVReader import UnicodeReader, UnicodeWriter
import csv

def extract_candidate_chunks(text, grammar=r'KT: {(<ADJ>​* <NOUN.*>+ <ADP>)? <ADJ>*​ <NOUN.*>+}'):
    import itertools, nltk, string
   
    # exclude candidates that are stop words or entirely punctuation
    punct = set(string.punctuation)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    # tokenize, POS-tag, and chunk using regular expressions
    chunker = nltk.chunk.regexp.RegexpParser(grammar)
    tagged_sents = POS(text)
    all_chunks = list(itertools.chain.from_iterable(nltk.chunk.tree2conlltags(chunker.parse(tagged_sent))
                                                   for tagged_sent in tagged_sents))
    # join constituent chunk words into a single chunked phrase
    candidates = [' '.join(word for word, pos, chunk in group).lower()
        for key, group in itertools.groupby(all_chunks, lambda (word,pos,chunk): chunk != 'O') if key]

    return [cand for cand in candidates
        if cand not in stop_words and not all(char in punct for char in cand)]


# In[ ]:



