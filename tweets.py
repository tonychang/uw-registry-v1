import tweepy

def get_tweets():
    return tweepy.api.search('#uwweb',rpp=10)

if __name__ == "__main__":
    for tweet in get_tweets():
        print tweet.from_user, tweet.text


