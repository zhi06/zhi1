import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()




from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>謝仁翔Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=謝仁翔>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>仁翔簡介網頁</a><br>"
    homepage += "<a href=/about>帳號密碼</a><br>"
    homepage += "<a href=/about>圖書精選</a><br>"
    return homepage


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")
@app.route("/addbooks")
def addbooks():
    result = ""
    
    collection_ref = db.collection("圖書精選")    
    docs = collection_ref.order_by("anniversary",direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        bk = doc.to_dict()
        result += "書名：<a href+" + bk["url"] + ">" + bk["tittle"]+"</a><br>"    
        result += "書名::" + bk["author"]+"<br>"
        result += str(bk["anniversary"])"周年紀念版<br>"
        result += "<img src =" + bk["cover"] + "></imp><br><br>"
    return result


if __name__ == "__main__":
    app.run(debug=Ture)