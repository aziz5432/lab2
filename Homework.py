#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
text = "iam Abdulaziz Khaled Aljammz "
sentence = nltk.sent_tokenize(text)
for sent in sentence:
	 print(nltk.pos_tag(nltk.word_tokenize(sent)))


# In[ ]:




