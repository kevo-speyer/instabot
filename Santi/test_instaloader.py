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
	new_users_to_follow_info_dic_list = []
	for user in username_list:
    		user_info = bot.get_user_info(user)
    		new_users_to_follow_info_dic_list.append(user_info)

	return new_users_to_follow_info_dic_list

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


