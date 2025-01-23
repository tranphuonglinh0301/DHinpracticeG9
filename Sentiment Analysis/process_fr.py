import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import ssl
import nltk


ssl._create_default_https_context = ssl._create_unverified_context

file_path = '/Users/zselykenemeth/Desktop/dataset_fr_hpv.csv'
data = pd.read_csv(file_path)

print(data.head())


tweet_column = 'full_text'

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_tweet(text):
  
    text = text.lower()

    
    text = re.sub(r'http\S+|www\.\S+', '', text)

   
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)

    
    text = re.sub(r'[^a-zA-Zàâçéèêëîïôûùüÿñæœ\s]', '', text)

   
    text = re.sub(r'\s+', ' ', text).strip()

    print(f"After cleaning: {text}")  

   
    tokens = word_tokenize(text, language='french')

    
    stop_words = set(stopwords.words('french'))
    tokens = [word for word in tokens if word not in stop_words]

    print(f"After removing stopwords: {' '.join(tokens)}")  

   
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

   
    return ' '.join(tokens)


data[tweet_column] = data[tweet_column].astype(str).apply(preprocess_tweet)


output_path = '/Users/zselykenemeth/Desktop/processed_tweets_fr_hpv.csv'
data.to_csv(output_path, index=False)

print(f"Processed tweets saved to {output_path}")




