# Data-Cleaning-Transformation-using-Python-Libraries

Project Report: Data Cleansing and Transformation for Payment Transactions for an E-Commerce Platform
Introduction:
This project focuses on cleaning and transforming a payment transaction dataset for analysis. The dataset includes transaction details such as amounts, dates, payment providers, and customer data. Key steps included handling missing values, converting data types, removing duplicates, and standardizing text. Insights on transaction patterns, top cities by volume, total revenue, and trends over time were extracted.
Objective:
•	Clean the dataset by resolving missing values, standardizing text, and converting data types.
•	Derive insights like top-performing cities, total revenue, and transaction trends.
Steps and Methodology:
1.	Data Loading and Inspection:
The dataset was loaded and inspected for missing values, data types, and structure.
2.	Handling Missing Values:
Missing values in Discount were replaced with 0, and the median value was used for missing Shipping entries.
3.	Data Cleaning:
o	Type Conversion: Amount was converted to numeric and Time & Date to datetime.
o	Text Standardization: The City column was standardized to title case.
o	Duplicate Removal: Duplicate rows were identified and removed.
4.	Post-Cleaning Validation:
The dataset was rechecked to confirm all issues were resolved.
Insights:
1.	Top 5 Cities with Most Transactions:
Cities like Bengaluru, Mumbai, and Delhi had the highest transaction volumes.
2.	Total Revenue Generated:
Total revenue from all transactions was calculated.
3.	Most Common Payment Provider:
The most frequently used payment provider was identified.
4.	Transaction Trend Over Time:
Transaction patterns showed fluctuations likely tied to sales periods or promotions.
Conclusion:
The dataset was successfully cleansed and transformed, making it ready for advanced analysis. Key insights into transaction patterns, revenue, and customer preferences were derived, offering valuable business intelligence.
