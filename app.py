
# A very simple Flask  app for you to get started with...

from flask import Flask
from datetime import datetime
from flask import jsonify
import urllib2
import cookielib
from nltk.corpus import words
import yaml
import random,requests
app = Flask(__name__)


def send_msg(text,number1,username,passwd):
    message = text
    number = number1


    message = "+".join(message.split(' '))

    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        print "error"

    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"

@app.route('/')
def hello_world():
    return "hello"

@app.route('/api/<data>', methods=['GET','POST'])
def get_task(data):
    data = data.split("+")
    text= data[3]
    snd_number=data[2]
    username = data[0]
    passwd = data[1]
    try:
        send_msg(text,snd_number,username,passwd)
        return "sent"
    except:
        return "could not be processed"
    #return jsonify(data)

