from flask import *
import pyrebase 

config = {
    "apiKey": "AIzaSyCEqjoN_ZdtCp3Wrl0SSwHLrfNg4fXtsN4",
    "authDomain": "chat-app-6c77f.firebaseapp.com",
    "databaseURL": "https://chat-app-6c77f-default-rtdb.firebaseio.com",
    "projectId": "chat-app-6c77f",
    "storageBucket": "chat-app-6c77f.appspot.com",
    "messagingSenderId": "635626355779",
    "appId": "1:635626355779:web:b605d30daed0081d6c28f6",
    "measurementId": "G-3QD83KGP85"
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()

app = Flask(__name__)

@app.route('/')
def entry_point():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
        global username
        username=request.form['username']
        return render_template('chat.html', text='{}'.format("Send something to View others msg") ,user='{}'.format(username))

@app.route('/send', methods=['POST'])
def send():
    if request.method=='POST':
        msg=request.form['msg']
        hi=username
        space=" : "
        db.child("messages").push(username+space+msg)
        data=db.child("messages").get()
        output=data.val()
        return render_template('chat.html', t=output.values(), user='{}'.format(hi))

if __name__== '__main__':
    app.run()