from matplotlib.pyplot import title
import youtube
from flask import Flask, request as rq, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    search = rq.args.get("search")
    if search:
        len1, hasil = youtube.search(search)
        len2 = "video found : " + str(len1)
        bg = "https://en.esportsku.com/wp-content/uploads/2021/01/ganyu.jpg"
    else:
        len2, hasil, bg = ("", "", "")
    return render_template("index.html", search=hasil, len2=len2, bg=bg, title=search)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80)