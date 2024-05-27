import pandas as pd
import string
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_excel('user_review.xls')

# Drop rows with any null values
df.dropna(inplace=True)

# Drop unnecessary columns (if any, adjust column names based on your actual dataset)
# In this case, we do not have any unnecessary columns

# Text preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Apply preprocessing
df['review'] = df['review'].apply(preprocess_text)

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['sentiment'] = df['review'].apply(analyze_sentiment)

# Generate summary report
sentiment_counts = df['sentiment'].value_counts()
print(sentiment_counts)

# Plot sentiment distribution
sentiment_counts.plot(kind='bar')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.title('Sentiment Distribution')
plt.savefig('sentiment_distribution.png')
plt.show()
