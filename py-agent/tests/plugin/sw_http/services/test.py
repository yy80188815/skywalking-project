import time

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == "GET":
        print("GET")
        time.sleep(500)
        return "11111"
    else:
        print('POST')
        # id = request.form['ID']
        # message = db.get_data(id)
        # for i in message:
        #     print(i)
        return "222222"


if __name__ == '__main__':
    app.run(debug=True)
