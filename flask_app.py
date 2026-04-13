from flask import Flask, render_template
app = Flask(__name__)
if __name__ == "__main__":
    app.run(port=5000, debug=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prijzen")
def prijzen():
    return "Binnenkort verschijnen hier onze actuele prijzen"

@app.route("/recepten")
def recepten():
    return "Binnenkort verschijnen hier enkele recepten"


