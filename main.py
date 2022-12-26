from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_query_string():
    param = request.query_string
    return 'FromPythonAPI YourQueryParamIs: ' + str(param,"utf-8")
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')