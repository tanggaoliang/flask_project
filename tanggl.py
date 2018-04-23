from flask import Flask, config, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


app.config.from_object(config)
if __name__ == '__main__':
    app.run()
