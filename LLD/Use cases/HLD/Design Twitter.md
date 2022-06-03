Design Twitter
    User can add a tweet
    User can see his own tweets
    User can see his timeline -> see the latest posts from his/her friends
    User can follow and unfollow


user_service -> registration, login, follow, unfollow
tweet_service -> add_tweet(user_id, tweet_body)
timeline_service -> get_next_timeline(user_id)

User Database:
    user_id,
    name,
    email

Follower DB:
    followers:
        user_id,
        follower_ids

    follows:
        user_id,
        follow_ids

write_based_fanout_approach
social graph service
flock => all the followers and who the user follows


