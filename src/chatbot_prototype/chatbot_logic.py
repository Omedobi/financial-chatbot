import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

# Load the dataset
final_report = pd.read_json(r'../dataset/Final_report/10k_final_report.json')
summary_report = pd.read_json(r'../dataset/Final_report/10k_summary_report.json')

# Create a function for querying the dataset
def query_financial_data(dataset, filters, column_name):
    """
    Queries a dataset with specified filters and returns the value of a specific column.

    Parameters:
    dataset (pd.DataFrame): The dataset to query.
    filters (dict): A dictionary of column-value pairs for filtering.
    column_name (str): The column to retrieve the value from.

    Returns:
    str: The queried value.
    """
    try:
        for key, value in filters.items():
            dataset = dataset[dataset[key] == value]
        return dataset[column_name].values[0]
    except IndexError:
        return "Data not found for the specified filters."

# Create a function for the chatbot logic
def financial_chatbot(company_input, fiscal_year, user_query):
    try:
        if user_query == "what is the total revenue?":
            revenue = query_financial_data(final_report, 
                                           {'Year': fiscal_year, 'Company': company_input}, 
                                           'Total_revenue')
            return f"The Total revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
        
        elif user_query == 'what is the Net income':
            net_income = query_financial_data(final_report, 
                                              {'Year': fiscal_year, 'Company': company_input}, 
                                              'Net_income')
            return f"The Net income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
        
        elif user_query == 'what is the sum of the total assets?':
            total_assets = query_financial_data(final_report, 
                                                {'Year': fiscal_year, 'Company': company_input}, 
                                                'Total_assets')
            return f"The sum of the Total assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets}"
        
        elif user_query == 'what is the sum of the total liabilities?':
            total_liabilities = query_financial_data(final_report, 
                                                     {'Year': fiscal_year, 'Company': company_input}, 
                                                     'Total_liabilities')
            return f"The sum of the Total liabilities for {company_input} for fiscal year {fiscal_year} is $ {total_liabilities}"
        
        elif user_query == 'what is the cash flow from operation activities?':
            cash_ops_flow = query_financial_data(final_report, 
                                                 {'Year': fiscal_year, 'Company': company_input}, 
                                                 'Cash_flow_from_operating_activities')
            return f"The Cash flow from operation activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops_flow}"
        
        elif user_query == 'what is the revenue growth %?':
            revenue_growth = query_financial_data(final_report, 
                                                  {'Year': fiscal_year, 'Company': company_input}, 
                                                  'Revenue_growth_(%)')
            return f"The Revenue growth % for {company_input} for fiscal year {fiscal_year} is {round(revenue_growth, 3)}(%)"
        
        elif user_query == "what is the profit margin?":
            revenue = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Total_revenue')
            net_income = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Net_income')
            profit_margin = (net_income / revenue) * 100
            return f"The Profit Margin for {company_input} in fiscal year {fiscal_year} is {profit_margin:.2f}%"
        
        elif user_query == "what is the debt-to-assets ratio?":
            liabilities = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Total_liabilities')
            assets = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Total_assets')
            debt_to_assets = (liabilities / assets) * 100
            return f"The Debt-to-Assets Ratio for {company_input} in fiscal year {fiscal_year} is {debt_to_assets:.2f}%"
        
        elif user_query == "which company had the highest revenue?":
            max_revenue_row = final_report[final_report['Year'] == fiscal_year].sort_values(by='Total_revenue', ascending=False).iloc[0]
            company = max_revenue_row['Company']
            revenue = max_revenue_row['Total_revenue']
            return f"{company} had the highest revenue of $ {revenue} in fiscal year {fiscal_year}"
        
        elif user_query == "which company had the highest net income?":
            max_net_income_row = final_report[final_report['Year'] == fiscal_year].sort_values(by='Net_income', ascending=False).iloc[0]
            company = max_net_income_row['Company']
            net_income = max_net_income_row['Net_income']
            return f"{company} had the highest net income of $ {net_income} in fiscal year {fiscal_year}"
        
        elif user_query == "summarize the financial performance":
            revenue = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Total_revenue')
            net_income = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Net_income')
            assets = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Total_assets')
            liabilities = query_financial_data(final_report, {'Year': fiscal_year, 'Company': company_input}, 'Total_liabilities')
            return (f"Financial Summary for {company_input} in fiscal year {fiscal_year}:\n"
                    f"- Total Revenue: $ {revenue}\n"
                    f"- Net Income: $ {net_income}\n"
                    f"- Total Assets: $ {assets}\n"
                    f"- Total Liabilities: $ {liabilities}")
        
        else:
            return "Sorry, I cannot provide information on the requested question."
        
    except Exception as e:
        return f"An error occurred: {e}"

# Interactive chatbot session
def interactive_chatbot():
    """
    Interactive session for the chatbot, allowing users to query financial data.
    """
    print("\nWelcome to the AI-Driven Financial Chatbot!")
    print("How can I assist you in your Financial question.\n")
    
    while True:
        print("-----------------------------------------------------------------")
        print("Enter 'exit' at any time to quit.")
        
        # Get company input
        company_input = input("Enter company name (Microsoft, Tesla, Apple): ").capitalize()
        if company_input.lower() == 'exit':
            print("Goodbye!")
            break
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid company name. Please try again.")
            continue
        
        # Get fiscal year input
        try:
            fiscal_year = int(input("Enter fiscal year (2020-2024): "))
            if fiscal_year not in [2020, 2021, 2022, 2023, 2024]:
                print("Invalid fiscal year. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid fiscal year.")
            continue
        
        # Query loop
        while True:
            print("\nYou can ask questions like:")
            print("- What is the total revenue?")
            print("- What is the net income?")
            print("- What is the profit margin?")
            print("- What is the debt-to-assets ratio?")
            print("- Which company had the highest revenue?")
            print("- what is the revenue growth %?")
            print("- what is the cash flow from operation activities?")
            print("- what is the sum of the total liabilities?")
            print("- what is the sum of the total assets?")
            print("- what is the sum of the total assets?")
            print("- which company had the highest net income?")
            print("- Summarize the financial performance")
            print("Enter 'back' to select a different company or fiscal year.")
            
            user_query = input("\nPlease enter your question: ").strip().lower()
            if user_query in ['exit' , 'quit']:
                print("Goodbye!")
                return
            if user_query == 'back':
                break
            
            # Process the query
            response = financial_chatbot(company_input, fiscal_year, user_query)
            print(response)

# Start the chatbot
interactive_chatbot()