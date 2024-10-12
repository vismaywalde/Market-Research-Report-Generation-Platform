# app.py

from flask import Flask, render_template, request
from marketresearch.data_fetcher import get_market_data_from_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This renders the form for user input

@app.route('/generate_report', methods=['POST'])
def generate_report():
    query = request.form['query']  # Get the search query from the form input
    market_data = get_market_data_from_search(query)  # Scrape data based on the query

    if market_data:
        # Process the data and render the report
        return render_template('report.html', market_data=market_data)
    else:
        return "Failed to retrieve data", 500

if __name__ == '__main__':
    app.run(debug=True)
