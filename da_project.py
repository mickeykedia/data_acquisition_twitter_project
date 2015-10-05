__author__ = 'mrunmayee'

# For the users pull tweets as many as possible, should we include retweets?

# Remove
# @rathsandeep, @arnavsaxena, @niyantay

import tweepy
import psycopg2

# ckey = ''
# csecret = ''
# atoken = ''
# asecret = ''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)
rows = []
rows_tweet = []

def profile_info(user):
    user = api.get_user(user)

    # print user
    # print "User info"
    # print user.id_str
    # print user.default_profile_image
    # print user.profile_use_background_image
    # print user.favourites_count
    # print user.created_at
    # print user.followers_count
    # print user.friends_count
    # print user.screen_name
    # print user.statuses_count

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

# db table: Location is tweet location or user location?
def tweet_info(tweets):
    for tweet in tweets:

        # print(username, tweet.coordinates)
        # print("ID_str:", tweet.id_str)
        # print "User ID:", tweet.user.id
        # print "Created:", tweet.created_at
        # print "Retweet count:", tweet.retweet_count
        if tweet.entities['hashtags'] <> []:
            # print("has_hashtag", 1)
            has_hashtag = True
        else:
            # print("has_hashtag", 0)
            has_hashtag = False

        if tweet.entities['urls'] <> []:
            #print("has_url", 1)
            has_url = True
        else:
            #print("has_url", 0)
            has_url = False

        if 'media' in tweet.entities:
            #print("has_media", 1)
            if tweet.entities['media'][0]['type'] == 'photo':
                #print("has_photo", 1)
                #print("has_video", 0)
                has_photo = True
                has_video = False
            else:
                #print("has_video", 1)
                #print("has_photo", 0)
                has_photo = False
                has_video = True
        else:
            #print("has_media", 0)
            has_photo = False
            has_video = False


        dict2 = {}
        dict2['id'] = tweet.id_str
        dict2['user_id'] = tweet.user.id
        dict2['created_at'] = tweet.created_at
        dict2['retweet_count'] = tweet.retweet_count
        dict2['has_hashtag'] = has_hashtag
        dict2['has_url'] = has_url
        dict2['has_photo'] = has_photo
        dict2['has_video'] = has_video
        rows_tweet.append(dict2)


        # print ("Geo:", tweet.geo)
        # print ("Contributors:", tweet.contributors)
        # print ("Coordinates:", tweet.coordinates)
        # print ("Favorited:", tweet.favorited)
        # print ("In reply to screen name:", tweet.in_reply_to_screen_name)
        # print ("In reply to status ID:", tweet.in_reply_to_status_id)
        # print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
        # print ("In reply to user ID:", tweet.in_reply_to_user_id)
        # print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
        # print ("Retweeted:", tweet.retweeted)
        # print ("Source:", tweet.source)
        # print ("Truncated:", tweet.truncated)
        # print ("Text:", re.sub(r'[^\x00-\x7F]+', '', str(tweet.text.encode("utf-8"))))



# Tweets from hashtags
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


# Users
list_users = ['Snowden', 'PhoenixAri1404', 'aditya_sriram', 'parth_reddy', 'manoharparrikar', 'vinaydadhich',
              'ssaxena2', 'Snehan_Peshin', 'chaubeyman', 'agrawalabhishek', 'shankysaraf',
              'sauravnandi', 'preetham18', 'unmarried_joy', 'r1jangid', 'vikky2904', 'DrSalmaShah', 'modi0409',
              'MihirDTweets', 'Kurt_Vonnegut', 'ravishndtv', 'SethMacFarlane', 'Oatmeal', 'dpanikkar',
              'flyinghorsesf', 'roastuggy', 'ImZaheer', 'UGpk', 'RiggedVeda', 'hazardeden10', 'KarlreMarks']

# list_users = ['SortingBot', 'Dev_Fadnavis', 'akanksha_shriv', 'Podcastinator', 'mrrajatkapoor', 'lordmaldy',
#                 'AzmiShabana', 'PritishNandy', 'kejriwal_arvind', 'ArvindKejriwal', 'SalmanRushdie', 'konkonas',
#                 'skipiit', 'anupbishnoi', 'velugoti', 'mythun', 'robinanil', 'somnathmeher', 'sisirkoppaka',
#                 'achyutbihani', 'nachiketmor', 'wowmrinal', 'p_ranjan', 'dheerajthegreat', 'anubhav_sahoo',
#                 'denastro', 'sinhayan', 'aditya_mani_jha', 'P_a_r_a_m', 'vijay013', 'deepthijs', 'umangjn', 'vivnau',
#                 'taurius1']

# list_users = ['MARLONLWAYANS', 'lilduval', 'GuyKawasaki', 'paulocoelho', 'LoriMoreno', 'Alyssa_Milano', 'aplusk',
#               'smashingmag', 'justinbieber', 'SongzYuuup', 'iamdiddy', 'deepakchopra',  'livetorque',
#               'ralphmarston', 'Flipbooks', 'OGOchoCinco', 'zuckerzerg', 'teatattler', 'nghushe', '__Athena___',
#               'AchillesEASaxby', 'DAVID_LYNCH', 'Shockraborty', 'ABrijTooFar', 'iamrana', 'Rekhta', 'smritiirani']

# list_users = ['artagnon', 'HRDMinistry', 'FactCheckIndia', 'earthquakesSF', 'larsonite', 'Maahi_Ve', 'SufiChronicles',
#               'galifianakisz', 'AashishKhetan', 'shutupmikeginn', 'DalrympleWill', 'ABdeVilliers17', 'msdhoni',
#               'Rumi_Quote', 'redditindia', 'ratansebastian', 'JBuch7', 'ravinder_ireddy', 'LeoDiCaprio', 'sachin_rt',
#               'arrahman', 'AllIndiaBakchod', 'Trendulkar', 'ARNABGOSWAMl', 'mishra_pravin', 'BeingSalmanKhan']

# list_users = ['TheWarholMuseum', 'SomersetHouse', 'LarkinQuotes',
#               'JohnCleese', 'jimmycarr', 'stephenfry', 'GareebGuy', 'tavleen_singh', 'amitabhk87',
#               'kaggle', 'NYUDataScience', 'scorewithdata', 'ShakespeareSays', 'awryaditi', 'TheBanat',
#               'TVMohandasPai', 'thevirdas', 'hankypanty', 'maheshmurthy', 'gkhamba', 'thetanmay', 'GhalibPoetry']

# list_users = ['TheTweetOfGod', 'itssylviaplath', 'NASAVoyager', 'MarsOrbiter', 'mojorojo', 'stupidusmaximus',
#               'AksharPathak', 'HridyaHere', 'VarunmThakur', 'svaradarajan']

for name in list_users:

    profile_info(name)
    print name
    # Tweets of a user
    # include_rts = True for retweets
    tweets = api.user_timeline(screen_name = name, include_rts = False, count = 200)
    tweet_info(tweets)

# results = api.search(q = "supermoon", count = 2)
# search(results)


# Store data in the db. Change the connection string according to your db name.
# given conn OR conn = psycopg2.connect(database = "da", username = "", password = "")
print "Database Connection"
conn = psycopg2.connect(database="data_acquisition")
cur = conn.cursor()

cur.executemany("""INSERT INTO twitter_data.twitter_users(id, has_profile_image, has_profile_image_background,
favourites_count, created_at, followers_count, following_count, screen_name, statuses_count) VALUES (%(id)s,
%(has_profile_image)s, %(has_profile_image_background)s, %(favourites_count)s, %(created_at)s,
%(followers_count)s, %(following_count)s, %(screen_name)s, %(statuses_count)s)""", rows)

conn.commit()

cur.executemany("""INSERT INTO twitter_data.tweet(id, user_id, created_at, retweet_count, has_hashtag, has_url,
                                               has_photo, has_video) VALUES\
     (%(id)s, %(user_id)s, %(created_at)s, %(retweet_count)s, %(has_hashtag)s, %(has_url)s, %(has_photo)s,
     %(has_video)s)""", rows_tweet)

conn.commit()

if conn:
    conn.close()
print "Success"

