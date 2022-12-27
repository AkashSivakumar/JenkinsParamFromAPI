from flask import Flask, request

app = Flask(__name__)
data = {
    'items':[
        {
            'name':'com/android/version/3.0.2/get'
        },
        {
            'name':'com/android/version/3.0.1/get'
        },
        {
            'name':'com/android/version/2.0.7/get'
        },
        {
            'name':'com/android/version/3.0.8/get'
        },
        {
            'name':'com/android/version/3.0.9/get'
        },
        {
            'name':'com/android/version/3.1.2/get'
        },
        {
            'name':'com/android/version/3.2.9/get'
        },
        {
            'name':'com/android/version/3.2.8/get'
        },
        {
            'name':'com/android/version/3.2.7/get'
        },
        {
            'name':'com/android/version/3.2.6/get'
        },
    ]
}
data_test = {
    'items':[
        {
            'name':'com/android/version/5.6.7/get'
        },
        {
            'name':'com/android/version/3.4.5/get'
        },
        {
            'name':'com/android/version/1.1.2/get'
        },
        {
            'name':'com/android/version/4.0.8/get'
        }
    ]
}


@app.route('/dev', methods=['GET'])
def get_query_string():
    return data
@app.route('/test', methods=['GET'])
def get_query_string_test():
    return data_test
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')