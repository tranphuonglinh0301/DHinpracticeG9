import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from langdetect import detect

vader_analyzer = SentimentIntensityAnalyzer()


data = pd.read_csv('/Users/zselykenemeth/Desktop/cleaned_dataset.csv')

data['full_text'] = data['full_text'].astype(str)

#Detecting language
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'


def analyze_sentiment(text, lang):
    if lang == 'en':  # Use VADER for English
        scores = vader_analyzer.polarity_scores(text)
        return scores['compound']
    else:  
        blob = TextBlob(text)
        return blob.sentiment.polarity

data['language'] = data['full_text'].apply(detect_language)


data['sentiment_score'] = data.apply(lambda x: analyze_sentiment(x['full_text'], x['language']), axis=1)

def categorize_sentiment(score):
    if score > 0.05:
        return 'positive'
    elif score < -0.05:
        return 'negative'
    else:
        return 'neutral'
