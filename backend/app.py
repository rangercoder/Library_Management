from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello World")
    return "Hello World! whatsup members"

if __name__ == "__main__":
    app.run()