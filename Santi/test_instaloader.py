#IMPORTACION DE LIBRERIAS#
import instaloader
import instabot

#IMPORTACION DE CLASES DE INSTALOADER##
from instaloader import Post
from instaloader import Profile

#LOGIN INSTABOT#
bot = instabot.Bot()
bot.login(username = "patagonian_review", password = "comandos1")

#LOGIN INSTALOADER#
L = instaloader.Instaloader()
L.login("patagonian_review","Comandos1")

#Creo objeto de clase Profile#
profile=Profile.from_username(L.context,"igalkej")

#Creo objeto de clase Post#
post = Post.from_shortcode(L.context, "Bh1wRc9Ha9VwwsHAFcHP-viJuh-favoZw0BB4U0")

#Get followees from profile#
print("{} follows these profiles:".format(profile.username))
for followee in profile.get_followees():
    print(followee.username)

#Get number of likes from post#
counter=0
for people in post.get_likes():
	counter+=1
print(counter)

#Obtener la lista de followers de un hashtag (InstaBot).

hashtags = ["Bariloche", "SanMartin", "Patagonia", "Sur",]
hashtag_users = []
for hashtag in hashtags:
    users_one_hashtag = bot.get_hashtag_users(hashtag)
    for users in users_one_hashtag:
        hashtag_users.append(users)

print(hashtag_users)

#Obtener la lista de usuarios que likearon un post

post = Post.from_shortcode(L.context, "Bh1wRc9Ha9VwwsHAFcHP-viJuh-favoZw0BB4U0")
likers=[]
for liker in post.get_likes():
	likers.append(liker.username)


#Get metadata del usuario
user_info_dic_list = []
for user in users_to_follow[1:50]:
    user_info = bot.get_user_info(user)
    user_info_dic_list.append(user_info)

#Obtener ratio de seguidores

USERNAME = "igalkej"
dic_user_info=bot.get_user_info(USERNAME)
ratio = dic_user_info.get("follower_count")/dic_user_info.get("following_count")


#SUBIR FOTO
bot.upload_photo(photo = "/home/santiago/Downloads/WhatsApp Image 2020-03-14 at 18.01.56.jpeg",
                 caption = "Puerto Patriada, Chubut, Argentina unforgettable place /n #Patagonia #l:130245771112629")

#SEGUIR USUARIOS
#bot.follow_users(hashtag_users[1:50])


### INTENTO DE CONSEGUIR UNA LISTA DE USERS #####
hashtags = ["Bariloche", "SanMartin", "Patagonia", "Sur",]
hashtag_users = []
for hashtag in hashtags:
    users_one_hashtag = bot.get_hashtag_users(hashtag)
    for users in users_one_hashtag:
        hashtag_users.append(users)

post = Post.from_shortcode(L.context, "Bh1wRc9Ha9VwwsHAFcHP-viJuh-favoZw0BB4U0")
likers=[]
for liker in post.get_likes():
        likers.append(liker.username)


candidates_to_follow = likers + hashtag_users

users_to_follow = random.sample(candidates_to_follow,100)

bot.follow_users(users_to_follow)

user_info_dic_list = []
for user in users_to_follow:
    user_info = bot.get_user_info(user)
    user_info_dic_list.append(user_info)


