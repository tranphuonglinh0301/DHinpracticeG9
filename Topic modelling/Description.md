# Topic modeling
During this step of the project, we did the topic modelling separately for tweets by languages using LDA. In LDA, the text is considered a bag of words, and the topics are identified based on the frequency of words. This is also the most common topic modelling method.

The content of the tweets were tokenized. Only tokens that are alphabetical characters than have more than 2 characters are kept (so random character and emoticons are removed). Stopwords are removed. All tokens are lemmatized. This allow better results in topic modelling and decrease the confusion. Based on the available tokens, the tweets are classified into 10 different topics (each language). 

The results of the topic modelling is represented as a set of words, based on the frequency of appearance in each topic. Further analysis is needed to identify the topics. 

In the documentation file on Google Docs, some plots regarding number of characters, number of words and common tokens in each language dataset are included. 

# Changes (22.01.2025)
Using the filtered datasets, we performed the topic modelling (one more time). For this time, after finding out the top most common words in each dataset, the tokens that directly mentioned HPV (“hpv”, “vaccine”, “vaccin”, “gardasil”, “papillomavirus”...) were removed from the bag of words. We remove this in order to see the other less common tokens more clearly, so we will be able to categorize them into meaningful topics. The files contain "_hpv" are the files related to this change. 
