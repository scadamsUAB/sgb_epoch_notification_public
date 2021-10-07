
import json
import time
import tweet_sender
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import discord_sender
import tweepy
from datetime import datetime






f= open("configs.json","r")
configs_json = json.load(f)
f.close()



token = configs_json["Discord_configs"]["discord_token"]
channels=configs_json["Discord_configs"]["channels"]
twitter_consumer_key = configs_json["twitter_configs"]["consumer_key"]
twitter_consumer_secret = configs_json["twitter_configs"]["consumer_secret"]
twitter_key= configs_json["twitter_configs"]["key"]
twitter_secret = configs_json["twitter_configs"]["secret"]




def get_epochblock(driver, epoch_to_check):
    while True:
        time.sleep(5)
        elements = driver.find_elements_by_css_selector("input[class='form-control form-control-sm address-input-sm mt-2']")
        elements[0].clear()
        elements[0].send_keys(epoch_to_check)

        
        elements = driver.find_elements_by_css_selector("input[class='button btn-line button-xs py-0 mt-2 write-contract-btn']")
        elements[0].click() 
        
        time.sleep(2)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        elements = driver.find_elements_by_css_selector("div[style='padding-left: 20px']")
        if "error" in elements[0].text:
            log_message = "As of " + str(dt_string) +"  the current epoch is : " + str(int(epoch_to_check)-1)
            print(log_message)
            f=open("log.txt","w")
            f.write(log_message)
            f.close()
        
        else:
            epoch_to_check = epoch_to_check + 1
        #    print("BLOCK " + str(elements[0].text.split(":")[1]))
            message="The #Songbird reward epoch has been locked as of Block Number: "+str(elements[0].text.split(":")[1]) +" Retweet to spread the word"
            print(message)
            #tweet_sender.send_tweet(twitter_consumer_key,twitter_consumer_secret, twitter_key,twitter_secret,message)
            message="The Songbird reward epoch has been locked as of Block Number: "+str(elements[0].text.split(":")[1]) +" Spread the word"
           
            #discord_sender.multi_send(token,message,channels)
         
        

print("starting")
should_continue = True

while should_continue:
    try:
        starting_epoch = input("Please enter the number for the epoch you wish to start looking at ")
        starting_epoch_int = int(starting_epoch)
        should_continue = False
    except:
        print("invalid input")
options = Options()
options.headless = True
driver = webdriver.Firefox( options=options)
print("driver Setup")
driver.get("https://songbird-explorer.flare.network/address/0xbfA12e4E1411B62EdA8B035d71735667422A6A9e/read-contract")
get_epochblock(driver,starting_epoch_int)
driver.quit()
