from flask import Flask, render_template, request, jsonify
from db import create_db, connect, add_email

EMAIL_ADDRESS = 'mackaycameron8@gmail.com'
EMAIL_PASSWORD = 'your_email_password'

app = Flask(__name__)

@app.route('/send-text', methods=['POST'])
def receive_text():
    data = request.get_json()
    received_text = data.get('text')
    print(received_text)

    add_email(received_text)
    # Process the text or perform any desired actions
    
    response_data = {'message': 'Text received successfully'}
    return jsonify(response_data)

@app.route('/', methods=['GET','POST'])
def submit():
    if request.method == "POST":
        value = request.form.get("sbox")
        print(value)
        add_email(value)

    return render_template('index.html')


@app.route('/')
def home():
    connect()
    return submit()

if __name__ == '__main__':
   app.run(debug=True)