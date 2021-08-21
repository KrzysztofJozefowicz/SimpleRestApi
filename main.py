from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/info',methods=['GET','OPTIONS'])
def get_sys_info():
    import datetime
    response = jsonify({'currentTime' : datetime.datetime.now()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)