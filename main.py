from flask import Flask
from flask import request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calendar():
        if "NBR DE MISSION AUJOUD’HUI" in request.form:
            pass
        elif "NBR DE MISSION A VENIR" in request.form:
            pass
        return render_template("calendar.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
