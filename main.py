
from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
import gevent.pywsgi
from flask_swagger_ui import get_swaggerui_blueprint
import zeep
import index as i

auth = HTTPBasicAuth()

app = Flask(__name__)
# flask swagger configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Todo List API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@auth.get_password
def get_password(username):
    if username == 'api_mid':
        return '123456789'
    return None

@auth.error_handler
def unauthorized():
    return (jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/', methods = ['POST'])
@auth.login_required
def index():
    x = request.get_json()
    response =i.findPerson(x["value"])
    print (response)
    return make_response(response,200)




@app.route('/', methods = ['GET'])

def index_test(): 
    response =i.findPerson(1)
    print (response)
    return make_response(response,203)
# if __name__ == '__main__':
#     app.run(debug=True)

app_server = gevent.pywsgi.WSGIServer(("0.0.0.0", 4000), app)
app_server.serve_forever()