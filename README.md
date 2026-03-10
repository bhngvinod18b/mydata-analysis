# Mobile Finance Approval Analysis 📊

## Project Overview

This project analyzes mobile phone finance applications to understand approval rates, rejection reasons, product demand, and sales executive performance. The analysis helps identify patterns in customer approvals and the main factors causing finance rejection.

The dataset contains information about customers applying for mobile phone financing, including product details, price, sales executive, approval status, and rejection reasons.

## Objectives

* Analyze approval vs rejection rates
* Identify the most common rejection reasons
* Find the highest demand mobile products
* Evaluate sales executive performance
* Understand price distribution of financed products

## Dataset Information

The dataset includes the following columns:

* **Date** – Application date
* **Customer Name** – Name of the applicant
* **Product** – Mobile phone model
* **Price** – Price of the mobile phone
* **Executive Name** – Sales executive handling the application
* **Phone Number** – Customer contact number
* **Application ID** – Finance application reference
* **Final Status** – Approved or Rejected
* **Reject Reason** – Reason for rejection (if rejected)

## Tools & Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Excel
* Jupyter Notebook / Python Script

## Data Analysis Process

### 1. Data Cleaning

* Removed empty columns
* Checked missing values
* Prepared the dataset for analysis

### 2. Exploratory Data Analysis (EDA)

The following analysis was performed:

* Approval vs Rejection analysis
* Rejection reason analysis
* Sales executive performance
* Product demand analysis
* Price distribution analysis

### 3. Visualization

Visualizations were created using **Seaborn** and **Matplotlib** including:

* Approval vs Rejection count plot
* Rejection reasons chart
* Executive performance chart
* Product demand chart
* Price vs number of sales

## Key Insights

* Most finance applications were **rejected** compared to approvals.
* The most common rejection reasons include **low CIBIL score and negative area**.
* Some mobile models such as **Apple and Note series** have higher demand.
* Certain sales executives handle more applications than others.

## Project Structure

```
Mobile-Finance-Analysis
│
├── data
│   └── vnv1.xlsx
│
├── analysis
│   └── analysis.py
│
├── visuals
│   └── charts
│
└── README.md
```

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/mobile-finance-analysis.git
```

2. Install required libraries

```
pip install pandas matplotlib seaborn
```

3. Run the Python script

```
python analysis.py
```

## Future Improvements

* Build an interactive dashboard using **Power BI or Tableau**
* Add more advanced analytics
* Include monthly sales trend analysis
* Predict approval probability using machine learning

## Author

Data Analysis Project created for learning and portfolio purposes.
