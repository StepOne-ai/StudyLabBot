import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Path to your service account key file
cred = credentials.Certificate('creds.json')

# Initialize the Firebase app with your credentials
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Example: Read data from a collection
# docs = db.collection('users').stream()
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

# Example: Write data to a collection
def push(data: dict, collection: str) -> bool:
    try:
        db.collection(collection).document().set(data);
        return True
    except:
        return False

def get_all(collection: str) -> None:
    return db.collection(collection).stream()