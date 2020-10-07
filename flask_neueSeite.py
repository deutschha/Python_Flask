from flask import Flask

app = Flask(__name__)

@app.route("/")

def neueSeite():
    html = """<html>
        <body>
        <p>Bitte Namen eingeben</p>
        <p> Bitte Adresse eingeben</p>
        </body>"""
    return html

if __name__ == "__main__":
    app.run(port=1337,debug = True)
