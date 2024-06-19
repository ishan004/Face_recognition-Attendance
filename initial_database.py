import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "Your Firebase Database URl ",
    "storageBucket": "Firebase storage bucker"
   
    },
)

ref = db.reference(
    "Employee"
)  # reference path to our database... will create student directory in the database

data = {
    "01": {  # id of student which is a key
        "id": "01",
        "name": "Ishan Bhusal",
        "password": "01ishan",
        "dob": "2001-04-11",
        "address": "Khairahani, chitwan",
        "phone": "9865040555",
        "email": "ishanbhusal004@gmail.com",
        "role": "Python Developer",
        "starting_year": 2024,
        "total_attendance": 4,
        "year": 2,
        "last_attendance_time": "2024-05-22 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
