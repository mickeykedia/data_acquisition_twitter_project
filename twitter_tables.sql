create schema twitter_data;


create table twitter_data.twitter_users (
    id bigint constraint userkey PRIMARY KEY,
    has_profile_image boolean,
    has_profile_image_background boolean,
    favourites_count int,
    created_at timestamp,
    followers_count int,
    following_count int,
    screen_name varchar(128),
    statuses_count int );


create table twitter_data.tweet (
    id bigint constraint tweetkey PRIMARY KEY,
    user_id bigint references twitter_data.twitter_users(id),
    created_at timestamp,
    retweet_count int,
    has_hashtag boolean,
    has_url boolean,
    has_photo boolean,
    has_video boolean,
    favorite_count integer,
    latitude float,
    longitude float,
    location varchar(32)
   );

