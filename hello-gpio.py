from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
# print(__name__)
@app.route("/")
def hello():
    now=datetime.datetime.now()
    time=now.strftime("%Y-%m-%d %H:%M")
    templateData={
        'title':"안녕하세요!",
        'time':time
    }
    return render_template('main.html',**templateData)

@app.route("/<pin>")
def readPin():
    try:
        GPIO.setup(int(pin),GPIO.IN)
        if GPIO.input(int(pin))==True:
            response="핀넘버"+pin+"은 HIGH"
        else:
            response="핀넘버"+pin+"은 LOW"
    except:
        response="핀을 읽는데 문제가 있음"+pin+"번 핀"
    templateData={
        'pin':"핀상태"+pin,
        'response':response
    }            
    return render_template('pin.html',**templateData)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)