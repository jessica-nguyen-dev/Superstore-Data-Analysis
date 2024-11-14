# Superstore Data Analysis Web App

An interactive web application built with Flask and Pandas that enables users to filter and analyze Superstore data by various categories, regions, and segments. Users can run pre-defined queries to generate insights on sales, profit, and discounts.

## Overview

This project utilizes:
- **Flask**: For web application development.
- **Pandas**: For data manipulation and analysis.
- **HTML/CSS**: For creating the user interface.

The application allows users to:
- Filter data from the Superstore dataset based on Category, Sub-Category, Region, and Segment.
- Run pre-defined queries to display insights such as total sales, profit, and discount information.

## Features

- **Filter Options**: Users can filter data by Category, Sub-Category, Region, and Segment through a user-friendly form.
- **Pre-Defined Queries**:
  - **Total Sales and Profit**: Sum of Sales and Profit for filtered data.
  - **Average Discount by Product**: Average discount for each product in the filtered subset, sorted in descending order.
  - **Total Sales by Year**: Grouped by Year with total sales calculated.
  - **Profit by Region**: Grouped by Region with total profit calculated.
  - **Products with Negative Profit**: Displays products with negative profit in the filtered subset.
- **Dynamic Data Display**: Displays query results on the same page with clear formatting for easy readability.

## Getting Started

### Prerequisites

- **Python 3.6+**
- **Libraries**: Install required libraries by running: pip install flask pandas

## Installation

1. **Clone the repository**: git clone https://github.com/jessica-nguyen-dev/Superstore-Data-Analysis.git
                             cd Superstore-Data-Analysis
2. **Prepare the Dataset**: Place the superstore_sales.csv file in the data/ folder.

## Running the Application

1. **Start the Flask server:**: python app.py
2. Open your web browser and go to http://127.0.0.1:5000 to interact with the application.
