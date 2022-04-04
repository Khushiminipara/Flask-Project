from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "This is a small demo application of flask framework. Made by 20CS019, 20CS022,20CS036"
if __name__=="__main__":
    app.run(debug=True)

