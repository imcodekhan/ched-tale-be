from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from urllib.parse import unquote


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World imcodekhan's flask poc!</p>"


@app.route('/get_recipe', methods=['GET'])
def get_recipe():

    encoded_name = request.args.get('name')
    decoded_name = unquote(encoded_name)

    api_url = f'https://api.api-ninjas.com/v1/cocktail?name={decoded_name}'

    headers = {'X-Api-Key': 'CrS2iY/YTkrMZhLFr6MfDw==IgDCZTN3N94nEaIN'}
    response = requests.get(api_url, headers=headers)

    if response.ok:
        responseData = response.json()
    else:
        responseData = {'status_code': response.status_code,
                        'message': response.text}

    return jsonify(responseData)
