# Sales Data Analysis Project

## Overview
This project analyzes sales data using Python's pandas and matplotlib libraries to extract insights and create visualizations. It's part of the PLP Python Assignment for Week 7.

## Project Structure
```
week7/
├── sales_data_sample.csv          # Raw sales dataset (2,823 records, 25 columns)
├── sales_analysis_notebook.ipynb   # Complete Jupyter notebook with analysis & visualizations
└── README.md                       # Project documentation
```

## Dataset Description
The `sales_data_sample.csv` contains sales transaction data with the following key columns:
- **ORDERNUMBER**: Unique order identifier
- **QUANTITYORDERED**: Number of items ordered
- **PRICEEACH**: Price per item
- **SALES**: Total sales amount
- **ORDERDATE**: Date of the order
- **PRODUCTLINE**: Product category (Motorcycles, Classic Cars, etc.)
- **COUNTRY**: Customer country
- **DEALSIZE**: Deal size category (Small, Medium, Large)

## Requirements
```
pandas
matplotlib
seaborn
numpy
jupyter (for notebook)
```

## Installation
1. Clone or download the project files
2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn numpy jupyter
   ```

## Usage

### Option 1: Jupyter Notebook (Recommended)
1. Open terminal in the project directory
2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open `sales_analysis_notebook.ipynb`
4. Run all cells to see the complete analysis

### Option 2: View Analysis Results
1. Open the Jupyter notebook to see pre-executed analysis results
2. All visualizations are embedded within the notebook
3. No separate Python script is needed - everything is in the notebook

## Analysis Features

### 1. Data Loading & Exploration
- Automatic encoding detection for CSV files
- Dataset structure analysis
- Missing value identification and handling
- Data type conversion (dates, categories)

### 2. Basic Data Analysis
- Summary statistics for numerical columns
- Sales performance by product line
- Geographic sales distribution
- Temporal sales trends
- Deal size analysis

### 3. Data Visualizations
**Main Dashboard (2x2 Grid):**
- **Line Chart**: Monthly sales trends over time with trend analysis
- **Horizontal Bar Chart**: Total sales by product line comparison
- **Histogram**: Sales amount distribution with mean/median indicators
- **Scatter Plot**: Quantity ordered vs. price relationship with correlation

**Additional Visualizations:**
- **Pie Chart**: Sales distribution by deal size (Small/Medium/Large)
- **Bar Chart**: Top 10 customers by total sales revenue

## Key Insights
The analysis reveals:
- Sales performance across different product categories
- Seasonal trends in sales data
- Geographic distribution of customers
- Relationship between quantity ordered and pricing
- Deal size patterns and their impact on revenue

## Technical Implementation
- **Data Cleaning**: Handles missing values and data type conversions
- **Error Handling**: Robust encoding detection for international characters
- **Visualization**: Professional charts with proper styling and labels
- **Documentation**: Comprehensive comments and markdown explanations

## Output Files
- All visualizations are embedded within the Jupyter notebook
- Interactive analysis results displayed in notebook cells
- Statistical summaries and key findings documented in markdown cells
- No separate image files - everything is contained in the notebook

## Assignment Requirements Met
✅ **Data Loading**: Successfully loaded 2,823 sales records with encoding detection  
✅ **Data Exploration**: Complete dataset structure analysis and missing value handling  
✅ **Basic Analysis**: Summary statistics, grouping, and pattern identification  
✅ **Four Required Visualizations**: Line chart, bar chart, histogram, scatter plot  
✅ **Additional Visualizations**: Pie chart and top customers analysis  
✅ **Data Cleaning**: Robust preprocessing with datetime conversion  
✅ **Documentation**: Comprehensive README and notebook documentation  
✅ **Jupyter Notebook**: Complete analysis in interactive format  

## Author
PLP Python Assignment - Week 7

## License
This project is for educational purposes as part of the PLP curriculum.