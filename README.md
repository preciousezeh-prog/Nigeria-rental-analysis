# Nigeria Rental Market Analysis

This project analyzes rental property data in Nigeria using Python. The objective is to understand how rental prices vary across locations and property features, and to demonstrate practical data analysis skills using real-world data.

## Tools Used in this Project
- Python
- pandas
- matplotlib

## Dataset
The dataset contains over 200,000 property listings with the following features:
- Location
- Price
- Date Added
- Bedrooms
- Bathrooms
- Toilets
- House Type

## Project Structure 
- data/ - raw dataset  
- outputs/ - cleaned data, charts, and summary tables  
- analysis.py - main analysis script  

## Data Preparation
The dataset was cleaned to ensure consistency and reliability:
- Converted date fields into proper format  
- Removed unrealistic price values  
- Filtered out extreme or invalid entries in bedrooms, bathrooms, and toilets  

## Analysis Performed in the Project
The project explores:
- Median rental prices across different locations  
- Relationship between rent and number of bedrooms  
- Price differences across house types  

Median values were used instead of averages to reduce the effect of outliers.

## Key Insights
- High-demand areas consistently show significantly higher rental prices  
- Rental prices increase with the number of bedrooms, though not always proportionally  
- Property type plays a role in pricing, with certain categories commanding higher rents  

## How to Run
1. Install dependencies:
   ```bash
   python3 -m pip install pandas matplotlib
