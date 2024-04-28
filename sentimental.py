from textblob import TextBlob
import pandas as pd

# Example tweet data
tweets = ["I love this movie!", "This movie is terrible.", "The weather today is great."]

# Perform sentiment analysis on each tweet
sentiments = []
for tweet in tweets:
    analysis = TextBlob(tweet)
    # Assign sentiment polarity
    if analysis.sentiment.polarity > 0:
        sentiment = 'positive'
    elif analysis.sentiment.polarity == 0:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    sentiments.append(sentiment)

# Create a DataFrame to store the results
df = pd.DataFrame({'Tweet': tweets, 'Sentiment': sentiments})

# Print the DataFrame
print(df)
