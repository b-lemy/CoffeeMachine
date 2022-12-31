from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# Helps to tap in the frontend and make the document editable javascript
# document.body.contentEditable=true
