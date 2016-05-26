#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

_author = "Eduardo S. Pereira"
_date = "26/05/2016"

import requests


class TwipiniquimApi:
    def __init__(self, apiID=None, secretKey=None):
        self.apiID = apiID
        self.secretKey = secretKey


    def getSentTweets(self, tweets):
        """
        Rerturn a json with the sentiments associates with each tweet.
        key:
            tweets: list of tweets.
        """
        data = {'apiID': self.apiID,
                'secretKey': self.secretKey,
                'tweets': tweets}

        r = requests.post('http://localhost:8000/twipiniquim/default/api/sent.json',
                          data=data)
        return r.json()

    def sentFromKey(self, keyWord, lat=None, lng=None, raio=None, testMode=0):
        """
        Return a json with the number of positive and negative tweets
        associated with a givem keyWord.
        key:
            keyWord: key word.
        """

        if(lat is not None and lng is not None and raio is not None):
            data = {'apiID': self.apiID,
                    'secretKey': self.secretKey,
                    'keyWord': keyWord,
                    'lat': lat,
                    'lng': lng,
                    'raio': raio,
                    'testMode': testMode
                    }
        else:
            data = {'apiID': self.apiID,
                    'secretKey': self.secretKey,
                    'keyWord': keyWord,
                    'testMode': testMode
                    }

        r = requests.post('http://localhost:8000/twipiniquim/default/api/sent.json',
                          data=data)
        return r.json()
