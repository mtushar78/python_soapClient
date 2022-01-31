
from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
import gevent.pywsgi
import zeep
import index as i

auth = HTTPBasicAuth()

app = Flask(__name__)

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
    print("requested Value: ",x["a"])
    wsdl2 = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls?wsdl'
    client2 = zeep.Client(wsdl2)
    info = client2.service.FindPerson(1)


    # print("returned_val: ", returned_val)
    # final_return = make_response()
    return info



@app.route('/', methods = ['GET'])
def index_test(): 
    response =i.getToken()
    print (response)
    return make_response(response,203)
# if __name__ == '__main__':
#     app.run(debug=True)

app_server = gevent.pywsgi.WSGIServer(("0.0.0.0", 4000), app)
app_server.serve_forever()