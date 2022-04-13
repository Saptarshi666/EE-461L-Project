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
current_user = ''
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

@app.route("/HWManagement", methods=["GET", "POST"])
def check_out_hw(): # (projID, setName, number):
        params = request.get_json()
        print(params)
        setName, number, projID = params['HWSet Name'].strip(), params['Availability'].strip(), params['projID'].strip()
        print(type(setName))
        # TODO what to do about logging out with sets forever?
        # any user can check in the checked out hw for a project, and ofc can check out more if available
        # hw set not like a library book
        db = Client['HWSets']
        set = db[setName]
        if not set.find_one({"HWSet Name": setName}):
                print('hwset not exists')
                return jsonify(result = "False")
        avail_temp = set.find_one({"HWSet Name": setName}, {"_id": 0, "Availability": 1})
        avail = avail_temp["Availability"]
        if avail == 0:
                print('no sets currently available')
                return jsonify(result = "False")
        if number > avail:
                print('not enough available to match your request')
                number = avail
        set.update_one({"HWSet Name": setName}, {'$inc':{'Availability': -number}})
        db = Client['Projects']
        proj = db[projID]
        if not proj.find_one({"HWSet Name": setName}):
                proj.insert_one({"HWSet Name": setName, "Current Out": number})
                return jsonify(result = "True")
        else:
                proj.find_one_and_update({"HWSet Name": setName}, {"$inc":{"Current Out": number}})
                return jsonify(result = "True")

@app.route("/HWManagement", methods=["GET", "POST"])
def check_in_hw(): # (setName, number):
        params = request.get_json()
        print(params)
        setName, number, projID = params['HWSet Name'].strip(), params['Availability'].strip(), params['projID'].strip()
        print(type(setName))
        db = Client['Projects']
        proj = db[projID]
        if not proj.find_one({"HWSet Name": setName}):
                print('hwset not checked out')
                return jsonify(result = "False")
        out_temp = proj.find_one({"HWSet Name": setName}, {"_id": 0, "Current Out": 1})
        current_Out = out_temp["Current Out"]
        if number > current_Out:
                print('this is more than you have checked out, try again')
                return jsonify(result = "False")
        proj.update_one({"HWSet Name": setName}, {'$inc':{'Current Out': -number}})
        out_temp = proj.find_one({"HWSet Name": setName}, {"_id": 0, "Current Out": 1})
        current_Out = out_temp["Current Out"]
        if current_Out == 0:
                print('all units of this set checked back in')
                proj.find_one_and_delete({"HWSet Name": setName})
        db = Client['HWSets']
        set = db[setName]
        set.update_one({"HWSet Name": setName}, {'$inc':{'Availability': number}})
        return jsonify(result = "True")

# *********** for checking how global current_user works *******************************8
@app.route("/sayHi", methods=["GET", "POST"])
def sayHi():
        return 'Hello there '+ current_user # jsonify(result = "True")

@app.route("/NewProj", methods=["GET", "POST"])
def add_project(): # (,projName, desc, auth):
        # TODO remove inputs
        # maybe make a method to pull name from project db based on if user has the corresponding projID attatched to their acct
        # so that it can always be displayed
        # either this or, as i did in delete_project(), simply add name to each projDoc in its members and update name, desc if its ever changed etc.
        params = request.get_json()
        print(params)
        projName, projDesc, projID, funds = params['projName'].strip(), params['projDesc'].strip(), params['projID'].strip(), params['funds'].strip()
        print(type(projName))
        # change below so that unique projects names only apply to individual users. is it even necessary if differing ID's and Descs? prob not
        # db = Client['Users']
        # user = db[current_user]
        # if user.find_one({"_id": projID}):
        #         print('project name already in use')
        #         return jsonify(result = "False")
        db = Client['Projects']
        project = db[projName]
        if project.find_one({"Project ID": projID}):
                print('project already exists')
                return jsonify(result = "False")
        post = {
                "Project Name": projName,
                "Description": projDesc,
                "_id": projID,
                "Funds": funds,
                "Members": [current_user]
                }
        # consider removing the user push, instead only pushing project ID
        project = db[projID]
        post_id = project.insert_one(post).inserted_id
        post_id
        db = Client['Users']
        user = db[current_user]
        user.insert_one({"_id": projID})
        return jsonify(result = "True")

@app.route('/ExistingProject/<user>', methods=["GET", "POST"])
def join_project(): # (projID):
        params = request.get_json()
        print(params)
        projID = params['projID'].strip()
        print(type(projID))
        db = Client['Users']
        user = db[current_user]
        if user.find_one({"_id": projID}):
                print('project already joined')
                return jsonify(result = "False")
        db = Client['Projects']
        project = db[projID]
        if not project.find_one({"Project ID": projID}):
                print('project not exists')
                return jsonify(result = "False")
        project.find_one_and_update({"Project ID": projID}, {"$addToSet": {"Members": current_user}})
        db = Client['Users']
        user = db[current_user]
        user.insert_one({"_id": projID})
        return jsonify(result = "True")

def edit_project(): #(projID):
        # dont know if we want this yet, basically can only edit title and desc anyway
        # maybe true owner can kick users or add them manually? true owner is [0] in users array in the project docu
        print('idk if we doing this')
        # user.find_one_and_update({"Project ID": projID}, {"$set": {"Description": 'new desc'}}) 

def delete_project(): # (projID):
        projID = input('delete project id- ')
        db = Client['Users']
        user = db[current_user]
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
        global current_user
        current_user = username
        return jsonify(result = "True")

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
                global current_user
                current_user = username
        return jsonify(result = "True")

def log_out():
        # add tracker of checkouts to mass checkin upon logout
        global current_user
        current_user = ''

# PhysioNet Citation:
# Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.
# @app.route("/PublicDatasets", methods=["GET", "POST"])
# can just run this as initialization with 5 predetermined set abbreviations, doesn't really need user input
def add_physio_db(pdbAbbrev): # (pdbAbbrev, pdbDesc): 
        # small sizes are aami-ec13, bpssrat, need 3 more
        # TODO no duplicates
        # TODO add descriptions
        # maybe add counter for number of downloads?
        dbs = wfdb.get_dbs()
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
                return False
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
def physio_db_zip(pdbAbbrev):
    # ".zip link": "https://physionet.org <+<breaks here>+> /static/published-projects/adfecgdb/abdominal-and-direct-fetal-ecg-database-1.0.0.zip" no spaces ofc
    # pdbAbbrev = 'aami-ec13'
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
                desc = "yes desc"
                return desc
        if pdbAbbrev == 'bpssrat':
                desc = "rat"
                return desc
        return 'no desc'


@app.route('/zipfile')
def request_physio_zip():
        print(fernet)
        params = request.get_json()
        print(params)
        pdbAbbrev = params['_id'].strip()
        print(type(pdbAbbrev))
        db = Client["PhysioNet"]
        pdb = db[pdbAbbrev]
        if db.list_collection_names().__contains__(pdbAbbrev):
                zip_link = pdb.find_one({"_id": pdbAbbrev})
                zip = zip_link["Zip Link"]
                print(zip)
                return jsonify(result = "True")
        else:
                print('dataset not exists')
                return jsonify(result = "False")

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

add_base_hwset()
add_physio_db('aami-ec13')
add_physio_db('bpssrat')
add_physio_db('wrongwrongwrong') # meant to fail
add_physio_db('adfecgdb')
add_physio_db('aftdb')
add_physio_db('norwegian-athlete-ecg')
# log_out()
# Client.close()
if __name__ == '__main__':
    app.run()