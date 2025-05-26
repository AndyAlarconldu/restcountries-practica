from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/countries')
def get_countries():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        data = response.json()
        countries = [{
            'name': c.get('name', {}).get('common'),
            'capital': c.get('capital', ['N/A'])[0],
            'region': c.get('region')
        } for c in data]
        return jsonify(countries)
    return jsonify({'error': 'No se pudo obtener los países'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')