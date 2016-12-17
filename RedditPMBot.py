# Simple PM bot for /r/DrunkenPeasants moderating use
# Made by /u/xGiBbYv or @RainbwowRoxxers on Twitter ^.^
# Date Created/Used/Dumped and never looked at again
# 17/12/16

# Importing the libraries

import praw
import time

# Functions

def lineamount():
    # Get the amount of lines in the txt file. Allowing you to make the array that big when you declare it.
    # Open file
    users = open('users.txt', 'r')
    # lineamount used as a counter
    lineamount = 0
    # Read in Users line by line, counting the number of lines each time.
    for line in users.readlines():
        lineamount = lineamount + 1
    users.close() # Close file 
    return lineamount


def getusers():
    count = 0
    linenum = lineamount() # Number found in function lineamount()
    users = open('users.txt', 'r')
    # Create a list with the same amount of addresses as the amount of users we need to put in it. 
    userlist = [None] * linenum 
    # .readlines() creates a list of each line in the text file. Meaning that all the users are given their own place in the array. We then place a user in the text file into the list we created earlier.
    # Probably would of been better to just use the list it creates itself. Since then you don't need line amount. But I made this just for one use. 
    for line in users.readlines():
        line = line.strip('\n') # Stripes the end of the line if it includes the string provided. Just removes the enter characters that python adds.
        userlist[count] = line
        count = count + 1
    users.close()
    return userlist


def sendpm(reddit):
    userlist = getusers()
    #print(userlist)
    print("Users loaded up into a list")
    count = 0
    messagetxt = open("message.txt").read().replace('\n','') # NOT GOOD PRACTICE FOR LARGE CODE. DON'T USE THIS A LOT.
    print("Message File Opened")
    #reddit.redditor('xgibbyv').message("DP Subreddit Mod Application - DO NOT REPLY", "Hey xgibbyv!" + messagetxt, 'drunkenpeasants')
    while count < lineamount():
        # Not <= because lineamount() shows 37, while the last address in the array is 36.
        reddit.redditor(userlist[count]).message("DP Subreddit Mod Application - DO NOT REPLY", "Hey " + userlist[count] + "!\n\n" + messagetxt, 'drunkenpeasants')
        print("Message sent to ", userlist[count])
        count = count + 1
        # Just incase the server doesn't appreciate me sending 37 messages in one go.
        time.sleep(2)


# Main Code

# "PMBot" takes info from the praw.ini file, like password, client id, and secret. So if you downloaded this from GitHub, no, you cannot login my account or get my details.
# Creating the Reddit Instance to interact with the API
reddit = praw.Reddit("PMBot",user_agent = "Quick PM bot to make it easier to send 40 PM's to potential new mods on /r/DrunkenPeasants. Made by /u/xGiBbYv",)
print("Logged in as ", reddit.user.me())
time.sleep(2)
# Funtion sends the reddit instance so I can mess with the API in that function.
sendpm(reddit)
print("Finished sending messages.")
input("Press Enter to Exit...")



