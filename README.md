# Sales Data Analysis Project

## Overview
This project is a Python-based sales data analysis project built in phases.  
In Phase 1, the project focuses on loading sales data from a CSV file, cleaning the data, removing duplicates, calculating basic KPIs, identifying top products and customers, and visualizing monthly sales trends.

## Features
- Load sales data from CSV.
- Clean and preprocess data.
- Remove duplicate records.
- Calculate key performance indicators:
  - Total Sales
  - Total Orders
  - Average Order Value
- Identify top 10 products by sales.
- Identify top 10 customers by sales.
- Analyze monthly sales trends.
- Generate charts using Matplotlib.

## Project Structure
```text
sales-analysis/
├── data/
│   └── sales_data.csv
├── notebook/
│   └── sales_analysis.ipynb
├── charts/
├── main.py
├── requirements.txt
└── README.md
```

## Dataset
The dataset used in this project is a sample sales dataset stored in the `data/` folder.  
It contains columns such as:
- order_id
- order_date
- region
- product_name
- category
- quantity
- sales
- customer_name
- customer_id

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit

## How to Run
### For Jupyter Notebook
1. Open the notebook in Jupyter.
2. Run all cells one by one.

### For Streamlit App
1. Install the required libraries:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
streamlit run main.py
```

## Files Description
- `data/sales_data.csv` → Raw sales data.
- `notebook/sales_analysis.ipynb` → Notebook for analysis.
- `charts/` → Saved chart images.
- `main.py` → Streamlit app file.
- `requirements.txt` → Required Python libraries.

## Future Improvements
- Add advanced sales insights.
- Include profit analysis.
- Add state-wise and category-wise performance.
- Create an interactive dashboard.
- Deploy the app online.

## Author
Created as a sales data analysis project.
