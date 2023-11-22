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
    homepage += "<a href=/addbooks>圖書精選</a><br>"
    homepage += "<br><a href=/spider>網路爬蟲抓取子青老師課程</a><br>"
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
@app.route("/spider")
def spider():
    url = "https://www1.pu.edu.tw/~tcyang/course.html"
    Data = requests.get(url)
    Data.encoding = "utf-8"
    sp = BeautifulSoup(Data.text,"html.parser")
    result=sp.select(".team-box")
    info = ""
    for x in result:
        info += "<a href=" + x.find("a").get("href") + ">" + x.text +"</a><br>"
        info += x.find("a").get("href") + "<br><br>"
    return info
    return render_template("spider.py")


#if __name__ == "__main__":
 #   app.run(debug=True)