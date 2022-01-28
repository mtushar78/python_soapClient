import zeep
import json

wsdl = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls?wsdl'
client = zeep.Client(wsdl=wsdl)
i = {'name':'Tushar',
    'age':34}
print(type(i))

def findPerson( id ):
    wsdl2 = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls?wsdl'
    client2 = zeep.Client(wsdl2)
    info = client2.service.FindPerson(id)
    json = zeep.helpers.serialize_object(info, dict)
    print(json)

    return json