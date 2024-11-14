from flask import Flask, render_template, request
import pandas as pd

# openpyxl allows Pandas to read Excel data and retrieve the company's sales information.
# This keeps the data's original format, which is better than changing it to a CSV file, in order to prevent corruption.
app = Flask(__name__)
df = pd.read_excel('data/TableauSalesData.xlsx', engine='openpyxl')

# Ensure the 'Order Date' column is converted to datetime to get the Year column
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get unique values for dropdowns
    categories = df['Category'].unique()
    subcategories = df['Sub-Category'].unique()
    regions = df['Region'].unique()
    segments = df['Segment'].unique()

    # Set the default result (an empty value)
    query_result = None

    # According to ChatGPT, a POST request means that the form was submitted. Therefore, if request.method == 'POST':
    # will process the form's data when a POST request is submitted (i.e., when the user clicks 'Submit').

    if request.method == 'POST':
        # Retrieves the values submitted by the user or assigns an empty string if no category was selected or provided
        category = request.form.get('category', '')
        subcategory = request.form.get('subcategory', '')
        region = request.form.get('region', '')
        segment = request.form.get('segment', '')
        query_type = request.form.get('query_type', '')

        # Start with the entire dataset and apply filters based on the users' specifications
        filtered_df = df.copy()
        if category:
            filtered_df = filtered_df[filtered_df['Category'] == category]
        if subcategory:
            filtered_df = filtered_df[filtered_df['Sub-Category'] == subcategory]
        if region:
            filtered_df = filtered_df[filtered_df['Region'] == region]
        if segment:
            filtered_df = filtered_df[filtered_df['Segment'] == segment]

        # Execute the selected query
        if query_type == 'total_sales_profit':
            query_result = filtered_df[['Sales', 'Profit']].sum()
        elif query_type == 'avg_discount_by_product':
            query_result = filtered_df.groupby('Product Name')['Discount'].mean().sort_values(ascending=False)
        elif query_type == 'total_sales_by_year':
            query_result = filtered_df.groupby('Year')['Sales'].sum()
            query_result = query_result.reset_index()   # The Year columns would not output correctly unless I put in this line.
            query_result['Year'] = query_result['Year'].astype(str)  # This line ensures that users see 2021 and not 2021.0.
        elif query_type == 'profit_by_region':
            query_result = filtered_df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
        elif query_type == 'negative_profit_products':
            query_result = (filtered_df[filtered_df['Profit'] < 0].groupby('Product Name', as_index=False)['Profit']
            .sum().sort_values(by='Profit'))

    # The following code snippet is from ChatGPT. This statement ensures that the result is always a DataFrame (even if
    # it’s a Series). We need it to be a dataframe so that we can pass the data into a table later on.

        if isinstance(query_result, pd.Series):
            query_result = query_result.reset_index()  # Convert Series to DataFrame


# According to ChatGPT, Flask's render_template function takes an HTML template file ('index.html') and uses it to
# create the final HTML output for the user. It also passes the required variables to the HTML template to display the
# queries' final result. Important: this line is ONLY for displaying the form options and query results on the page!!

    return render_template(
        'index.html',
        categories=categories,
        subcategories=subcategories,
        regions=regions,
        segments=segments,
        query_result=query_result
    )

# Suggested by ChatGPT; This block starts the Flask application when the script is run directly, which saves time and
# makes it a little bit easier to test the application. Note: it is also possible to run the application by typing
# "flask run" into the terminal.

if __name__ == '__main__':
    app.run(debug=True)
