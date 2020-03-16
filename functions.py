import json
import instaloader
import instabot
from helpers import *

def main():
    login_data = read_my_user_n_pass()   
    print(login_data)
    L, bot = log_to_user(login_data)
    
    print("succes")






if __name__ == "__main__":
    main()
