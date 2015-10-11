setwd("/Users/mayankkedia/Documents/USF/Data_Acquisition/Presentation/")
df <- read.csv("data_twitter.csv", header = TRUE)
head(df)


as.numeric(as.character(df$has_hashtag))
df[df$has_hashtag =='t','has_hashtag_bin']<- 1
df[df$has_hashtag =='f','has_hashtag_bin']<- 0

df[df$has_url =='t','has_url_bin']<- 1
df[df$has_url =='f','has_url_bin']<- 0

df[df$has_photo =='t','has_photo_bin']<- 1
df[df$has_photo =='f','has_photo_bin']<- 0


df[df$has_profile_image =='t','has_profile_image_bin']<- 1
df[df$has_profile_image =='f','has_profile_image_bin']<- 0

df[df$has_profile_image_background =='t','has_profile_image_background_bin']<- 1
df[df$has_profile_image_background =='f','has_profile_image_background_bin']<- 0
d <- df[c(4, 9, 16, 18, 19, 21, 22, 23, 24, 25, 26)]

l <- lm(retweet_count ~ ., d)
summary(l)
l <- lm(retweet_count ~ . - has_profile_image_bin - following_count, d)
summary(l)

l <- lm(retweet_count ~ . - has_profile_image_bin - following_count - has_hashtag_bin, d)
summary(l)
