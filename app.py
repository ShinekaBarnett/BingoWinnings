from flask import Flask, redirect, url_for, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="Testing") 

if __name__ == "__main__":
    app.run(debug=True)