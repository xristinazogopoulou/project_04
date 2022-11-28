import praw
import time 
import random 

while True:
    reddit = praw.Reddit('bot')
    subreddit = reddit.subreddit('cs40_2022fall')
    hot_sub = list(reddit.subreddit('liberal').hot(limit=None))
    submission = random.choice(hot_sub)
    content = submission.selftext 
    title = submission.title
    if content == '':
        link = submission.url
        subreddit.submit(title, url = link)
        print('posted linkpost')
    else: 
        subreddit.submit(title, selftext = content)
        print('posted textpost')

    time.sleep(1)