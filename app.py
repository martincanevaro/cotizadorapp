from flask import Flask, jsonify,request,Response
from flask_cors import CORS
import json
import requests
app = Flask(__name__)
CORS(app)

@app.route('/cotizacion/dolar',methods=['GET'])
def cotizacionDolar():			
	moneda="dolar"
	precio=apicotizacion("USD")
	return jsonify( {
    	"moneda": moneda,"precio":precio
    })
@app.route('/cotizacion/euro',methods=['GET'])
def cotizacionEuro():			
	moneda="euro"
	precio=apicotizacion("EUR")
	return jsonify( {
    	"moneda": moneda,"precio":precio
    })
@app.route('/cotizacion/real',methods=['GET'])
def cotizacionReal():			
	moneda="real"
	precio=apicotizacion("BRL")
	return jsonify( {
    	"moneda": moneda,"precio":precio
    })
def apicotizacion(divisa):
	key="6265|XTCEQd6Zb78ahZKQ4d4AuMHisuU0hnXg"
	url="https://api.cambio.today/v1/quotes/"+divisa+"/ARS/json?quantity=1&key="+key
	response=requests.get(url)
	if response.status_code==200:
		response_json=response.json()
		result=response_json['result']
		value=result['value']
		value=str(value)
		return(value)

if __name__=='__main__':
	app.run(debug=True, port=5000)
	