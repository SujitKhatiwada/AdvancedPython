#!/usr/bin/env python
# coding: utf-8

# # Project 2c

# In[1]:


#Importing required libraries

import re
import contractions
import numpy as np

txt = "This movie made it into one of my top 10 most awful movies. Horrible. There wasn't a continuous minute where there wasn't a fight with one monster or another. There was no chance for any character development, they were too busy running from one sword fight to another. I had no emotional attachment ( except to the big bad machine ## that wanted to destroy them)"


# Cleaning the data

# In[2]:


class PreProcess():
    
    def __init__(self,text):
        self.text = text
        self.tokenized = []
        self.stop_word = []
        self.tags = []
        self.expanded_txt = self.remcontra(self.text)
        self.spec = self.remSpecChar(self.expanded_txt)

    def remcontra(self,text:str):

      '''
          This method expands the contractions in the given text
              Input arguments : text (Here the input is the text and this function expands the contractions inside the text 
              ---------------         For Ex: doesn't changes to does not)
              Returns: We get the expanded text
              --------
              '''
      words = []    
      for word in text.split():
        words.append(contractions.fix(word))   
        expanded_text = ' '.join(words)
      return expanded_text
      

    def remSpecChar(self, text:str):
      '''This method removes the special characters along with extra spaces
          Input arguments: text ( In this function all the special characters will be removed and extra spaces will be cleared )
          ---------------     
          Returns: The final text will have cleared special characters.'''

      specChar = re.sub('[^A-Za-z0-9@]+',' ',text)
      return specChar 
      

    def regexp(self):
      ''' 
          This method simplifies the digits and emails using regular expressions.
                Input arguments: text (In this function the digits and email will be cleared by using certain patterns)
                ---------------     
                Returns:  We get simplified text.
          '''
      self.rg=re.sub('[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}','email',self.spec)
      self.rg=re.sub('\d+','',self.rg)
      return self.rg

    def token(self,tokenize_on):

      ''' In this function the whole text will be divided into tokens.
                  By tokenization we can transform indivisible assets into tokens'''

      self.tokenized = nltk.word_tokenize(self.rg)
      return self.tokenized

    def remove_stopwords(self):
      ''' 
        Stopwords are a set of commonly used words such as is, the, are etc.. 
        Input
        -----
        text file as string
        
        Returns
        ------
        list of words without stopwords
      '''
      stop_words = set(stopwords.words('english'))  
      for w in self.tokenized:
        if w not in stop_words:
          self.stop_word.append(w)
      return self.stop_word
      
    def stemmingOrLemmatization(self, method):
      """
      stemmingOrLemmatization(argument) function decides which functions should
      be running based on the input
      """
      if method == 'stem':
        self.out = self.stemming()
      else:
        self.out = self.lemmatization()
      return self.out

    # Stemming


    def stemming(self):
      """
      Stemming() removes suffix from a word and reduce it to 
      its root word.
      """
      stm = nltk.porter.PorterStemmer()
      stword = [stm.stem(word) for word in self.stop_word]
      return stword
    
    # Lemmetization
    def lemmatization(self):
      """
      lemmatization() functions takes input from stemming and reduces it to the
      right word
      """
      lem = WordNetLemmatizer()
      lemout = [lem.lemmatize(word) for word in self.stop_word]
      return lemout
        
        
    def ngram(self,tx):
      ''' 
      In this function it returns a sequence of N items from a given sample of text.
      Here an item can be a character,words,sentence and N can be any integer
              
      '''
      NGRAMS=ngrams(sequence=nltk.word_tokenize(tx), n=5)
      for grams in NGRAMS:
          print(grams)

      
 


# Cleaned Data

# In[3]:


process = PreProcess(txt)
process.regexp()


# In[4]:


#Importing sklearn libraries

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import _stop_words
text = [process.regexp()]
StopWords = list(_stop_words.ENGLISH_STOP_WORDS)
vectorizer = CountVectorizer(stop_words=StopWords)
vectorizer.fit(text)
print(len(vectorizer.vocabulary_))


# In[5]:


#Printing vocabulary

print(vectorizer.vocabulary_)


# In[6]:


#Vectors to Array

vectors = vectorizer.transform(text)
print(vectors.toarray())


# TF-IDF

# In[7]:


# importing TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
text


# In[8]:


tfidf = TfidfVectorizer()
result = tfidf.fit_transform(text)


# Giving Indexes and TFIDF Values

# In[9]:


# get indexing
print('\nWord indexes:')
print(tfidf.vocabulary_)
  
print('\ntf-idf values in matrix form:')
print(result.toarray())


# In[ ]:




