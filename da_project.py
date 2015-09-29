__author__ = 'mrunmayee'

# No. of followers, No. of followed, No. of tweets

import tweepy
import psycopg2

# ckey = ''
# csecret = ''
# atoken = ''
# asecret = ''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
results = api.search(q = "supermoon", count = 2)
rows = []


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

    # For db
    dict1 = {}
    dict1['id'] = user.id_str
    dict1['has_profile_image'] = user.default_profile_image
    dict1['has_profile_image_background'] = user.profile_use_background_image
    dict1['favourites_count'] = user.favourites_count
    dict1['created_at'] = user.created_at
    dict1['followers_count'] = user.followers_count
    dict1['following_count'] = user.friends_count
    dict1['screen_name'] = user.screen_name
    dict1['statuses_count'] = user.statuses_count
    rows.append(dict1)


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


# Tweeet details
search(results)

# User details
list_users = ['BillGates', 'rihanna', 'elonmusk', 'narendramodi', 'realDonaldTrump', 'ActuallyNPH',
              'EmWatson', 'SrBachchan', 'DalaiLama', 'MegWhitman', 'marissamayer', 'tim_cook', 'evanspiegel',
              'drewhouston', 'sundarpichai']

for name in list_users:
    profile_info(name)


# Store data in the db. Change the connection string according to your db name.
# given conn OR conn = psycopg2.connect(database = "da", username = "", password = "")
print "Database Connection"
conn = psycopg2.connect(database="da")
cur = conn.cursor()

cur.executemany("""INSERT INTO twitter_data.twitter_users(id, has_profile_image, has_profile_image_background,
favourites_count, created_at, followers_count, following_count, screen_name, statuses_count) VALUES (%(id)s,
%(has_profile_image)s, %(has_profile_image_background)s, %(favourites_count)s, %(created_at)s,
%(followers_count)s, %(following_count)s, %(screen_name)s, %(statuses_count)s)""", rows)

conn.commit()
print "Success"
