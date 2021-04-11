# from email.utils import parseaddr

from flask import Flask, render_template, request

from send_mail import send_mail

import re

app = Flask(__name__)

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']
        if subject == '' or body == '' or recipient == '':
            return render_template('index.html', message='You cannot leave any field blank!')
        if(not(re.search(regex, recipient))):
            return render_template('index.html', message='Please enter a valid email address in the recipient field!')
        send_mail(recipient, subject, body)
        return render_template('success.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
