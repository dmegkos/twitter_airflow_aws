# Import libraries
import tweepy  # For interacting with the Twitter API
import pandas as pd  # For data manipulation and analysis
import s3fs  # For interacting with AWS S3

def run_twittter_etl():
    # Define your Twitter Bearer Token
    bearer_token = "Your_Token_Here"

    # Create a client to interact with the Twitter API using Tweepy
    client = tweepy.Client(bearer_token=bearer_token)

    # Define the query to search recent tweets
    # The query is looking for tweets with the hashtag #elonmusk, excluding retweets and in English
    query = '#elonmusk -is:retweet lang:en'
    
    # Get the tweets from the API
    tweets = client.search_recent_tweets(query=query, tweet_fields=['author_id', 'created_at'], max_results=100)

    # Initialize an empty list to store the tweets
    tweet_list = []

    # Loop through the tweets and store the relevant information
    for tweet in tweets.data:
        refined_tweet = {'user': tweet.author_id,
                        'text': tweet.text,
                        'created_at': tweet.created_at}
        tweet_list.append(refined_tweet)

    # Convert the list of tweets into a pandas DataFrame
    df = pd.DataFrame(tweet_list)

    # Write the DataFrame to a CSV file in the specified S3 bucket
    df.to_csv("s3://dm-airflow-project/elonmust_twitter_data.csv")
