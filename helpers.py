import json
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
