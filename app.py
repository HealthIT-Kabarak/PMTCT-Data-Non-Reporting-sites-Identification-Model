from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the data into a Pandas DataFrame
data = pd.read_csv('HTS_TST-KSM.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    county = request.form.get('county')
    period = request.form.get('period')

    # Filter the data based on the user's search criteria
    results = data[(data['county'] == county) & (data['period'] == period)]

    # Pass the results, county, and period variables to the results.html template
    return render_template('results.html', results=results, county=county, period=period)


""" @app.route('/results', methods=['POST'])
def results():
    county = request.form.get('county')
    period = request.form.get('period')

    # Filter the data based on the user's search criteria
    results = data[(data['county'] == county) & (data['period'] == period)]

    return render_template('results.html', results=results) """

    
if __name__ == '__main__':
    app.run()
