#Gretabot app: twitter bot

#!/usr/bin/env python
import sys
from twython import Twython
import threading
from threading import Timer
from datetime import date
import time

def GetEnvironementTweet():
    signdate = date(2016, 4, 22)
    today = date.today()
    time_since = today-signdate
    
    tweet = "@JustinTrudeau @liberal_party\n"
    tweet = tweet + "It has been " + str(time_since.days) +" days since the Paris Agreement signature.\n"
    tweet = tweet + "People are suffering. People are dying. Entire ecosystem are collapsing.\n"
    tweet = tweet + "Your government commitment to this situation is unaccceptable. You are failing us. \n"
    tweet = tweet + "How dare you.\n"
    tweet = tweet + "#environment #greta"

    return tweet

def GetPanamaTweet():
    signdate = date(2016, 4, 3)
    today = date.today()
    time_since = today-signdate
    
    tweet = "@JustinTrudeau @liberal_party\n"
    tweet = tweet + "It has been " + str(time_since.days) +" days since the release of the Panama Paper scandal.\n"
    tweet = tweet + "Your government has done nothing to stop tax evasion.\n"
    tweet = tweet + "You are a shame to this country.\n"
    tweet = tweet + "#taxevasion #panamapapers #incomeinequality"

    return tweet

def SendTweet(type_of_tweet):
    apiKey = 'XNDKbkrWjjFUj6r6CaZImQ8Uq'
    apiSecret = '0eJC2XCEF91GklSRNmtgk6yXOsj3tK9ZLWmqYeJIgob7KRxsgA'
    accessToken = '1185532283442401280-G7EFJawo4oan9fPMJgd0RTLFXaSNqv'
    accessTokenSecret = 'Hb3vXyvEiJuBGKMLS3K3qf4hvyiy8WscdwJGAAm7U2b8K'

    api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
    if (type_of_tweet == "environnement"):
        tweetStr = GetEnvironementTweet()

    else:
        tweetStr = GetPanamaTweet()
   
    api.update_status(status=tweetStr)

def Run():
    waittime = 22* 3600 #22 hours
    while True:
        SendBothTweet()
        time.sleep(waittime)

def SendBothTweet():
    SendTweet("environnement")
    time.sleep(3600*2) #2 hours
    SendTweet("PP")

if __name__ == "__main__":
    Run()