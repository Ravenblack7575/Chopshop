import pandas as pd
import numpy as np

import regex as re


#tokenize text

def tokenize(text):
    return re.findall(r'[\w+]*\p{L}[\w-]*', text)



#remove stopwords

import nltk

stopwords = set(nltk.corpus.stopwords.words('english'))

def remove_stop(tokens):
    return [t for t in tokens if t.lower() not in stopwords]


#additional words that you might want to include or exclude from the default stopwords dictionary.

include_stopwords = {}
exclude_stopwords = {}

stopwords |= include_stopwords
stopwords -= exclude_stopwords


#preparing text data with a pipeline

pipeline = [str.lower, tokenize, remove_stop]

def prepare(text, pipeline):
    tokens = text
    for transform in pipeline:
        tokens = transform(tokens)
    return tokens


