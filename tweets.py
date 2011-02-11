import tweepy

def get_tweets():
    try:
        return tweepy.api.search('#uwweb',rpp=10,headers={'User-Agent': 'tweepy'})
    except tweepy.TweepError, e:
        return []

if __name__ == "__main__":
    for tweet in get_tweets():
        print tweet.from_user, tweet.text


