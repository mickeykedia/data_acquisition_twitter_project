tdat  <- as.data.frame(read.table("data_analysis", sep = ",", stringsAsFactors = FALSE, row.names = NULL, header = TRUE))
                       
hist(tdat$retweet_count)
summary(tdat$retweet_count)
head(tdat)
tdat["flag"] <- sapply(tdat$max_cnt, function(x){
  if(x > 700) {return(1)} else {return(0)}
})
hgh_rtwt <- tdat[which(tdat$flag ==1), ]
low_rtwt <- tdat[which(tdat$flag ==0), ]

#### Hypothesis 1 ########################################
# If a tweet has hashtag then average retweet count is higher for these 
# tweets in comparison to those which do not have hashtag(one or more)
# Checked for normality..both samples are approximately normal
qqPlot(tdat[which(tdat$has_hashtag == "t"), 2])
qqPlot(tdat[which(tdat$has_hashtag == "f"), 2])
# Check for Variance
sd(tdat[which(tdat$has_hashtag == "t"), 2])
sd(tdat[which(tdat$has_hashtag == "f"), 2])
wilcox.test(tdat[which(tdat$has_hashtag == "t"), 2],
            tdat[which(tdat$has_hashtag == "f"), 2],
            alternative = c("greater"),
            paired = FALSE, exact = NULL, correct = FALSE,
            conf.int = FALSE, conf.level = 0.95)
# Resuts
# W = 60484, p-value = 1.022e-14
# alternative hypothesis: true location shift is greater than 0
# alternate hypothesis is validated to be true
(mean(tdat[which(tdat$has_hashtag == "t"), 2]) - mean(tdat[which(tdat$has_hashtag == "f"), 2])) / mean(tdat[which(tdat$has_hashtag == "f"), 2])
# 1.746978


#### Hypothesis 2 ########################################
# If a tweet has URL then average retweet count is higher for these 
# tweets in comparison to those which do not have url
# Checked for normality..both samples are approximately normal
wilcox.test(tdat[which(tdat$has_url == "t"), 2],
            tdat[which(tdat$has_url == "f"), 2],
            alternative = c("greater"),
            paired = FALSE, exact = NULL, correct = FALSE,
            conf.int = FALSE, conf.level = 0.95)
# Resuts
# W = 98510, p-value = 0.05771
# alternative hypothesis: true location shift is greater than 0
# alternate hypothesis is validated to be true
(mean(tdat[which(tdat$has_url == "t"), 2]) - mean(tdat[which(tdat$has_url== "f"), 2])) / mean(tdat[which(tdat$has_url == "f"), 2])

#### Hypothesis 3 ########################################
# If a tweet has photo then average retweet count is higher for these 
# tweets in comparison to those which do not have photo
# Checked for normality..both samples are approximately normal
wilcox.test(tdat[which(tdat$has_photo == "t"), 2],
            tdat[which(tdat$has_photo == "f"), 2],
            alternative = c("greater"),
            paired = FALSE, exact = NULL, correct = FALSE,
            conf.int = FALSE, conf.level = 0.95)
# Resuts
# W = 49909, p-value < 2.2e-16
# alternative hypothesis: true location shift is greater than 0
# alternate hypothesis is validated to be true
(mean(tdat[which(tdat$has_photo == "t"), 2]) - mean(tdat[which(tdat$has_photo== "f"), 2])) / mean(tdat[which(tdat$has_photo == "f"), 2])
# 0.8101095

#### Hypothesis 4 ########################################
# no data to capture this... we can say media for photo
# If a tweet has video then average retweet count is higher for these 
# tweets in comparison to those which do not have video
# Checked for normality..both samples are approximately normal
wilcox.test(tdat[which(tdat$has_video == "t"), 2],
            tdat[which(tdat$has_video == "f"), 2],
            alternative = c("greater"),
            paired = FALSE, exact = NULL, correct = FALSE,
            conf.int = FALSE, conf.level = 0.95)
# num of records with video = 0

#### Hypothesis 5 ########################################
# increase in favorite count increases the number of retweets
# Results:
# correlation Coefficient: 0.96194
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}
scatterplot_matrix <- function(test) {
  name <- colnames(test)
  print(name)
  plots <-  list()
  for (i in 2:ncol(test)) {
    test1 <- test[ , which(names(test) %in% c(name[1],name[i]))]
    colnm <- colnames(test1)
    string <- formula(paste(colnm[1], '~', colnm[2]))
    lm_cakes <- lm(string, data = test1)
    plots[[i]] <-  ggplot(lm_cakes$model, aes_string(x = names(lm_cakes$model)[2], 
                                                     y = names(lm_cakes$model)[1]),  
                          environment = environment()) + 
      geom_point(size = 3, color = "blue") +
      stat_smooth(method = "lm", col = "red") +
      theme(axis.text.x = element_text(colour = "black",
                                       vjust = -0.35, 
                                       size = 11)) +
      theme(axis.text.y = element_text(colour = "black",
                                       vjust = 0.5, 
                                       size = 11)) +
      labs(title = paste("R2 = ",signif(summary(lm_cakes)$r.squared, 5),
                         "Radj =",signif(summary(lm_cakes)$adj.r.squared,5 ),
                         " Slope =",signif(lm_cakes$coef[[2]], 5),
                         " P =",signif(summary(lm_cakes)$coef[2,4], 5))) +
      theme(axis.line = element_line(colour = "black"),
            plot.title = element_text(face="bold")) +
      xlab(names(lm_cakes$model)[2]) + ylab(names(lm_cakes$model)[1])
  }
  multiplot(plotlist=plots[-1], ncol =3)
}

# plot(cakes1$time, cakes1$temp)
scatterplot_matrix(tdat[,c(2,8)])
cor(tdat[,c(2,8)]) #  0.9807831  

#### Hypothesis 6 ########################################
# If user who made the tweet has a profile image
# then average retweet count is higher for these 
# tweets in comparison to those which do not have profile image

wilcox.test(tdat[which(tdat$has_profile_image == "t"), 2],
            tdat[which(tdat$has_profile_image == "f"), 2],
            alternative = c("greater"),
            paired = FALSE, exact = NULL, correct = FALSE,
            conf.int = FALSE, conf.level = 0.95)
# REsults
# W = 33013, p-value = 1
# alternative hypothesis: true location shift is greater than 0

#### Hypothesis 7 ########################################
# More the number of followersretweet count is higher for these 
# users

scatterplot_matrix(tdat[,c(2,16)]) # followers
cor(tdat[,c(2,16)]) # 0.5605956  


# Check that correlation coefficient is different from zero..rho ≠ 0

t <- 0.5605956  * sqrt((915)/(1 - 0.5605956^2 )) 
# t  = 20.47778 Hence proved

#### Hypothesis 7 ########################################
# More the number of following, retweet count is higher for these 
# users

scatterplot_matrix(tdat[,c(2,17)]) # following
cor(tdat[,c(2,17)]) # 0.01657466      


# Check that correlation coefficient is different from zero..rho ≠ 0

t <- 0.01657466 * sqrt((915)/(1 - 0.01657466^2 )) 
# t  = 0.5014 Hence proved
