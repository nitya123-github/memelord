import config
reddit = praw.Reddit(user_agent= config.REDDIT_USER_AGENT,
                  client_id=config.REDDIT_CLIENT_ID,
                  client_secret=config.REDDIT_CLIENT_SECRET,
                  username=config.REDDIT_USERNAME,
                  password=config.REDDIT_PASSWORD
                  )

