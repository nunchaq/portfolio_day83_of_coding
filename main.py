from flask import Flask, render_template
import data
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    date = datetime.datetime.now()
    return render_template('index.html', data=data, year=date.year)


if __name__ == '__main__':
    app.run(debug=True)
