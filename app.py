import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'chatbot_app')))
import pandas as pd
from flask import Flask, render_template, request
from chatbot_logic import financial_chatbot


app = Flask(__name__, template_folder='chatbot_app/templates', static_folder='chatbot_app/static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get user input from the form
        company_input = request.form['company'].capitalize()
        fiscal_year = int(request.form['year'])
        user_query = request.form['query'].lower()
        

        # Process the query using the chatbot logic
        response = financial_chatbot(company_input, fiscal_year, user_query)
        return {'response': response}
    
    except ValueError as ve:
        return {"error": f"Please enter a numeric value: {ve}"}
    
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

if __name__ == '__main__':
    app.run()
