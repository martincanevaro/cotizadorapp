from flask import Flask, jsonify,request,Response
import json
import requests
app = Flask(__name__)

app.config.from_pyfile('config.cfg')


@app.route('/cotizacion/dolar',methods=['GET'])
def cotizacionDolar():			
	moneda="dolar"
	precio=apiDolar()
	return jsonify( {
    	"moneda": moneda,"precio":precio
    })
@app.route('/cotizacion/euro',methods=['GET'])
def cotizacionEuro():			
	moneda="euro"
	precio=apiEuro()
	return jsonify( {
    	"moneda": moneda,"precio":precio
    })
@app.route('/cotizacion/real',methods=['GET'])
def cotizacionReal():			
	moneda="real"
	precio=apiReal()
	return jsonify( {
    	"moneda": moneda,"precio":precio
    })
def apiDolar():
	url="https://api.cambio.today/v1/quotes/USD/ARS/json?quantity=1&key=6265|XTCEQd6Zb78ahZKQ4d4AuMHisuU0hnXg"
	response=requests.get(url)
	if response.status_code==200:
		response_json=response.json()
		result=response_json['result']
		value=result['value']
		value=str(value)
		return(value)
def apiReal():
	url="https://api.cambio.today/v1/quotes/BRL/ARS/json?quantity=1&key=6265|XTCEQd6Zb78ahZKQ4d4AuMHisuU0hnXg"
	response=requests.get(url)
	if response.status_code==200:
		response_json=response.json()
		result=response_json['result']
		value=result['value']
		value=str(value)
		return(value)
def apiEuro():
	url="https://api.cambio.today/v1/quotes/EUR/ARS/json?quantity=1&key=6265|XTCEQd6Zb78ahZKQ4d4AuMHisuU0hnXg"
	response=requests.get(url)
	if response.status_code==200:
		response_json=response.json()
		result=response_json['result']
		value=result['value']
		value=str(value)
		return(value)

if __name__=='__main__':
	app.run(debug=True, port=5000)
	