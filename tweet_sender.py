import tweepy

def send_tweet(consumer_key, consumer_secret, key, secret,message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    print("IN SSEND TWEET")
    print(consumer_secret)
    print(consumer_key)
    print(key)
    print(secret)
    print(message)
    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status(message)
        