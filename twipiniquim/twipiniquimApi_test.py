#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

_author = "Eduardo S. Pereira"
_date = "26/05/2016"

import unittest
from twipiniquimApi import TwipiniquimApi
import json

class TestGetSentTweets(unittest.TestCase):

    def setUp(self):
        self.localHost = True

        self.apiId = '140304980380',
        self.secretKey ='e722d4016ed21759081bc53ff70629b29054d1144b30ba9b'

        #self.apiId = '253071546838',
        #self.secretKey ='c40b96499dbcb88ce6b59a3584adb1568f865a6f75104d0b'
        self.testMode = 1

        self.tweetsSent = TwipiniquimApi(apiID=self.apiId,
    secretKey=self.secretKey ,
    tw_consumer_key = 'HanTn77mONX8T29ZgraGuqB5E',
    tw_consumer_secret = 'zY0z2mTEqSYQGScEUOynAbP4qPlFtPSjCQhnoHdaQW6LL7h1lN',
    tw_access_token = '66704493-C6LfOHSoxVzcwL401VIU195lb5J6SQfprjN24Ixlu',
    tw_access_token_secret = 'TiYTVM2irgPVS3toLPYSWKbSFzV8hz1JvZ0yj5NXwEiil',
    localHost=self.localHost
        )

    def test_apiIDError(self):
        tw = TwipiniquimApi(apiID=None,secretKey=None,localHost=self.localHost)
        error = tw.sentFromKey('filme')
        expected = {'error': 'apiID and secret key not defined'}
        self.assertDictEqual(expected, error)

    def test_apiIDNotFounded(self):
        tw = TwipiniquimApi(apiID='000000',
                            secretKey='000000',
                            localHost=self.localHost)
        error = tw.sentFromKey('filme')
        expected = {'error': 'Api ID not founded'}
        self.assertDictEqual(expected, error)

    def test_apiIDNotFounded(self):
        tw = TwipiniquimApi(apiID=self.apiId,
                            secretKey='000000',
                            localHost=self.localHost)
        error = tw.sentFromKey('filme')
        expected = {'error': 'Not valid Secret'}
        self.assertDictEqual(expected, error)

    def test_sentFromKey(self):
        keyWord = 'filme'
        expected = {'keyWord': 'filme', 'negativo':16}
        actual = self.tweetsSent.sentFromKey(keyWord, testMode=self.testMode)
        self.assertDictContainsSubset(expected, actual)

    def test_sentFomKeyLocation(self):
        keyWord = 'filme'

        lat = -23.1774695
        lng = -45.8789595
        raio = 50

        expected = {'keyWord': 'filme', 'positivo': 78, 'lat': -23.1774695}
        actual = self.tweetsSent.sentFromKey(keyWord, lat, lng, raio,
                                             testMode=self.testMode)
        self.assertDictContainsSubset(expected, actual)

    def test_getSentTweets(self):
        result = {u'message': u'POST'}

        tweets = ['eu odeio esse filme :(', 'odeio essa bosta de film :@',
                  'eu amo esse filme meu deus sempre choro com ele']

        expected = {'eu amo esse filme meu deus sempre choro com ele': 1,
                    'eu odeio esse filme :(': -1}
        actual = self.tweetsSent.getSentTweets(tweets)['sentiments']

        self.assertDictContainsSubset(expected, actual)

if(__name__ == "__main__"):
    unittest.main()
