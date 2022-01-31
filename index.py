import zeep
import json

def getToken():
    wsdl2 = 'https://trx.dev.brifast.co.id/Webservice/brifastService?wsdl'
    client2 = zeep.Client(wsdl2)
    parameters = {
             'username':'nblws',
             'password': 'ra8h!w0c2a4iphEsPeSw',
             'counterpart':'NBL',
             'ipAddress':'127.0.0.1'
            }
    info = client2.service.requestToken(parameters)
    json = zeep.helpers.serialize_object(info, dict)
    return json
