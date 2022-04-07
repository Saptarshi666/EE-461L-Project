from asyncio.windows_events import NULL
from datetime import date
from http import client
from operator import contains
from pickle import FALSE
from sqlite3 import Date
import pymongo
from pymongo import MongoClient
import encrypt
import datetime
import pprint
# ajstiles caWpDYgtyCH0Z1JU
# ^^user   ^^cluster password --> mongodb info
# change next line if you testing with your own mongodb if you want to be able to see inside
Client=MongoClient("mongodb+srv://ajstiles:caWpDYgtyCH0Z1JU@cluster0.fvy1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = Client['Users']
db = Client['Projects']
db = Client['HWSets']
db = Client['Physionet']
username = ''
auth = FALSE

# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** ctrl+f and REMOVE INPUTS ***************8888

def add_base_hwset(): # (projID ??):
        # probably add this to some sort of initializtion or check to see if sets/database got reset
        db = Client['HWSets']
        if db.list_collection_names().__contains__('HW Set1') and db.list_collection_names().__contains__('HW Set2'):
                return
        set = db['HW Set1']
        post = {
                "HWSet Name": "HW Set1",
                "Capacity": 100,
                "Availability": 100
                }
        post_id = set.insert_one(post).inserted_id
        post_id
        set = db['HW Set2']
        post = {
                "HWSet Name": "HW Set2",
                "Capacity": 150,
                "Availability": 150
                }
        post_id = set.insert_one(post).inserted_id
        post_id

def add_custom_hwset(): # (projName,setName, capc, avail, auth): # comments like this is needed inputs if this is to act as a methods only file that is called by another
        # TODO remove inputs
        projID = input('add hwset to project id- ')
        db = Client['Projects']
        project = db[projID]
        if not project.find_one({"Project ID": projID}):
                print("project not exists")
                return False
        setName = input("HWSet Name: ") # remove input statements like this one when receiving data from front end
        if project.find_one({"HWSet Name": setName}):
                print('hwset already exists')
                return False
        capc = int(input("capacity: "))
        avail = int(capc)
        post = {
                "HWSet Name": setName,
                "Capacity": capc,
                "Availability": avail
                }
        post_id = project.insert_one(post).inserted_id
        post_id

def check_out_hw(): # (projID, setName, number):
        # TODO what to do about logging out with sets forever?
        setName = input('check out set name- ')
        db = Client['HWSets']
        set = db[setName]
        if not set.find_one({"HWSet Name": setName}):
                print('hwset not exists')
                return False
        avail_temp = set.find_one({"HWSet Name": setName}, {"_id": 0, "Availability": 1})
        avail = avail_temp["Availability"]
        if avail == 0:
                print('no sets currently available')
                return False
        number = int(input('how many- '))
        if number > avail:
                print('not enough available to match your request')
                number = avail
        set.update_one({"HWSet Name": setName}, {'$inc':{'Availability': -number}})
        db = Client['Users']
        user = db[username]
        if not user.find_one({"HWSet Name": setName}):
                user.insert_one({"HWSet Name": setName, "Current Out": number})
        else:
                user.find_one_and_update({"HWSet Name": setName}, {"$inc":{"Current Out": number}})

def check_in_hw(): # (setName, number):
        setName = input('check in set name- ')
        db = Client['Users']
        user = db[username]
        if not user.find_one({"HWSet Name": setName}):
                print('hwset not checked out')
                return False
        out_temp = user.find_one({"HWSet Name": setName}, {"_id": 0, "Current Out": 1})
        current_Out = out_temp["Current Out"]
        number = int(input('how many- '))
        if number > current_Out:
                print('this is more than you have checked out, try again')
                return False
        user.update_one({"HWSet Name": setName}, {'$inc':{'Current Out': -number}})
        out_temp = user.find_one({"HWSet Name": setName}, {"_id": 0, "Current Out": 1})
        current_Out = out_temp["Current Out"]
        if current_Out == 0:
                print('all units of this set checked back in')
                user.find_one_and_delete({"HWSet Name": setName})
        db = Client['HWSets']
        set = db[setName]
        set.update_one({"HWSet Name": setName}, {'$inc':{'Availability': number}})

def add_project(): # (,projName, desc, auth):
        # TODO remove inputs
        # maybe make a method to pull name from project db based on if user has the corresponding projID attatched to their acct
        # so that it can always be displayed
        # either this or, as i did in delete_project(), simply add name to each projDoc in its members and update name, desc if its ever changed etc.
        projName = input("Project Name- ") # remove inputs when receiving data from front end
        db = Client['Projects']
        project = db[projName]
        if project.find_one({"Project Name": projName}):
                print('project name already in use')
                return False
        desc = input("project description- ")
        projID = input('project id- ')
        if project.find_one({"Project ID": projID}):
                print('project id already exists')
                return False
        post = {
                "Project Name": projName,
                "Description": desc,
                "Project ID": projID,
                "Members": [username]
                }
        # consider removing the user push, instead only pushing project ID
        project = db[projName]
        post_id = project.insert_one(post).inserted_id
        post_id
        db = Client['Users']
        user = db[username]
        user.insert_one({"_id": projID})
        return True

def join_project(): # (projID):
        projID = input("join project enter ID- ")
        db = Client['Users']
        user = db[username]
        if user.find_one({"_id": projID}):
                print('project already joined')
                return False
        db = Client['Projects']
        project = db[projID]
        if not project.find_one({"Project ID": projID}):
                print('project not exists')
                return False
        project.find_one_and_update({"Project ID": projID}, {"$addToSet": {"Members": username}})
        db = Client['Users']
        user = db[username]
        user.insert_one({"_id": projID})
        return True

def edit_project(): #(projID):
        # dont know if we want this yet, basically can only edit title and desc anyway
        # maybe true owner can kick users or add them manually? true owner is [0] in users array in the project docu
        print('idk if we doing this')
        # user.find_one_and_update({"Project ID": projID}, {"$set": {"Description": 'new desc'}}) 

def delete_project(): # (projID):
        projID = input('delete project id- ')
        db = Client['Users']
        user = db[username]
        if not user.find_one({"_id": projID}):
                print('project not exists')
                return False
        db = Client['Projects']
        project = db[projID]
        if not project.find_one({"Project ID": projID}):
                print('project not exists')
                return False
        members_grab = project.find_one({"Project ID": projID}, {"_id": 0, "Members": 1})
        members = members_grab["Members"]
        project.drop()
        db = Client['Users']
        for element in members:
                user = db[element]
                user.find_one_and_delete({"_id": projID})
        return True

def make_user(user, password):
        # TODO remove INPUTS when receiving data from front end
        # check for strength of pw? maybe for the future
        # add encryption
        db = Client['Users']
        if db.list_collection_names().__contains__(user):
                print('username unavailable')
                return False
        global username
        username = user
        post = {
                "Username": username,
                "Password": password,
                "Funds": 100
                }
        user = db[user]
        post_id = user.insert_one(post).inserted_id
        post_id
        print('Welcome ' + username + '!')
        return True

def add_Funds():
        print('are we doing funds?')

def check_user_password(user, password):
        # TODO add reverse encryption
        # add limit on attempts? attempts per user or machine?
        global username
        db = Client['Users']
        userCheck = db[user]
        if not userCheck.find_one({"Username": user, "Password": password}):
                print('login credentials incorrect')
                return False
        else:
                username = user
                print('Welcome ' + username + ' !')
                return True

def log_out():
        # add tracker of checkouts to mass checkin upon logout
        global username
        username = ''

add_base_hwset()
# *********** TESTING WITH INPUTS REMOVE BELOW
print(db.list_collection_names())
if not make_user('alberto', 'pass'):
        check_user_password('alberto', 'pass')
add_project()
log_out()
if not make_user('alberto2', 'pass2'):
        check_user_password('alberto2', 'pass2')
# add_project()
join_project()
# check_out_hw()
# check_in_hw()
# print('make next project ID is delete no spaces')
delete_project()
# add_custom_hwset()
log_out()
# *********** END OF MANUAL TEST DONT REMOVE STUFF PAST HERE

Client.close()

# TODO
# encrypt password (HW1) cypher
# get info from ui 
# lock user info behind password 
# physio??? 5 sets, have link to download in mongodb