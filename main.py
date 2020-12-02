import tweepy

auth = tweepy.OAuthHandler('Api key','Api Secret Key')
auth.set_access_token('Access token','Access token secret')

api = tweepy.API(auth)

user = api.get_user('username')
print(user)
print(user.id)
print(user.friends_count)

for post in tweepy.Cursor(api.friends).items():
    print(post.location)