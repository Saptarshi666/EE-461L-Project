from asyncio.windows_events import NULL
# from crypt import methods
from datetime import date
from http import client
import json
from operator import contains
from pickle import FALSE
from sqlite3 import Date
from unittest import result
from matplotlib.pyplot import title
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
# from flask_cors import CORS
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
project_id = ''
auth = FALSE
app = Flask(__name__, static_folder='./frontend/build', static_url_path="")
# CORS(app)
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
        if db.list_collection_names().__contains__('HWSet1') and db.list_collection_names().__contains__('HWSet2'):
                return
        set = db['HWSet1']
        post = {
                "HWSet Name": "HWSet1",
                "Capacity": 100,
                "Availability": 100
                }
        post_id = set.insert_one(post).inserted_id
        post_id
        set = db['HWSet2']
        post = {
                "HWSet Name": "HWSet2",
                "Capacity": 100,
                "Availability": 100
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
def get_availability():
        params = request.get_json()
        print(params)
        setName = params['setName']
        print(type(setName))
        print(setName)
        db = Client['HWSets']
        set = db[setName]
        avail_temp = set.find_one({"HWSet Name": setName}, {"_id": 0, "Availability": 1})
        avail = avail_temp["Availability"]
        print(avail)
        return jsonify({'result' : avail})

@app.route("/HWManagement1", methods=["GET", "POST"])
def check_out_hw(): # (projID, setName, number):
        params = request.get_json()
        print(params)
        projID, amount, setName = params['projID'].strip(), params['amount'].strip(), params['setName'].strip()
        print(type(setName))
        amount = int(amount)
        print(type(amount))
        # TODO what to do about logging out with sets forever?
        # any user can check in the checked out hw for a project, and ofc can check out more if available
        # hw set not like a library book
        # change returns to be availability
        db = Client['Projects']
        proj = db[projID]
        print(db.list_collection_names())
        print(proj)
        if not db.list_collection_names().__contains__(projID):
                print('proj not exists')
                return jsonify(result = "noprojerror")
        db = Client['HWSets']
        set = db[setName]
        print(db.list_collection_names())
        print(setName)
        if not db.list_collection_names().__contains__(setName):
                print('hwset not exists')
                return jsonify(result = "noseterror")
        avail_temp = set.find_one({"HWSet Name": setName}, {"_id": 0, "Availability": 1})
        avail = avail_temp["Availability"]
        if avail == 0:
                print('no sets currently available')
                return jsonify(result = "noneavailable")
        if amount > avail:
                print('not enough available to match your request')
                amount = avail
        set.update_one({"HWSet Name": setName}, {'$inc':{'Availability': -amount}})

        db = Client['Projects']
        proj = db[projID]
        proj.find_one_and_update({"_id": projID}, {"$inc":{setName: amount}})
        avail_temp = set.find_one({"HWSet Name": setName}, {"_id": 0, "Availability": 1})
        avail = avail_temp["Availability"]
        return jsonify(result = avail)

@app.route("/HWManagement2", methods=["GET", "POST"])
def check_in_hw(): # (setName, number):
        # change returns to be availability
        print('chkin')
        params = request.get_json()
        print(params)
        projID, amount, setName = params['projID'].strip(), params['amount'].strip(), params['setName'].strip()
        print(type(setName))
        amount=int(amount)
        db = Client['Projects']
        proj = db[projID]
        
        db = Client['Projects']
        proj = db[projID]
        print(db.list_collection_names())
        print(proj)
        if not db.list_collection_names().__contains__(projID):
                print('proj not exists')
                return jsonify(result = "noprojerror")
        chkout = proj.find_one({"_id": projID}, {"_id": 0, setName: 1})
        chkout = chkout[setName]
        print(type(chkout))
        print(chkout)
        if amount > chkout:
                print('this is more than you have checked out, try again')
                return jsonify(result = "toomany")

        proj.update_one({"_id": projID}, {'$inc':{setName: -amount}})
        db = Client['HWSets']
        set = db[setName]
        set.update_one({"HWSet Name": setName}, {'$inc':{'Availability': amount}})
        avail_temp = set.find_one({"HWSet Name": setName}, {"_id": 0, "Availability": 1})
        avail = avail_temp["Availability"]
        return jsonify(result = avail)

@app.route("/projectHW", methods=["GET", "POST"])
def get_proj_HW():
        print('get proj hw')
        params = request.get_json()
        print(params)
        projID = params['projID']
        print(type(projID))
        db = Client['Projects']
        proj = db[projID]
        print(db.list_collection_names())
        print(proj)
        if not db.list_collection_names().__contains__(projID):
                print('proj not exists')
                return jsonify(result = "noprojerror")
        db = Client['Projects']
        proj = db[projID]
        proj.find({"_id": projID})
        avail_temp = proj.find_one({"_id": projID})
        set1 = avail_temp["HWSet1"]
        set2= avail_temp["HWSet2"]
        print(set1)
        print(set2)
        print(type(set1))
        return jsonify(result = set1, set1 = set1, set2 = set2)

# *********** for checking how global current_user works *******************************8
@app.route("/sayHi", methods=["GET", "POST"])
def sayHi():
        return 'Hello there '+ current_user # jsonify(result = "True")

@app.route("/projectpage", methods=["GET", "POST"])
def add_project(): # (,projName, desc, auth):
        # TODO remove inputs
        # maybe make a method to pull name from project db based on if user has the corresponding projID attatched to their acct
        # so that it can always be displayed
        # either this or, as i did in delete_project(), simply add name to each projDoc in its members and update name, desc if its ever changed etc.
        global project_id
        print('add project')
        params = request.get_json()
        print(params)
        projName, projDesc, projID = params['projName'].strip(), params['projDesc'].strip(), params['projID'].strip()
        print(type(projName))
        # change below so that unique projects names only apply to individual users. is it even necessary if differing ID's and Descs? prob not
        # db = Client['Users']
        # user = db[current_user]
        # if user.find_one({"_id": projID}):
        #         print('project name already in use')
        #         return jsonify(result = "False")
        db = Client['Projects']
        project = db[projName]
        if db.list_collection_names().__contains__(projID):
                print('project already exists')
                return jsonify(result = "False")
        post = {
                "Project Name": projName,
                "Description": projDesc,
                "_id": projID,
                "HWSet1": 0,
                "HWSet2": 0
                }
        # consider removing the user push, instead only pushing project ID
        project_id = projID
        project = db[projID]
        post_id = project.insert_one(post).inserted_id
        post_id
        # db = Client['Users']
        # user = db[current_user]
        # user.insert_one({"_id": projID})
        return jsonify(result = "True")

@app.route('/projectpage1', methods=["GET", "POST"])
def join_project(): # (projID):
        global project_id
        params = request.get_json()
        print(params)
        projID = params['projID'].strip()
        print(type(projID))

        db = Client['Projects']
        if not db.list_collection_names().__contains__(projID):
                print('project not exists')
                return jsonify(result = "False")
        project_id = projID
        print(project_id)
        # project.find_one_and_update({"Project ID": projID}, {"$addToSet": {"Members": current_user}})
        # db = Client['Users']
        # user = db[current_user]
        # user.insert_one({"_id": projID})
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
        # TODO remove INPUTS when receiving data from front end
        # check for strength of pw? maybe for the future
        # add encryption
        params = request.get_json()
        username, password = params['username'].strip(), params['password'].strip()

        db = Client['Users']
        if db.list_collection_names().__contains__(username):
                print('username unavailable')
                return jsonify({'result' :"false"})
        token = f.encrypt(username.encode())
        token2 = f.encrypt(password.encode())
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
        # Client=MongoClient("mongodb+srv://ajstiles:caWpDYgtyCH0Z1JU@cluster0.fvy1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return jsonify(result = "True")

@app.route('/login', methods=["GET", "POST"])
def check_user_password():
        # TODO add reverse encryption
        # add limit on attempts? attempts per user or machine?
        params = request.get_json()
        username, password = params['username'].strip(), params['password'].strip()
        db = Client['Users']
        user = db[username]
        if not db.list_collection_names().__contains__(username):
                print("no such user exists")
                avail = 0
                return jsonify({"result": avail})
        enc_user = user.find_one()
        enc_username = enc_user["Username"]
        dec_username = f.decrypt(enc_username).decode()
        enc_password = enc_user["Password"]
        dec_password = f.decrypt(enc_password).decode()
        if username != dec_username or password != dec_password:
                print("login credentials incorrect")
                avail = 0
                return jsonify({"result": avail})
        else:
                print('Welcome ' + username + ' !')
                global current_user
                current_user = username
                # Client=MongoClient("mongodb+srv://ajstiles:caWpDYgtyCH0Z1JU@cluster0.fvy1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        return jsonify({"result": username})

@app.route('/logout', methods=["GET", "POST"])
def log_out():
        # add tracker of checkouts to mass checkin upon logout
        global current_user
        global Client
        print("goodbye")
        current_user = ''
        # Client.close()
        return jsonify(result = "True")

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
        # file sizwdztw creatwd, channels
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
        zip_ext = z.split('"')[1::2]
        zip_ext = zip_ext[0]
        print(zip_ext)
        zippy = "https://physionet.org" + zip_ext
        print(zippy)
        return zippy
    else:
        print('no zip link')
        return "error"

def physio_db_desc(pdbAbbrev):
        if pdbAbbrev == 'aami-ec13':
                desc = "The files in this set can be used for testing a variety of devices that monitor the electrocardiogram. The recordings include both synthetic and real waveforms. "
                return desc
        if pdbAbbrev == 'bpssrat':
                desc = "Salt-sensitive hypertension is known to be associated with dysfunction of the baroreflex control system in the Dahl salt-sensitive (SS) rat. However, neither the physiological mechanisms nor the genomic regions underlying the baroreflex dysfunction seen in this rat model are definitively known. Here, we have adopted a mathematical modeling approach to investigate the physiological and genetic origins of baroreflex dysfunction in the Dahl SS rat. We have developed a computational model of the overall baroreflex heart rate control system based on known physiological mechanisms to analyze telemetry-based blood pressure and heart rate data from two genetic strains of rat, the SS and consomic SS.13BN, on low- and high-salt diets. With this approach, physiological parameters are estimated, unmeasured physiological variables related to the baroreflex control system are predicted, and differences in these quantities between the two strains of rat on low- and high-salt diets are detected. Specific findings include: a significant selective impairment in sympathetic gain with high-salt diet in SS rats and a protection from this impairment in SS.13BN rats, elevated sympathetic and parasympathetic offsets with high-salt diet in both strains, and an elevated sympathetic tone with high-salt diet in SS but not SS.13BN rats. In conclusion, we have associated several important physiological parameters of the baroreflex control system with chromosome 13 and have begun to identify possible physiological mechanisms underlying baroreflex impairment and hypertension in the Dahl SS rat that may be further explored in future experimental and modeling-based investigation."
                return desc
        if pdbAbbrev == 'adfecgdb':
                desc = "The research material included in the Abdominal and Direct Fetal Electrocardiogram Database contains multichannel fetal electrocardiogram (FECG) recordings obtained from 5 different women in labor, between 38 and 41 weeks of gestation. The recordings were acquired in the Department of Obstetrics at the Medical University of Silesia, by means of the KOMPOREL system for acquisition and analysis of fetal electrocardiogram (ITAM Institute, Zabrze, Poland). Each recording comprises four differential signals acquired from maternal abdomen and the reference direct fetal electrocardiogram registered from the fetal head."
                return desc
        if pdbAbbrev == 'aftdb':
                desc = "This database of two-channel ECG recordings has been created for use in the Computers in Cardiology Challenge 2004, an open competition with the goal of developing automated methods for predicting spontaneous termination of atrial fibrillation (AF). "
                return desc
        if pdbAbbrev == 'norwegian-athlete-ecg':
                desc = "The Norwegian Endurance Athlete ECG Database contains 12-lead ECG recordings from 28 elite athletes from various sports in Norway. All recordings are 10 seconds resting ECGs recorded with a General Electric (GE) MAC VUE 360 electrocardiograph. All ECGs are interpreted with both the GE Marquette SL12 algorithm (version 23 (v243)) and one cardiologist with training in interpretation of athlete's ECG. The data was collected at the University of Oslo in February and March 2020."
                return desc
        return 'no desc'


@app.route('/zipfile', methods=["GET", "POST"])
def request_physio_zip():
        print('getzip')
        params = request.get_json()
        print(params)
        pdbAbbrev = params['_id'].strip()
        print(type(pdbAbbrev))
        print(pdbAbbrev)
        db = Client["PhysioNet"]
        pdb = db[pdbAbbrev]
        if db.list_collection_names().__contains__(pdbAbbrev):
                zip_link = pdb.find_one({"_id": pdbAbbrev})
                zip = zip_link["Zip Link"]
                title = zip_link["Database Title"]
                desc = zip_link["Description"]
                print(zip)
                return jsonify(result = zip, title = title, desc = desc)
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
    app.run(host="0.0.0.0")