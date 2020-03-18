#IMPORTACION DE LIBRERIAS#
import instaloader
import instabot
from instaloader import Post
from instaloader import Profile

import os
import csv
import datetime
from datetime import datetime
from datetime import time


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


#Get usernames for hashtaf


def users_list_from_hashtags(hashtags):
	print("Importing ~ 85 usernames for each hashtag")
	hashtag_users = []
	hashtag_usernames = []

	try:
		for hashtag in hashtags:
   			 users_one_hashtag = bot.get_hashtag_users(hashtag)
   			 for users in users_one_hashtag:
        			hashtag_users.append(users)
		
		for user_id in hashtag_users:
			username = bot.get_username_from_user_id(user_id)
			hashtag_usernames.append(username)
					

	except:
		print("couldn't get users from given hashtags") 

	return hashtag_usernames 



#Obtener la lista de usuarios que likearon un post

def users_list_from_post_links_list(post_links_list):
	print("Importing <1000 usernames for each post")
	likers_id = [] 
	likers_username= []
	counter = 0
	try:
		for link in post_links_list: 
			
			post_id = bot.get_media_id_from_link("https://www.instagram.com/p/B9nKn1Th8h9/")
			post_likers=bot.get_media_likers(post_id) 
			likers_id.append(post_likers)
		
		for liker_id in likers_id:
			likers_username[counter] = bot.get_username_from_user_id(likers_id[counter]) 
 			counter += 1
	except:
		print("couldn't get users from given posts")
	
	return likers_username


#Obtener la lista de usuarios que likearon un post
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



#Get metadata del usuario
def user_metadata_from_usernames_list(username_list):
	new_following_info_list = []
	for user in username_list:
    		user_id = bot.get_user_id_from_username(user)
		user_info = bot.get_user_info(user_id)
    		new_following_info_list.append(user_info)

	return new_following_info_list



def follow_new_users(users_to_follow):
	with open("recent_following.txt", "w") as f:
		for user in users_to_follow:
			f.write("%s\n" % user)
			bot.follow(user)

	new_following_data = user_metadata_from_usernames_list(users_to_follow) 
 	for dictionary in new_following_data: 
		now=datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		dictionary["datetime"] = dt_string   
	
	with open("followed_users_data.json","r") as rf:
		old_data = json.load(rf)
		updated_data = old_data + new_following_data
	
	with open("followed_users_data.json","w") as wf:
		json.dump(updated_data, wf)
		 



def unfollow_not_recent_followback():
	counter = 0
	current_followers = []
	
	for user_id in bot.followers:
		current_followers.append(bot.get_username_from_user_id(user_id))
	 
	with open("recent_following.txt", "r") as rf:
		reader=csv.reader(rf)
		recent_followed = list(reader)
	for user in recent_followed:
		recent_followed[counter] = user[0]
                counter += 1
	
	for user in recent_followed: 
		if user not in current_followers:
			bot.unfollow(user)



def unfollow_non_followers_until_ratio(desired_ratio):
	account_data_file = "./account_data.json"

	with open(account_data_file, 'r') as fp:
		account_data = json.load(fp)
		username = account_data["user"] 
	
	dic_user_info=bot.get_user_info(username)
	
	followers = dic_user_info.get("follower_count")
	followed = dic_user_info.get("following_count")
	current_ratio = followers / followed
	
	if current_ratio < desired_ratio: 
		followed_deseados = followers/desired_ratio
		unfollows_to_perform = round(followed - followed_deseados)
		bot.unfollow_non_followers(unfollows_to_perform)
	else: 
		print("Current ratio already satisfies your desire :)")
		
		
	



	



#FILTRAR USUARIOS A SEGUIR

def filter_userlist_by_blacklist(usernames):
	usernames_blacklist=[]
	usernames_whitelist=[]
	try:
		with open("blacklist.txt") as f:
			reader=csv.reader(f)
			blacklist=list(reader)
	
	except:
		print("couldn't find or open blacklist file")

	try:
		for user in blacklist:
			user_id = user[0]
	       		usernames_blacklist.append(user_id)

				
		for user in usernames: 
			if user not in usernames_blacklist:
				usernames_whitelist.append(user)
							
	except: 

		print("couldn't get users to follow")	
		
	return usernames_whitelist

def definitive_users_to_follow_by_number(usernames, number):
	definitive_list = random.sample(usernames, number)
	
	return definitive_list 
	




##FOLLOW AND GATHER INFORMATION FUNCTION###

		
#Obtener ratio de seguidores

USERNAME = "igalkej"
dic_user_info=bot.get_user_info(USERNAME)
ratio = dic_user_info.get("follower_count")/dic_user_info.get("following_count")


#SUBIR FOTO
bot.upload_photo(photo = "/home/santiago/Downloads/WhatsApp Image 2020-03-14 at 18.01.56.jpeg",
                 caption = "Puerto Patriada, Chubut, Argentina unforgettable place /n #Patagonia #l:130245771112629")

#SEGUIR USUARIOS
#bot.follow_users(hashtag_users[1:50])


