import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# Fetch the service account key JSON file contents
path_to_key = "/Users/williamlee/Desktop/CS411/Firebase/cs411-e12c0-firebase-adminsdk-z7icf-dbfcf166c2.json"
cred = credentials.Certificate(path_to_key)
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://cs411-e12c0-default-rtdb.firebaseio.com/"
})


ref = db.reference("/history")
name = "will"
events_data = [1, 2]
#push and get
if str(name) in ref.get().keys():
        history = {}
        history[current_time]=events_data
        ref = db.reference("/history/"+str(name))
        ref.update(history)
    
else:
    history = {}
    history[str(name)]={}
    history[str(name)][current_time] = events_data
    ref = db.reference("/history")
    ref.update(history)

