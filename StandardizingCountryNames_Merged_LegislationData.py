# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:40:08 2023

@author: amyfo
"""

import pandas as pd

# Load Datasets
 df1 = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\datasets\Merged_Dataset_with_All_CTDC_Data.csv')
 df2 = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Requested Table Data from WorldPopulationReview.com\countries-where-prostitution-is-legal-2023.csv')
 

# Verify column names in df2
print(df2.columns)

# Convert the relevant columns to sets
countries_df1 = set(df1['CountryOfExploitation'].dropna().unique())
countries_df2 = set(df2['country'].dropna().unique())

# Find common elements
common_countries = countries_df1.intersection(countries_df2)

# Find elements that are only in df1 and not in df2
only_in_df1 = countries_df1 - countries_df2

# Find elements that are only in df2 and not in df1
only_in_df2 = countries_df2 - countries_df1

# Print the results
print("Common Countries:", common_countries)
print("Only in df1:", only_in_df1)
print("Only in df2:", only_in_df2)

