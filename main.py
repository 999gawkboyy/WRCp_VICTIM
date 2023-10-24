import subprocess, socket, datetime as dt
from firebase_admin import db, credentials
import firebase_admin

def get_desktop_name():
    try:
        desktop_name = socket.gethostname()
        return desktop_name
    except socket.error as e:
        return f"Error: {e}"
desktop_name = get_desktop_name()

cred = credentials.Certificate("./wrcp-pwd.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://wrcp-14e73-default-rtdb.firebaseio.com/'
})
ref = db.reference(f'/{desktop_name}') 
new_data = {"mouse": {"x":f"1234/{dt.datetime.now()}", "y":f"123/{dt.datetime.now()}","isCick":f"True/{dt.datetime.now()}"}}
ref.set(new_data)

