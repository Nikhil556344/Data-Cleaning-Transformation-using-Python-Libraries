
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading the dataset

dataset=pd.read_csv("C:\\Users\\nikhi\\OneDrive\\Desktop\\Github Projects\\Data Cleansing & Transformation\\Payment Transaction Dataset\\payments.csv")
#displaying basic information about the dataset

print(dataset.info())
print(dataset.head())

#Checking for missing values

print(dataset.isnull().sum())

print(dataset.dtypes)

#Data cleaninig
#filling missing values for discount with 0

dataset['Discount']=pd.to_numeric(dataset['Discount'],errors='coerce').fillna(0)

#filling missing shipping values with the median

dataset['Shipping']=dataset['Shipping'].fillna(dataset['Shipping'].median())

#Convert  categorical data to numerical data
dataset['Amount']=pd.to_numeric(dataset['Amount'],errors='coerce')

#convert time & date to datetime format
dataset['Time & Date']=pd.to_datetime(dataset['Time & Date'], format='%d/%m/%y%I:%M:%S %p', errors='coerce')
                                      
# Standardize city names
dataset['City'] = dataset['City'].str.title()

# Check for unique city names after standardization
print(dataset['City'].unique())

# Check for duplicates
duplicates = dataset.duplicated().sum()
print(f'Duplicates found: {duplicates}')

# Remove duplicates
dataset = dataset.drop_duplicates()

# Check for missing values after cleaning
print(dataset.isnull().sum())

# Check data types after cleaning
print(dataset.dtypes)

#Code for insights - Top  5 cities with most transactions

top_cities = dataset['City'].value_counts().head(5)
print("Top 5 Cities with Most Transactions:\n", top_cities)

# Plot the top cities
top_cities.plot(kind='bar')
plt.title('Top 5 Cities with Most Transactions')
plt.xlabel('City')
plt.ylabel('Number of Transactions')
plt.show()

#Total Revenue generated
total_revenue = dataset['Amount'].sum()
print(f'Total Revenue Generated: {total_revenue}')


#Most common payment provider

common_provider = dataset['Payment Provider'].value_counts().idxmax()
print(f'Most Common Payment Provider: {common_provider}')

#Transaction trend over time 

# Extract month and year from the 'Time & Date' column
dataset['Year-Month'] = dataset['Time & Date'].dt.to_period('M')

# Count the number of transactions per month
monthly_transactions = dataset.groupby('Year-Month')['Order ID'].count()

# Boxplot to visualize the spread of transaction amounts
plt.figure(figsize=(8, 6))
plt.boxplot(dataset['Amount'].dropna(), vert=False)
plt.title('Boxplot of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.tight_layout()
plt.show()

# Count the number of transactions per Payment Provider
payment_provider_count = dataset['Payment Provider'].value_counts()

# Plot the payment provider distribution
payment_provider_count.plot(kind='bar', figsize=(10, 6))
plt.title('Payment Provider Distribution')
plt.xlabel('Payment Provider')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
