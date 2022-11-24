from flask import Flask, render_template
import modules.dinstation

app = Flask(__name__)


@app.route('/')
def hello():
    return 'pendler-statistik'


@app.route('/trains')
def trains():
    trains = modules.dinstation.get_trains("HH")
    return render_template('trains.html', trains=trains)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
