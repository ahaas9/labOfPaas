from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello finalists this is a PaaS Practical Session!"

if __name__ == "__main__":
    app.run()
