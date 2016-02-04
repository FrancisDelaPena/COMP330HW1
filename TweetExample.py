#HW1 for COMP 330

class NotTwitter(): #Named such because this is not official twitter

    def findmention(tweet): #checks for mentioning account
        if tweet.find("@") == -1:
            return False
        else:
            return True
        
    def findhashtag(tweet): #checks for hashtags
        if tweet.find("#") == -1:
            return False
        else:
            return True

    def findurl(tweet): #checks for url
        if tweet.find("http://") == -1:
            return False
        else:
            return True
