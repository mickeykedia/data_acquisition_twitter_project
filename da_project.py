__author__ = 'mrunmayee'

# No. of followers, No. of followed, No. of tweets

import tweepy

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

results = api.search(q = "supermoon", count = 2)

# for tweet in public_tweets:
#     print tweet.text


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

