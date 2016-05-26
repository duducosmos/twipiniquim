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

    def sentFromKey(self, keyWord):
        """
        Return a json with the number of positive and negative tweets
        associated with a givem keyWord.
        key:
            keyWord: key word.
        """

        data = {'apiID': self.apiID,
                'secretKey': self.secretKey,
                'keyWord': keyWord}

        r = requests.post('http://localhost:8000/twipiniquim/default/api/sent.json',
                          data=data)
        return r.json()
