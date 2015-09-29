

# No. of followers, No. of followed, No. of tweets
# from rauth import OAuth1Service
# twitter = OAuth1Service(
#     name='twitter',
#     consumer_key='pnE9kjOJOhAO3WTUMJ4rLRe1W',
#     consumer_secret='e7pEcYtCBkr3jjalFjlVNakcjZkn4sWGD5pKLDASA3zAnLnRNz',
#     request_token_url='https://api.twitter.com/oauth/request_token',
#     access_token_url='https://api.twitter.com/oauth/access_token',
#     authorize_url='https://api.twitter.com/oauth/authorize',
#     base_url='https://api.twitter.com/1.1/')
#
#
# request_token, request_token_secret = twitter.get_request_token()
#
# authorize_url = twitter.get_authorize_url(request_token)
# pin = 7635292
# session = twitter.get_auth_session(request_token,
#                                    request_token_secret,
#                                    method='POST',
#                                    data={'oauth_verifier': pin})
#
# params = {'screen_name': 'RevRunWisdom',  # User to pull Tweets from
#           'include_rts': 1,         # Include retweets
#           'count': 100}              # 10 tweets
#
# r = session.get('statuses/user_timeline.json', params=params)
# for i, tweet in enumerate(r.json(), 1):
#     handle = tweet['user']['screen_name'].encode('utf-8')
#     text = tweet['text'].encode('utf-8')
#     print '{0}. @{1} - {2}'.format(i, handle, text)


import tweepy

ckey = 'pnE9kjOJOhAO3WTUMJ4rLRe1W'
csecret = 'e7pEcYtCBkr3jjalFjlVNakcjZkn4sWGD5pKLDASA3zAnLnRNz'
atoken = '3665746454-sKiPPDpeGc05UHrhR3IZGtgH9fsU0jc3uIM35hP'
asecret = '4wMtT0MVGh9O7GGHQFpmbfSkAS9j3BA3G9oo8K528bC9j'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

user1 = api.get_user("BillGates")

tweets = api.user_timeline(screen_name="BillGates", include_rts=True, count=300)

tweets_for_csv = [['BillGates',tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
for tweet in tweets:
    print len(tweets)
    print tweet.id,  tweet.text.encode("utf-8"), tweet.retweet_count


for tweet in tweets:
    print ("ID:", tweet.id)
    print ("User ID:", tweet.user.id)
    print ("Text:", tweet.text)
    print ("Created:", tweet.created_at)
    print ("Geo:", tweet.geo)
    print ("Contributors:", tweet.contributors)
    print ("Coordinates:", tweet.coordinates)
    print ("Favorited:", tweet.favorited)
    print ("In reply to screen name:", tweet.in_reply_to_screen_name)
    print ("In reply to status ID:", tweet.in_reply_to_status_id)
    print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
    print ("In reply to user ID:", tweet.in_reply_to_user_id)
    print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
    print ("Place:", tweet.place)
    print ("Retweeted:", tweet.retweeted)
    print ("Retweet count:", tweet.retweet_count)
    print ("Source:", tweet.source)
    print ("Truncated:", tweet.truncated)


def profile_info(user):
    user = api.get_user(user)
    print user
    print "User info"
    print user.id_str
    print user.default_profile_image
    print user.profile_use_background_image
    print user.favourites_count
    print user.created_at
    print user.followers_count
    print user.friends_count
    print user.screen_name
    print user.statuses_count
    # print user.location
    # print user.description


def userinfo(user):
    for friend in user.friends():                                   # Following
        print friend
        print "Screen-name", friend.screen_name
        # print friend.profile_use_background_image
        print friend.id_str
        print friend.statuses_count
        print friend.description
        print friend.friends_count
        print friend.location
        print friend.followers_count

    print("\n")
    for follower in tweepy.Cursor(api.followers).items():           # Your followers
        print follower.screen_name
        # print follower.follow(), follower.screen_name             # Follow your followers



def search(results):
# Tweets
    for result in results:
        # print result.text
        print result.id
        print result.created_at
        print result.author.id
        print result.retweet_count
        print result
        print result.author



search(results)



list_users = ['BillGates', 'narendramodi', 'rihanna', 'elonmusk', 'narendramodi', 'realDonaldTrump', 'ActuallyNPH',
              'EmWatson', 'SrBachchan', 'DalaiLama', 'MegWhitman', 'marissamayer', 'tim_cook', 'evanspiegel',
              'drewhouston',
              'sundarpichai']
# print "Screen name\tFollowers count\tFollowed Count\tNo. of tweets\tLocation\tDescription"
for name in list_users:
    profile_info(name)
    #print("\n")

