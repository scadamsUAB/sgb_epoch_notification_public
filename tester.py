import discord_sender
import tweet_sender
import json




f= open("configs.json","r")
configs_json = json.load(f)
f.close()



token = configs_json["Discord_configs"]["discord_token"]
channels=configs_json["Discord_configs"]["channels"]
twitter_consumer_key = configs_json["twitter_configs"]["consumer_key"]
twitter_consumer_secret = configs_json["twitter_configs"]["consumer_secret"]
twitter_key= configs_json["twitter_configs"]["key"]
twitter_secret = configs_json["twitter_configs"]["secret"]


#tweet_sender.send_tweet(twitter_consumer_key,twitter_consumer_secret, twitter_key,twitter_secret,message)

