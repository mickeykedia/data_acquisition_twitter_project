create schema twitter_data;

create table twitter_data.hashtag (
    id integer constraint hashtagkey PRIMARY KEY, 
    name varchar(128) NOT NULL);

create table twitter_data.twitter_users (
    id bigint constraint userkey PRIMARY KEY, 
    has_profile_image boolean, 
    has_profile_image_background boolean, 
    favourites_count int, 
    created_at date, 
    followers_count int, 
    following_count int, 
    screen_name varchar(128),
    statuses_count int );

create table twitter_data.tweet (
    id bigint constraint tweetkey PRIMARY KEY, 
    user_id bigint references twitter_data.twitter_users(id),
    created_at date, 
    retweet_count int,
    has_hashtag boolean, 
    has_url boolean, 
    has_photo boolean, 
    has_video boolean, 
    latitude float, 
    longitude float,
    location varchar(32)
    );

create table twitter_data.tweet_hashtags (
    hashtag_id int references twitter_data.hashtag(id),
    tweet_id bigint references twitter_data.tweet(id),
    PRIMARY KEY (hashtag_id, tweet_id)
    );


