import json
import instaloader
import instabot

def read_my_user_n_pass():
    account_data_file = "./account_data.json"
    try:
        with open(account_data_file, 'r') as fp:
            account_data = json.load(fp)
    except: 
        print(f"Error, file {account_data_file} not found")
    return account_data

def log_to_user(account_data):
    try:
        L = instaloader.Instaloader()
        L.login(user=account_data["user"],passwd=account_data["pass"])
    except:
        print("Error couldn't login to account with instaloader")

    try:
        bot = instabot.Bot()
        bot.login(username = account_data["user"], password = "comandos1")
    except:
        print("Error couldn't login to account with instabot")

    return L, bot


def users_list_from_hashtags(hashtags):
        print("Importing ~ 85 usernames for each hashtag")
        hashtag_users = []
        try:
                for hashtag in hashtags:
                         users_one_hashtag = bot.get_hashtag_users(hashtag)
                         for users in users_one_hashtag:
                                hashtag_users.append(users)
        except:
                print("couldn't get users from given hashtags") 

        return hashtag_users


def users_list_from_post_shortcode_list(post_shortcode_list):
        print("Importing <1000 usernames for each post")
        likers=[]
        for shortcode in post_shortcode_list:
                post = Post.from_shortcode(L.context, shortcode)
                for liker in post.get_likes():
                        likers.append(liker.username)
                        print(len(likers))
                        if len(likers) == 999:
                                break
        return likers

