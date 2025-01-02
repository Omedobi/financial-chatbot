import sys
import os
from flask import Flask, render_template, request
from chatbot_logic import financial_chatbot


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get user input from the form
    company_input = request.form['company'].capitalize()
    fiscal_year = int(request.form['year'])
    user_query = request.form['query'].lower()

    # Process the query using the chatbot logic
    response = financial_chatbot(company_input, fiscal_year, user_query)
    return {'response': response}


if __name__ == '__main__':
    app.run(debug=True)