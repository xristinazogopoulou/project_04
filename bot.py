import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "Senator Bernie Sanders has enjoyed a [REMARKABLY] long career as the [ULTIMATE] political outsider. His signature message of income [INEQUALITY], delivered with a metronomic, almost numbing consistency, has often seemed like the [ONLY] thing [ONE] needed to know about him—that is, until he surged to the forefront of the 2020 Democratic field.",
    "On October 23, 1971, at a [MEETING] in Vermont of the [SMALL], anti-war Liberty Union Party, Sanders, 30, raised his hand to run for U.S. Senate. He ran on the Liberty Union ticket for Senate in a [SPECIAL] election in [EARLY] 1972, and for governor later that year, and for Senate again in 1974, and for governor again in 1976. He never [GOT] more than 6 percent of the vote.",
    "He [STARTED] a business [PRODUCING] low-budget filmstrips about Vermont and New England history that he sold to schools. He [MADE] a 30-minute documentary on Eugene Debs, a [PROMINENT] labor organizer in the early 1900s and the five-time presidential candidate of the Socialist Party of America—whom Sanders has [CITED] as a hero.",
    "Sanders [PROPOSES] a $16.3tn (£12.5tn) Green New Deal that he [SAYS] would create 20 million jobs and pay for itself over 15 years, including through $3tn of taxes on oil companies. Sanders [SUPPORTS] the environment and wants to adopt [LEGISLATION] to [PROTECT] it",
    "With an anti-establishment [STYLE] that has [CHANGED] little over five decades, Mr. Sanders has attracted a [LOYAL] cadre of fans. He often boasts, correctly, that some of his agenda items once [CONSIDERED] radical — “Medicare for all,” a $15 minimum wage, tuition-free public college — have [NOW] been embraced by many Democrats."
    "Bernie Sanders is a [GREAT] [OLD] [MAN]. [EVERYBODY] [LOVES] Bernie Sanders. "
    ]
replacements = {
    'REMARKABLY' : ['exceptionally', 'remarkably'],
    'ULTIMATE' : ['absolute', 'ultimate'],
    'INEQUALITY' : ['inequity', 'inequality', 'disproportion'],
    'ONLY' : ['sole', 'only', 'single'],
    'ONE' : ['someone', 'somebody', 'anoyone'],
    'MEETING'  : ['assembly', 'conference', 'gathering'],
    'SMALL' : ['little', 'small-scale', 'tiny'],
    'SPECIAL' : ['particular', 'exceptional'],
    'EARLY' : ['the beginning of', 'early'],
    'GOT' : ['got', 'received'],
    'STARTED' : ['initiated', 'started', 'established'],
    'PRODUCING' : ['creating', 'producing'],
    'MADE' : ['created', 'made', 'produced'],
    'PROMINENT' : ['eminent', 'important', 'prominent'],
    'CITED' : ['mentiioned', 'presented', 'cited'],
    'PROPOSES' : ['proposes', 'suggests' 'offers'],
    'SAYS' : ['highlights','mentions' 'says'],
    'SUPPORTS' : ['helps', 'assists' 'supports'],
    'LEGISLATION' : ['law', 'legislation', 'code'],
    'PROTECT' : ['safeguard', 'save', 'protect'],
    'STYLE' : ['way', 'style', 'methodology'],
    'CHANGED': ['altered', 'transformed', 'changed'],
    'LOYAL' : ['devoted', 'faithful', 'loyal'],
    'CONSIDERED': ['perceived', 'considered'],
    'NOW': ['currently', 'now'],
    'GREAT': ['great', 'amazing', 'spectacular'],
    'OLD': ['aged', 'senior', 'elder'],
    'MAN': ['person', 'human', 'man'],
    'EVERYBODY':['everyone', 'all people', 'anybody'],
    'LOVES': ['adores', 'loves']}

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib 

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/ywdc19/cs40_zogobot_test/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()


    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not

    not_my_comments = []
    for comment in all_comments:
        if comment.author != 'zogobot':
            not_my_comments.append(comment)
    
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        

        submission.reply(body=generate_comment())
        print('top level comment')

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            reddit_reply = True 
            for reply in comment.replies:
                if reply.author == 'zogobot':
                    reddit_reply = False 

            if reddit_reply == True:
                comments_without_replies.append(comment)


        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        
        if len(comments_without_replies)>0:
            
            random_comment = random.choice(comments_without_replies)
            random_comment.reply(body=generate_comment())
            print('reply to a comment')
        

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    hot_sub = list(reddit.subreddit('cs40_2022fall').hot(limit=5))
    submission = random.choice(hot_sub)


    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1)
