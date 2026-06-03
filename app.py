from flask import Flask
from organizer import organize_files

app = Flask(__name__)

@app.route('/')

def home():

    organize_files("uploads")

    return "Files Organized Successfully 😁🔥"

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
