# autoreplytwitter
This is a simple python codes to reply twitter user automatically.
On this script, I use scraping to monitor the twitter pages, to bypass the low usage limit the twitter API has.
Tweepy only used for replying the new tweet.

Enter your usual tweepy requirement on auto.py,
```python

cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

```
Enter twitter username you like to monitor on **twitterUsername**

Enter twitter text reply you want on **tweetText**

and to run it simply

> python auto.py