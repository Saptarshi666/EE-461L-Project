from asyncio.windows_events import NULL
# from crypt import methods
from datetime import date
from http import client
import json
from operator import contains
from pickle import FALSE
from sqlite3 import Date
from unittest import result
from numpy import printoptions
import pymongo
from pymongo import MongoClient
import os
import wfdb
import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
from flask import Flask, jsonify, session, request
from flask.helpers import send_from_directory
from flask_cors import CORS
# ajstiles caWpDYgtyCH0Z1JU
# ^^user   ^^cluster password --> mongodb info
# change next line if you testing with your own mongodb if you want to be able to see inside
print('hello world')
Client=MongoClient("mongodb+srv://ajstiles:caWpDYgtyCH0Z1JU@cluster0.fvy1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = Client['Users']
db = Client['Projects']
db = Client['HWSets']
db = Client['PhysioNet']
username = ''
Password = ''
auth = FALSE
app = Flask(__name__, static_folder='./frontend/build', static_url_path="")
CORS(app)
# fernet = Fernet.generate_key()
fernet = b'dGbn-lNuJMHD7BAHzxzq-6Ji158xIxMHQlGrFXit7H0='
f = Fernet(fernet)
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** YOU MUST REMOVE INPUTS ***************8888
# ****************** ctrl+f and REMOVE INPUTS ***************8888

def add_base_hwset(): # (projID ??):
        # probably add this to some sort of initializtion or check to see if sets/database got reset
        # while adding this also add something to bring in the 5 OG physio datasets
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
        # any user can check in the checked out hw for a project, and ofc can check out more if available
        # hw set not like a library book
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

@app.route("/NewProj", methods=["GET", "POST"])
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

@app.route('/newuser', methods=['GET', 'POST'])
def make_user():
        print('make user')
        # TODO remove INPUTS when receiving data from front end
        # check for strength of pw? maybe for the future
        # add encryption
        params = request.get_json()
        print(params)
        username, password = params['username'].strip(), params['password'].strip()
        print(type(username))

        db = Client['Users']
        if db.list_collection_names().__contains__(username):
                print('username unavailable')
                return jsonify(result = 'False')
        token = f.encrypt(username.encode())
        print(token)
        token2 = f.encrypt(password.encode())
        print(token2)
        post = {
                "Username": token,
                "Password": token2
                }
        user = db[username]
        post_id = user.insert_one(post).inserted_id
        post_id
        print('Welcome ' + username + '!')
        return jsonify(result = "True")

def add_Funds():
        print('are we doing funds?')

@app.route('/login', methods=["GET", "POST"])
def check_user_password():
        print('check user')
        # TODO add reverse encryption
        # add limit on attempts? attempts per user or machine?
        print(fernet)
        params = request.get_json()
        print(params)
        username, password = params['username'].strip(), params['password'].strip()
        print(type(username))
        db = Client['Users']
        user = db[username]
        if not db.list_collection_names().__contains__(username):
                print("no such user exists")
                return jsonify(result = "True")
        enc_user = user.find_one()
        print("enc_user: ")
        print(enc_user)
        enc_username = enc_user["Username"]
        print(enc_username)
        dec_username = f.decrypt(enc_username).decode()
        print(dec_username)
        print(username)
        enc_password = enc_user["Password"]
        print(enc_password)
        dec_password = f.decrypt(enc_password).decode()
        print(dec_password)
        print(password)
        if username != dec_username or password != dec_password:
                print("login credentials incorrect")
                return jsonify(result = "True")
        else:
                print('Welcome ' + username + ' !')
        return jsonify(result = "True")

def log_out():
        # add tracker of checkouts to mass checkin upon logout
        global username
        username = ''

# PhysioNet Citation:
# Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.
def add_physio_db(pdbAbbrev): # (pdbAbbrev, pdbDesc): 
        # small sizes are aami-ec13, bpssrat, need 3 more
        # TODO no duplicates
        # TODO add descriptions
        # maybe add counter for number of downloads?
        dbs = wfdb.get_dbs()
        # pdbAbbrev = input('enter pdb- ')
        for i in range(len(dbs)):
                if dbs[i][0] == pdbAbbrev:
                        pdbTitle = str(dbs[i][1])
                        break
        db = Client['PhysioNet']
        if db.list_collection_names().__contains__(pdbAbbrev):
                print('dataset already exsists')
                return False
        if not physio_db_exists(pdbAbbrev):
                print('dataset does not exist')
                return
        pdbDesc = "curse you and your lack of uniform formatting physionet"
        db = Client["PhysioNet"]
        pdb = db[pdbAbbrev]
        post = {
                "Database Title": pdbTitle,
                "_id": pdbAbbrev,
                "Description": physio_db_desc(pdbAbbrev),
                "Webpage": "https://physionet.org/content/" + pdbAbbrev + "/1.0.0/",
                "Zip Link": physio_db_zip(pdbAbbrev)
                }
        post_id = pdb.insert_one(post).inserted_id
        post_id
        
def physio_db_exists(pdbAbbrev):
        URL = "https://physionet.org/content/" + pdbAbbrev + "/1.0.0/"
        resp = requests.get(URL)
        if resp.status_code == 200:
                return True
        else:
                return False

# will have to manually put in the description, author for 5
# change it to webscrape for the zip url still possible tho
@app.route('/zipfile')
def physio_db_zip():
    # ".zip link": "https://physionet.org <+<breaks here>+> /static/published-projects/adfecgdb/abdominal-and-direct-fetal-ecg-database-1.0.0.zip" no spaces ofc
    pdbAbbrev = 'aami-ec13'
    URL = "https://physionet.org/content/" + pdbAbbrev + "/1.0.0/"
    resp = requests.get(URL)
    if resp.status_code==200:
        soup = BeautifulSoup(resp.text,'html.parser') 
        abs_neck = soup.find("h5", text="Access the files")  
        abs_head = abs_neck.findNext("ul",{"class":""})
        z = str(abs_head.find_next())
        zip_ext = z[13:-41]
        zippy = "https://physionet.org" + zip_ext
        print(zippy)
        return zippy
    else:
        print('no zip link')
        return "error"

def physio_db_desc(pdbAbbrev):
        if pdbAbbrev == 'aami-ec13':
                desc = "desc"
                return desc
        if pdbAbbrev == 'bpssrat':
                desc = "rat"
                return desc
        return 'no desc'

def request_physio_zip(pdbAbbrev):
        db = Client["PhysioNet"]
        pdb = db[pdbAbbrev]
        if db.list_collection_names().__contains__(pdbAbbrev):
                zip_link = pdb.find_one({"_id": pdbAbbrev})
                zip = zip_link["Zip Link"]
                print(zip)
                return True
        else:
                print('dataset not exists')
                return False

# below downloads individual files to computer, idk if really needed tho
# needs to be called in if __name__ == "__main__": function or it will time out and be stuck in loop forever
def download_physio_db(): # (pdbAbbrev): the abbreviation for the physioDatabase, might have to redo as it downloads not send as zip atm
        print('wfdb for physionet .dat files and metadata')
        wfdb.io.get_dbs()
        wfdb.get_record_list('bpssrat')
        wfdb.dl_database('bpssrat', r'C:\Users\User\Desktop\bpsrat-DATA', records='all', annotators='all', keep_subdirs=True, overwrite=False)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")
    
@app.route('/projectpage')
def sayHi():
        print('say hi')
        return 'Hello!'

# add_base_hwset()
# *********** TESTING WITH INPUTS REMOVE BELOW
# print(db.list_collection_names())
# if not make_user('alberto', 'pass'):
#         check_user_password('alberto', 'pass')
# if __name__ == "__main__":
#         download_physio_db()
# add_physio_db('aami-ec13')
# add_physio_db('bpssrat')
# add_physio_db('wrongwrongwrong') # meant to fail
# add_physio_db('adfecgdb')
# add_physio_db('aftdb')
# add_physio_db('norwegian-athlete-ecg')
# request_physio_zip('aami-ec13')
# request_physio_zip('bpssrat')
# request_physio_zip('adfecgdb')
# request_physio_zip('aftdb')
# request_physio_zip("norwegian-athlete-ecg")
# add_project()
# log_out()
# if not make_user('alberto2', 'pass2'):
#         check_user_password('alberto2', 'pass2')
# add_project()
# join_project()
# check_out_hw()
# check_in_hw()
# print('make next project ID is delete no spaces')
# delete_project()
# add_custom_hwset()
# log_out()
# *********** END OF MANUAL TEST DONT REMOVE STUFF PAST HERE

# Client.close()
if __name__ == '__main__':
    app.run()
# TODO
# encrypt password (HW1) cypher
# get info from ui 
# lock user info behind password 
# physio??? 5 sets, have link to download in mongodb