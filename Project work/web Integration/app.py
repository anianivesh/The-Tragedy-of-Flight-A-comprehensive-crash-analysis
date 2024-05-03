from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(".flasktemplate/index.html")

if __name__ == "__main__":
    app.run(debug = False, port = 5000)