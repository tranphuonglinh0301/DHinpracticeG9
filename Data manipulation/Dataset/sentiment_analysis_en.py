from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import nltk


nltk.download('vader_lexicon')


sia = SentimentIntensityAnalyzer()


cleaned_tweets_path = '/Users/zselykenemeth/Desktop/processed_tweets_en.csv'
data = pd.read_csv(cleaned_tweets_path)


def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment


data['sentiment_scores'] = data['full_text'].astype(str).apply(analyze_sentiment)


data['positive'] = data['sentiment_scores'].apply(lambda x: x['pos'])
data['neutral'] = data['sentiment_scores'].apply(lambda x: x['neu'])
data['negative'] = data['sentiment_scores'].apply(lambda x: x['neg'])
data['compound'] = data['sentiment_scores'].apply(lambda x: x['compound'])


def label_sentiment(compound_score):
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

data['sentiment_label'] = data['compound'].apply(label_sentiment)

sentiment_output_path = '/Users/zselykenemeth/Desktop/sentiment_analysis_en.csv'
data.to_csv(sentiment_output_path, index=False)

print(f"Sentiment analysis results saved to {sentiment_output_path}")
