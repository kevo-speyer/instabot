import instabot
bot = instabot.Bot()
bot.login()
1
#Obtener la lista de followers que interesa.

hashtags = ["Bariloche", "SanMartin", "Patagonia", "Sur"]
hashtag_users = []
for hashtag in hashtags:|
    users_one_hashtag = bot.get_hashtag_users(hashtag)
    for users in users_one_hashtag:
        hashtag_users.append(users)

#La lista de potenciales a seguir está en hashtag_users

#Pruebo seguir a 50
bot.follow_users(hashtag_users[1:50])

# Quiero obtener toda la informacion que se pueda de ellos.

# df = DataFrame(list(diccionario.items()) #Lo transformo a dataframe, o me amigo con los diccionarios.

user_info_dic_list = []
for user in hashtag_users:
    user_info = bot.get_user_info(user)  # Es un diccionario
    user_info_dic_list.append(user_info)

ds = user_info_dic_list.append
d = {}
for k in ds[1].keys():
    d[k] = tuple(d[k] for d in ds)




