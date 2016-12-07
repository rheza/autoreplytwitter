import tweepy
import random
import time
import requests
import datetime
from lxml import html
from lxml.cssselect import CSSSelector

# Enter twitter username you want to monitor
twitterUsername = ""
waitSeconds = 30
sourceLink = "https://twitter.com/" + twitterUsername

totalReply = 0
currentTweetId = ""
latestTweetId = ""

# Enter your multiple text here
tweetText = [" "," "]

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted 
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

  randomNumber = random.randrange(1,1000)
  randomTweet = random.randrange(1,len(tweetText))
  api = get_api(cfg)
  tweet = "@" + twitterUsername + tweetText[randomTweet] + " " + str(randomNumber)
  status = api.update_status(status=tweet,in_reply_to_status_id=latestTweetId)
  print("Posted Tweet #"+str(randomNumber))




def checkTweet():
  #check latest tweet and save
  global currentTweetId
  global latestTweetId
  global totalReply
  #print("check")
  #print("currentTweetId = " + str(currentTweetId))
  #print("latestTweetId = " + str(latestTweetId))
  try:
    print(datetime.datetime.now())
    print("Total Tweet Reply = ", str(totalReply))
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    }
    page = requests.get(sourceLink, headers=headers)
    tree = html.fromstring(page.content)
    #print(tree)
    isTherePinnedTweet = tree.cssselect("div.pinned")
    pinnedTweetNo  = len(isTherePinnedTweet)
    #print(len(isTherePinnedTweet))
    if pinnedTweetNo > 0:
        latestTweetId = tree.cssselect("li.js-stream-item")[1].attrib["data-item-id"]
        #print("Has pinned tweet")
    else:   
        latestTweetId = tree.cssselect("li.js-stream-item")[0].attrib["data-item-id"]
        #print("Dont have pinned tweet")
    #print(latestTweetId)
  except:
    pass
  if currentTweetId == "":
      if latestTweetId != currentTweetId:
        currentTweetId = latestTweetId
        print("init currentTweetId")
  elif currentTweetId != latestTweetId:
        print("reply tweet to  "+ twitterUsername +" ")
        totalReply = 1 + totalReply
        main()
        currentTweetId = latestTweetId
  elif currentTweetId == latestTweetId:
        print("nothing new, pass")
  else:
        print("error, pass")
    

if __name__ == "__main__":
  while True:
    checkTweet()
    time.sleep(waitSeconds)

  