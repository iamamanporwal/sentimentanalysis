# twitter sentiment analysis

Problem statement : Users assessed tweets related to various brands and products, providing evaluations on whether the sentiment conveyed was positive, negative, or neutral. Additionally, if the tweet conveyed any sentiment, contributors identified the specific brand or product targeted by that emotion.

Dataset Columns: tweet_text ,emotion_in_tweet_is_directed_at ,is_there_an_emotion_directed_at_a_brand_or_product.

#Steps that I followed
1. Cleaned data/ removed null values and special char.
2. Tokenization of elements in tweet texts.
3. Grouped apple/google tweets and negative/positive to boolean.
4. As it is a classification problem, I Used Scikit learn, and logistic regression.
5. Then exported it as a twittermodel.joblib
6. Then I deployed this project as a flask app

 ![Screenshot 2024-01-04 113607](https://github.com/iamamanporwal/sentimentanalysis/assets/74871831/09432866-2262-40e6-9524-1ee5b72888f2)

![Screenshot 2024-01-04 115537](https://github.com/iamamanporwal/sentimentanalysis/assets/74871831/2548d9e4-db85-4361-b094-7e87b6387df0)

