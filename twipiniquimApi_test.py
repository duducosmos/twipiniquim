#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

_author = "Eduardo S. Pereira"
_date = "26/05/2016"

import unittest
from twipiniquimApi import TwipiniquimApi
import json

class TestGetSentTweets(unittest.TestCase):

    def setUp(self):

        self.tweetsSent = TwipiniquimApi(apiID='000000',
                                         secretKey='000000')

    def test_apiIDError(self):
        tw = TwipiniquimApi()
        error = tw.sentFromKey('filme')
        expected = {'error': 'apiID and secret key not defined'}
        self.assertDictEqual(expected, error)

    def test_sentFromKey(self):
        keyWord = 'filme'
        expected = {'keyWord': 'filme', 'positivo': 10}
        actual = self.tweetsSent.sentFromKey(keyWord)
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
