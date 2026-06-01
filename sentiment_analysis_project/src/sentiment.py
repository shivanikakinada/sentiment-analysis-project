from textblob import TextBlob

def analyze_sentiment(df):

    df["sentiment_score"] = df["title"].apply(
        lambda x: TextBlob(str(x)).sentiment.polarity
    )

    def classify(score):
        if score > 0:
            return "Positive"
        elif score < 0:
            return "Negative"
        else:
            return "Neutral"

    df["sentiment"] = df["sentiment_score"].apply(classify)

    return df