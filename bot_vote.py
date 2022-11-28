import praw
from textblob import TextBlob

reddit = praw.Reddit ('bot', user_agent='cs40')
subreddit = reddit.subreddit('cs40_2022fall')
print("getting submissions")
submissions = list(subreddit.top(limit=None))
for submission in submissions:
    print("looking at submission")
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()

    not_my_comments = []

    for comment in all_comments:
        print("looking at a comment")
        try:
            if comment.author=="zogobot":
                pass
            else:
                not_my_comments.append(comment)
                print("checking")
                if "Trump" in comment.body:
                    blob= TextBlob(comment.body)
                    if blob.sentiment.polarity>0:
                        comment.downvote()
                    else: 
                        comment.upvote()
        except Exception as e:
            print(e)