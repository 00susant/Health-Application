<<<<<<< HEAD
from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route("/")

@app.route("/cancer")
def cancer():
    return render_template(r"index.html")


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=7640)
    #app.run_server(mode="external", host="localhost", port=7647, debug=True)
=======
from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route("/")

@app.route("/cancer")
def cancer():
    return render_template(r"index.html")


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=7640)
    #app.run_server(mode="external", host="localhost", port=7647, debug=True)
>>>>>>> c1a3a2d6300b395045ceee9a72c2397e80a6024a
