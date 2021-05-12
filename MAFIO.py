import tweepy

consumer_key = "FB8m0jXxtzVw6TCtfSt0CXQ7L"
consumer_secret = 'sm708ySHzDK4dQNpx1WFFowo9hvmgqXG0kubuGR7bM5QM9vAzr'

access_token = '1392282925022932992-ZBtwD9YrLlG2u7XgoquW9Ah0TFnBIm'
access_token_secret = 'U02dVI7yFztD3kopnktksDSoYVPtBV3uPVplIxdK57Nz9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
