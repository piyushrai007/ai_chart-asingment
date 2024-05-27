# Sentiment Analysis Summary Report

## Approach

1. **Load the Dataset**: The dataset was loaded from a CSV file using pandas.
2. **Clean the Data**: Any null values were removed. Since there were no unnecessary columns in this dataset, no columns were dropped.
3. **Text Preprocessing**: The text in the reviews was converted to lowercase, and punctuation was removed.
4. **Sentiment Analysis**: The sentiment of each review was analyzed using TextBlob, categorizing them as Positive, Negative, or Neutral.
5. **Summary Report**: The distribution of sentiments was displayed using a bar chart.

## Challenges Faced

- **Text Preprocessing**: Ensuring the text was uniformly preprocessed required careful handling of string operations.

## Assumptions Made

- **Review Text Column**: It was assumed that the column containing the review text is named `review`.
- **Sentiment Categorization**: Sentiment polarity greater than 0 was considered Positive, less than 0 as Negative, and equal to 0 as Neutral.

## Results

The distribution of sentiments was as follows:
