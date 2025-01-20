from transformers import pipeline
import pandas as pd


sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")


cleaned_tweets_path = '/Users/zselykenemeth/Desktop/processed_tweets_it.csv'
data = pd.read_csv(cleaned_tweets_path)


def analyze_sentiment_vader_style(text):
    try:
        result = sentiment_analyzer(text)[0]
        label = result['label']  
        score = result['score']  

        
        stars = int(label[0])  
        compound = (stars - 3) / 2  

       
        if compound > 0:
            positive = compound
            neutral = 1 - compound
            negative = 0
        elif compound < 0:
            positive = 0
            neutral = 1 + compound
            negative = -compound
        else:
            positive = 0
            neutral = 1
            negative = 0

        return {
            'positive': positive,
            'neutral': neutral,
            'negative': negative,
            'compound': compound,
            'sentiment_label': 'Positive' if compound > 0.05 else 'Negative' if compound < -0.05 else 'Neutral'
        }
    except Exception as e:
        print(f"Error analyzing text: {text}\n{e}")
        return {
            'positive': None,
            'neutral': None,
            'negative': None,
            'compound': None,
            'sentiment_label': None
        }


data['sentiment_scores'] = data['full_text'].astype(str).apply(analyze_sentiment_vader_style)


data['positive'] = data['sentiment_scores'].apply(lambda x: x['positive'])
data['neutral'] = data['sentiment_scores'].apply(lambda x: x['neutral'])
data['negative'] = data['sentiment_scores'].apply(lambda x: x['negative'])
data['compound'] = data['sentiment_scores'].apply(lambda x: x['compound'])
data['sentiment_label'] = data['sentiment_scores'].apply(lambda x: x['sentiment_label'])


sentiment_output_path = '/Users/zselykenemeth/Desktop/sentiment_analysis_it.csv'
data.to_csv(sentiment_output_path, index=False)

print(f"Sentiment analysis results saved to {sentiment_output_path}")






