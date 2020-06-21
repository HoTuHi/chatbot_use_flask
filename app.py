from flask import Flask, render_template, request
# from sa import getfuntion
from shiftfuntion import corona, getsub, gettemp
flag = 0
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if "dich" in userText:
        contry = userText.split(" ")
        return "(•_•) " + corona(contry[-1])
    elif "num" in userText:
        number = userText.split(" ")
        return "( ´･･)ﾉ(._.`) " + getsub(number[-1])
    elif "temp" in userText:
        return "༼ つ ◕_◕ ༽つ  " + gettemp(userText)
    return "¯\\_(ツ)_/¯ Không hiểu gì hết"


if __name__ == "__main__":
    app.run()
