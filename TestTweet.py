import unittest
from TweetExample import *

#HW1 for COMP 330

extweet = "When @twotribes go to war, a #point is all you can score.  See http://reddit.com"
    #Reference to example in prompt!  I know 80s music too.

class TestTweet(unittest.TestCase):

    def setUp(self):
        pass

    def test_none(self):
        self.assertIsNotNone(NotTwitter.findmention(extweet))

    def test_mention(self):
        self.assertTrue(NotTwitter.findmention(extweet))

    def test_none2(self):
        self.assertIsNotNone(NotTwitter.findhashtag(extweet))
    
    def test_hashtag(self):
        self.assertTrue(NotTwitter.findhashtag(extweet))

    def test_none3(self):
        self.assertIsNotNone(NotTwitter.findurl(extweet))

    def test_findurl(self):
        self.assertTrue(NotTwitter.findurl(extweet))
        
if __name__ == '__main__':
    unittest.main() #All tests should pass in this case
