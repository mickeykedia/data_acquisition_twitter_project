import tweepy
import re


ckey = 'pnE9kjOJOhAO3WTUMJ4rLRe1W'
csecret = 'e7pEcYtCBkr3jjalFjlVNakcjZkn4sWGD5pKLDASA3zAnLnRNz'
atoken = '3665746454-sKiPPDpeGc05UHrhR3IZGtgH9fsU0jc3uIM35hP'
asecret = '4wMtT0MVGh9O7GGHQFpmbfSkAS9j3BA3G9oo8K528bC9j'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

user1 = api.get_user("BillGates")

tweets = api.user_timeline(screen_name="BillGates", include_rts=True, count=200)

# tweets_for_csv = [['BillGates',tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]



for tweet in tweets:
    print ("ID:", tweet.id)
    print("ID_str:", tweet.id_str)
    print ("User ID:", tweet.user.id)
    print ("Text:", re.sub(r'[^\x00-\x7F]+','', str(tweet.text.encode("utf-8"))))
    print ("Created:", tweet.created_at)
    # print ("Geo:", tweet.geo)
    # print ("Contributors:", tweet.contributors)
    print ("Coordinates:", tweet.coordinates)
    print ("Favorite Count:", tweet.favorite_count)
    print ("Place:", tweet.place)
    # whether this Tweet has been retweeted by the authenticating user.
    # print ("Retweeted:", tweet.retweeted)
    # print ("entities:", tweet.entities)
    # print tweet.entities
    if tweet.entities['hashtags'] <> []:
        print("has_hashtag", 1)
    else:
      print("has_hashtag", 0)

    if tweet.entities['urls'] <> []:
        print("has_url", 1)
    else:
      print("has_url", 0)

    if 'media' in tweet.entities:
        print("has_media", 1)
        if tweet.entities['media'][0]['type'] == 'photo':
            print("has_photo", 1)
            print("has_video", 0)
        else:
            print("has_video", 1)
            print("has_photo", 0)
    else:
      print("has_media", 0)

    print ("Retweet count:", tweet.retweet_count)
    print ("Source:", tweet.source)

exit()

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

