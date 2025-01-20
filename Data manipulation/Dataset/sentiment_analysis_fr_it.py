import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from langdetect import detect

nlp_fr = spacy.load("fr_core_news_sm")  
nlp_it = spacy.load("it_core_news_sm") 

analyzer = SentimentIntensityAnalyzer()

file_path = '/Users/zselykenemeth/Desktop/processed_tweets_it.csv'
data = pd.read_csv(file_path)


tweet_column = 'full_text'


def analyze_sentiment(text, language):
    try:
        
        if language == 'fr':
            nlp = nlp_fr
        elif language == 'it':
            nlp = nlp_it
        else:
            return {
                'sentiment_label': 'Unsupported',
                'polarity': None
            }

        
        doc = nlp(text)
        processed_text = " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

        
        sentiment = analyzer.polarity_scores(processed_text)
        compound = sentiment['compound']
        if compound >= 0.05:
            label = 'Positive'
        elif compound <= -0.05:
            label = 'Negative'
        else:
            label = 'Neutral'

        return {
            'sentiment_label': label,
            'polarity': compound
        }
    except Exception as e:
        return {
            'sentiment_label': 'Error',
            'polarity': None,
            'error': str(e)
        }


def process_tweet(row):
    try:
       
        language = detect(row[tweet_column])
        row['language'] = language

        
        result = analyze_sentiment(row[tweet_column], language)
        row['sentiment_label'] = result['sentiment_label']
        row['polarity'] = result['polarity']
        row['error'] = result.get('error', None)
        return row
    except Exception as e:
        row['language'] = 'unknown'
        row['sentiment_label'] = 'Error'
        row['polarity'] = None
        row['error'] = str(e)
        return row


data = data.apply(process_tweet, axis=1)


output_path = '/Users/zselykenemeth/Desktop/sentiment_analysis_it.csv'
data.to_csv(output_path, index=False)

print(f"Sentiment analysis results saved to {output_path}")





