from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


def get_sys_procs():
    import psutil
    procList=0
    for proc in psutil.process_iter():
        procList+=1
    return procList


def get_sys_mem():
    import psutil
    free=psutil.virtual_memory().free / 1024 / 1024
    return free



@cross_origin()
@app.route('/info',methods=['GET','OPTIONS'])
def get_sys_info():
    import datetime
    response = jsonify({'currentTime' : datetime.datetime.now(),'proc' : get_sys_procs(), 'mem': get_sys_mem()})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)