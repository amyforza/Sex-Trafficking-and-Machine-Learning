# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:28:56 2023

@author: amyfo

Cleaning Merging and Filtering the CTDC Dataset

"""

#%%

# Add prostitution legislation from world population review to human trafficking data
# Normalize the country names from two data sets to match on a common column 

import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\CTDC_synthetic_20210825.csv')
df2 = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\World_Population_Review_Prostitution Legislation 160 Countries_2023.csv')

#'CountryofExploitation' from CTDC df and 'cca3' from World Pop df have the 'ISO3166-1-Alpha-3' country codes 

# Merging the dataframes on 'CountryofExploitation' and 'cca3'
# The 'how' parameter is set to 'outer' to ensure that all records from both dataframes are included
merged_df = pd.merge(df1, df2, left_on='CountryOfExploitation', right_on='cca3', how='outer')

# Save the merged dataframe to a new CSV file
merged_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\OutterJoin_bycca3andCountryOfExploitation_dataset.csv', index=False)




#%%%

# Find out which countries still don't have legislation data 
# Print all column names in the merged dataframe

# Check columns
print(merged_df.columns)

# Filter for countries that have no legislation model data
filtered_df = merged_df[merged_df['countriesWhereProstitutionIsLegal_model'].isna()]
unique_countries = filtered_df['CountryOfExploitation'].unique()

# Print unique countries
unique_countries

# Convert the array to a DataFrame
unique_countries_df = pd.DataFrame(unique_countries, columns=['UniqueCountries'])

# Save the dataFrame to a CSV file
unique_countries_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\unique_countries.csv', index=False)


#%%

'''

RESULTS

unique_countries
Out[5]: 
array([nan, 'TKL', 'MYS', 'TTO', 'SRB', 'BIH', 'SDN', 'MUS', 'GAB', 'VUT',
       'MRT', 'SVK', 'GIN', 'CUW', 'MNE', 'SVN'], dtype=object)

'''

#%%

# Convert country codes to country names
# Both datasets use the the "ISO3166-1-Alpha-3" naming convention 
# Reference country code Index "ISO3166-1-Alpha-3"

# Load the merged dataframe
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\OutterJoin_bycca3andCountryOfExploitation_dataset.csv', low_memory=False)

# Load the country codes dataframe
country_codes_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\country-codes.csv')


# Merge the 'official_name_en' column from the 'country_codes_df' DataFrame into 'merged_df'
# This is done by matching 'CountryOfExploitation' in 'merged_df' with 'ISO3166-1-Alpha-3' in 'country_codes_df'
# The merge is performed using a left join, which means all records from 'merged_df' will be retained
# If a match is found in 'country_codes_df', the 'official_name_en' is added to 'merged_df'
# If no match is found, the corresponding rows in 'merged_df' will have NaN in the 'official_name_en' column
merged_df = merged_df.merge(country_codes_df[['ISO3166-1-Alpha-3', 'official_name_en']], 
                            left_on='CountryOfExploitation', right_on='ISO3166-1-Alpha-3', 
                            how='left')


# Save the updated merged dataframe
merged_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\updatedwCountryNames_OutterJoin_bycca3andCountryOfExploitation.csv', index=False)


#%%

# Identify which countries still do not have legislation data

# Load merged dataframe
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\updatedwCountryNames_OutterJoin_bycca3andCountryOfExploitation.csv', low_memory=False)

# Filter for rows where 'countriesWhereProstitutionIsLegal_model' is NaN
no_prostitution_data_df = merged_df[merged_df['countriesWhereProstitutionIsLegal_model'].isna()]

# Get unique values from 'official_name_en'
unique_countries_no_prostitution_data = no_prostitution_data_df['official_name_en'].unique()

print(unique_countries_no_prostitution_data)

# Write countries with no legislation data to a csv

# Convert the list to a DataFrame
countries_no_legal_data_df = pd.DataFrame(unique_countries_no_prostitution_data, columns=['CountriesWithNoLegalData'])

# Save the DataFrame to a CSV file
countries_no_legal_data_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\countries_with_no_legal_data.csv', index=False)


#%%

'''

16 Countries from merged dataset have no legal model data. 

However, there is no cooresponding human trafficking data for most of these countries 
in the CTDC data. 

Therefore, we need to find which CTDC countries have no legal data.

'''

#%%

# Specify which 'CountriesOfExploitation' in the CTDC Data have no cooresponding legislation

import pandas as pd

# Load your merged dataframe
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\updatedwCountryNames_OutterJoin_bycca3andCountryOfExploitation.csv', low_memory=False)

# Filter for rows where 'countriesWhereProstitutionIsLegal_model' is NaN
Prostitution_LegalModel_NaN_df = merged_df[merged_df['countriesWhereProstitutionIsLegal_model'].isna()]

# Get unique values from the CTDC 'CountryOfExploitation' Column
No_CountryOfExploitation_LegalMatch = Prostitution_LegalModel_NaN_df['CountryOfExploitation'].unique()

print(No_CountryOfExploitation_LegalMatch)

# Write CTDC Countries with no Legal Data to DF List

# Convert the list to a DataFrame
No_CountryOfExploitation_LegalMatch = pd.DataFrame(No_CountryOfExploitation_LegalMatch, columns=['CTDCCountriesWithNoLegalMatch'])

# Save the DataFrame to a CSV file
No_CountryOfExploitation_LegalMatch.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\No_CountryOfExploitation_LegalMatch.csv', index=False)


#%%

# List is in ISO3166-1-Alpha-3 format
# Add the country names to this list

# Load the merged dataframe
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\updatedwCountryNames_OutterJoin_bycca3andCountryOfExploitation.csv', low_memory=False)

# Load the dataframe 'CountryOfExploitation' with no legal data
no_legal_match_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\No_CountryOfExploitation_LegalMatch.csv')

# Map country codes to names
country_name_map = merged_df.set_index('CountryOfExploitation')['official_name_en'].to_dict()
no_legal_match_df['CountryName'] = no_legal_match_df['CTDCCountriesWithNoLegalMatch'].map(country_name_map)

# Save the updated dataframe to a new CSV file
no_legal_match_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\No_CountryOfExploitation_LegalMatch_with_Names.csv', index=False)


#%%

'''
RESULTS

CTDCCountriesWithNoLegalMatch	CountryName
	
TKL	Tokelau
MYS	Malaysia
TTO	Trinidad and Tobago
SRB	Serbia
BIH	Bosnia and Herzegovina
SDN	Sudan
MUS	Mauritius
GAB	Gabon
VUT	Vanuatu
MRT	Mauritania
SVK	Slovakia
GIN	Guinea
CUW	CuraÃ§ao
MNE	Montenegro
SVN	Slovenia

Maually added missing legislation to 'No_CountryOfExploitation_LegalMatch_with_Names_and_Prostitution Legislation' csv

'''

#%%

# Add missing legislation to CTDC countries

import pandas as pd

# Load the datasets
no_legal_match_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\No_CountryOfExploitation_LegalMatch_with_Names_and_Prostitution Legislation.csv')
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\updatedwCountryNames_OutterJoin_bycca3andCountryOfExploitation.csv', low_memory=False)

# Create a dictionary from no_legal_match_df for mapping 'Prostitution Legislation' based on 'ISO3166-1-Alpha-3'
legislation_map = no_legal_match_df.set_index('ISO3166-1-Alpha-3')['Prostitution Legislation'].to_dict()

# Update 'countriesWhereProstitutionIsLegal_model' in merged_df using the legislation_map
merged_df['countriesWhereProstitutionIsLegal_model'] = merged_df['ISO3166-1-Alpha-3'].map(legislation_map).fillna(merged_df['countriesWhereProstitutionIsLegal_model'])

# Save the updated DataFrame
merged_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df.csv', index=False)


#%%

import pandas as pd

# Check to see if the legislation data is added
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df.csv')

# Define the ISO codes of interest
iso_codes_of_interest = [
    "TKL", "MYS", "TTO", "SRB", "BIH", "SDN", "MUS", "GAB",
    "VUT", "MRT", "SVK", "GIN", "CUW", "MNE", "SVN"
]

# Filter the dataframe for the given ISO codes
filtered_df = merged_df[merged_df['ISO3166-1-Alpha-3'].isin(iso_codes_of_interest)]

# Select only the columns of interest
selected_data = filtered_df[['ISO3166-1-Alpha-3', 'countriesWhereProstitutionIsLegal_model']]

# Print the selected data
print(selected_data)


#%%

# Print the unique code list for selected ISO Codes

merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df.csv')

# Define the ISO codes of interest
iso_codes_of_interest = [
    "TKL", "MYS", "TTO", "SRB", "BIH", "SDN", "MUS", "GAB",
    "VUT", "MRT", "SVK", "GIN", "CUW", "MNE", "SVN"
]

# Filter the dataframe for the given ISO codes
filtered_df = merged_df[merged_df['ISO3166-1-Alpha-3'].isin(iso_codes_of_interest)]

# Select only the relevant columns and remove duplicates
unique_legislation_data = filtered_df[['ISO3166-1-Alpha-3', 'countriesWhereProstitutionIsLegal_model']].drop_duplicates()

# Sort by the ISO code for better readability
unique_legislation_data_sorted = unique_legislation_data.sort_values('ISO3166-1-Alpha-3')

# Display the DataFrame
unique_legislation_data_sorted

#%%


# Now check all legslation by CTDC Countries

merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df.csv')

# Get the unique ISO codes and the corresponding prostitution legislation data
unique_legislation_data = merged_df.drop_duplicates(subset=['ISO3166-1-Alpha-3'])[['ISO3166-1-Alpha-3', 'countriesWhereProstitutionIsLegal_model']]

# Print the unique legislation data
print(unique_legislation_data.to_string(index=False))

# Count the number of unique countries (ISO codes)
num_unique_countries = unique_legislation_data['ISO3166-1-Alpha-3'].nunique()

#141 CTDC Countries with Legislation Data
num_unique_countries



#%%

# Standardize the prostitution legislation model by dropping countries with mixed Legislation
# List should only contain ['Abolitionism', 'Neo Abolitionism', 'Prohibitionism', 'Legalization', 'Decriminalization']
# List which countries do not conatin this specific legislation ['Abolitionism', 'Neo Abolitionism', 'Prohibitionism', 'Legalization', 'Decriminalization']

# Load the merged dataframe 
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df.csv')

# Define the specific legislation categories
specific_legislation = ['Abolitionism', 'Neo-Abolitionism', 'Prohibitionism', 'Legalization', 'Decriminalization']

# Filter out the countries that do not have the specified legislation
countries_without_specific_legislation = merged_df[
    ~merged_df['countriesWhereProstitutionIsLegal_model'].isin(specific_legislation)
]

# Get the unique official country names that do not have the specified legislation
unique_countries_without_specific_legislation = countries_without_specific_legislation['official_name_en'].unique()

# Output the list of countries
print(unique_countries_without_specific_legislation)


#%%

'''
RESULTS
['Sark' 'United States of America' 'Tokelau' 'Malaysia' 'Kenya' 'Nigeria'
 'Trinidad and Tobago' 'Serbia' 'Bosnia and Herzegovina' 'Sudan' 'Mexico'
 'Mauritius' 'Gabon' 'Vanuatu' 'Mauritania' 'Slovakia' 'Guinea'
 'El Salvador' 'Australia' 'Curaçao' 'Montenegro' 'Slovenia']

'''


#%%

# The United States is a "Prohibitionist" country 
# except for a few counties in only 1 of 50 states 
# so we will change the legislation to "Prohibitionist" 
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df.csv')

# Update 'countriesWhereProstitutionIsLegal_model' for 'United States of America'
merged_df.loc[merged_df['official_name_en'] == 'United States of America', 'countriesWhereProstitutionIsLegal_model'] = 'Prohibitionism'

# Save the updated dataframe back to the CSV
merged_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_Legislation.csv', index=False)



#%%

import pandas as pd

merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_Legislation.csv')

# Get the unique values in the 'countriesWhereProstitutionIsLegal_model' column
unique_models = merged_df['countriesWhereProstitutionIsLegal_model'].unique()

# Print the unique values
print("Unique values in 'countriesWhereProstitutionIsLegal_model':")
print(unique_models)

#%%

'''
['Prohibitionism' 'Legalization' 'Abolitionism' 'Decriminalization'
 
 'Neo-Abolitionism' 'Prohibitionism, Abolitionism'
 
 'Abolitionism/Prohibitionism' 'Legalization/Abolitionism/Prohibitionism'
 
 'Abolitionism/Prohibitionism/Legalization' 'Legalization/Prohibitionism']

'''
#%%

import pandas as pd

merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_Legislation.csv')


# List of specified legislation types
specified_legislation_types = [
    "Prohibitionism",
    "Abolitionism",
    "Neo-Abolitionism",
    "Decriminalization",
    "Legalization"
]


# Define the column name that contains official country names
country_column = 'official_name_en'

# Filter the DataFrame to find countries that do not have the specified legislation types
# This is done by checking if the 'countriesWhereProstitutionIsLegal_model' column does not contain any of the specified legislation types
countries_without_specified_legislation = merged_df[
    ~merged_df['countriesWhereProstitutionIsLegal_model'].isin(specified_legislation_types)
]


# Retrieve unique country names that do not have the specified legislation types
unique_countries = countries_without_specified_legislation[country_column].unique()

# Print the list of countries without the specified legislation types
print("Countries without specified legislation types:")
for country in unique_countries:
    print(country)


#%%

# Drop the countries that don't conform to the specific_legislation = ['Abolitionism', 'Neo-Abolitionism', 'Prohibitionism', 'Legalization', 'Decriminalization']

import pandas as pd

# Load the dataset
merged_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_Legislation.csv')

# Define the list of countries to be removed
countries_to_remove = ['Sark', 'Kenya', 'Nigeria', 'Mexico', 'El Salvador', 'Australia']

# Filter out the rows with the specified countries
filtered_df = merged_df[~merged_df['official_name_en'].isin(countries_to_remove)]

# Save the filtered dataframe to a new CSV file
filtered_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFiltered.csv', index=False)

# Count the number of unique countries in the 'official_name_en' column
num_unique_countries = filtered_df['official_name_en'].nunique()

# Print the number of unique countries
print(f'There are {num_unique_countries} unique countries in the official_name_en column.')

# Get the list of unique country names
unique_country_names = filtered_df['official_name_en'].unique()

# Print the list of country names
print(unique_country_names)

#%%

'''
There are 135 unique countries in the official_name_en column.
['Russian Federation' 'Georgia' 'Bangladesh' 'Kazakhstan' 'Poland'
 'Indonesia' 'Japan' 'Turkey' 'Libya' 'United States of America' 'Lebanon'
 'Republic of Moldova' 'Saudi Arabia' 'Greece' 'Italy' 'Tokelau' 'Oman'
 'South Africa' 'Ukraine' 'Jordan' 'Egypt' 'Thailand' 'Malaysia' 'China'
 'Belarus' 'United Arab Emirates' 'Dominican Republic' 'Republic of Korea'
 'Ghana' 'Haiti' 'Kyrgyzstan' 'Ireland' 'Viet Nam' 'Mozambique'
 "Côte d'Ivoire" 'Switzerland' 'Argentina' 'Uganda' 'Afghanistan' 'India'
 'Philippines' "Democratic People's Republic of Korea"
 'China, Hong Kong Special Administrative Region' 'Portugal' 'Senegal'
 'Cambodia' 'Zambia' 'Mali' 'Denmark' 'Morocco' 'Romania' 'Qatar'
 'Bahrain' 'Syrian Arab Republic' 'Singapore' nan 'Trinidad and Tobago'
 'Kuwait' 'Azerbaijan' 'Germany' 'Ethiopia'
 'The former Yugoslav Republic of Macedonia' 'Serbia'
 'Bosnia and Herzegovina' 'Cyprus' 'Albania' 'Uzbekistan' 'Lithuania'
 'Bulgaria' 'Czechia' 'Austria' 'Burundi' 'Israel' 'Spain' 'Niger'
 'France' 'Tajikistan' 'Sierra Leone' 'Ecuador' 'Turkmenistan'
 'United Republic of Tanzania' 'Iraq' 'Sudan' 'Tunisia' 'Malawi'
 'Mauritius' 'Sweden' 'Gabon' 'Madagascar' 'Vanuatu'
 'United Kingdom of Great Britain and Northern Ireland' 'Norway' 'Hungary'
 'Guatemala' 'Burkina Faso' 'Colombia' 'Djibouti' 'Papua New Guinea'
 'Somalia' 'Cameroon' 'Guyana' 'Chad' 'Mauritania' 'Netherlands' 'Finland'
 'Pakistan' 'Nepal' 'Belgium' 'Slovakia' 'Brunei Darussalam' 'Armenia'
 'Algeria' 'Guinea' 'Honduras' 'Benin' 'Brazil' 'Chile' 'Uruguay' 'Yemen'
 'Sri Lanka' 'Peru' 'Bahamas' 'Democratic Republic of the Congo'
 'Costa Rica' 'Curaçao' 'Croatia' 'Iran (Islamic Republic of)'
 "Lao People's Democratic Republic" 'Montenegro' 'Mongolia' 'Panama'
 'Paraguay' 'South Sudan' 'Slovenia' 'Timor-Leste'
 'Venezuela (Bolivarian Republic of)']

'''

#%%

# 'TWN' has no country name in official_name_en
# Add the name "Taiwan" to the dataset in official_name_en to make 136 countries

filtered_df = pd.read_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFiltered.csv')

# Update 'official_name_en' for 'TWN'
filtered_df.loc[filtered_df['ISO3166-1-Alpha-3'] == 'TWN', 'official_name_en'] = 'Taiwan'

# Verify the changes for 'TWN'
updated_twn_rows = filtered_df[filtered_df['ISO3166-1-Alpha-3'] == 'TWN']

# Display the updated rows for 'TWN'
print(updated_twn_rows[['ISO3166-1-Alpha-3', 'official_name_en']])

# Save the changes back to the CSV file
filtered_df.to_csv(r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv')


unique_legality = filtered_df['countriesWhereProstitutionIsLegal_model'].unique()

# Print the unique values
print("Unique values in 'countriesWhereProstitutionIsLegal_model':")
print(unique_legality)


#%%

"""
Created on Tue Dec 12 08:28:56 2023

@author: amyfo

Visulaizations for Dataset 

"""

#%%

# Create visualizations 
# Spot outliers in the data


#%%

# Bar Chart measured in log due to large disparity in the values with number labeles

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path)

# Convert 'isSexualExploit' to binary format and encode 'countriesWhereProstitutionIsLegal_model'
df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)
encoder = LabelEncoder()
df['countriesWhereProstitutionIsLegal_model_encoded'] = encoder.fit_transform(df['countriesWhereProstitutionIsLegal_model'])

# Group by 'countriesWhereProstitutionIsLegal_model_encoded' and count the instances of sex trafficking
grouped_data = df.groupby('countriesWhereProstitutionIsLegal_model_encoded')['isSexualExploit'].sum().reset_index()


# Define a custom color palette
custom_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']


# Replace the color hex codes below with the colors you want to use for each group
# Define a custom color palette with actual hex color codes
custom_palette = ['#9467bd',  # Purple for Abolitionism
                  '#7f7f7f',  # Medium Gray for Decriminalization
                  '#2ca02c',  # Green for Legalization
                  '#1f77b4',  # Blue for Neo-Abolitionism
                  '#d62728']  # Red for Prohibitionism


# Create a bar plot with the custom color palette
plt.figure(figsize=(12, 6))
barplot = sns.barplot(
    x='countriesWhereProstitutionIsLegal_model_encoded',
    y='isSexualExploit',
    data=grouped_data,
    palette=custom_palette  # Use the custom color palette
)

# Set the y-axis to a logarithmic scale
plt.yscale('log')

# Set the x-axis labels to the actual legislation names using the encoder's classes_
plt.xticks(range(len(encoder.classes_)), encoder.classes_, rotation=45)

# Add labels to each bar with a relative offset for clarity
percentage_offset = 0.1  # Adjust this value to change the space percentage
for index, value in enumerate(grouped_data['isSexualExploit']):
    offset_value = value * percentage_offset
    plt.text(index, value + offset_value, str(value), color='black', ha="center")

plt.title('Instances of Sex Trafficking by Legislation Type')
plt.xlabel('Legislation Type')
plt.ylabel('Instances of Sex Trafficking (log scale)')
plt.tight_layout()  # Adjust layout to make room for x-axis labels
plt.show()


#%%

# Scatter plot of sex trafficking instances by legislation and year

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Convert 'isSexualExploit' to binary format (1 for yes, 0 for no)
df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)

# Group data by year and legislation type and sum the instances
df_grouped = df.groupby(['yearOfRegistration', 'countriesWhereProstitutionIsLegal_model'])['isSexualExploit'].sum().reset_index()

# Custom color palette with more distinguishable colors
custom_palette = {
    'Abolitionism': '#FFA500',  # Orange
    'Prohibitionism': '#FF00FF',  # Magenta
    'Legalization': '#32CD32',  # LimeGreen
    'Neo-Abolitionism': '#1E90FF',  # DodgerBlue
    'Decriminalization': '#A9A9A9'  # Dark Gray
}

# Create a scatter plot
plt.figure(figsize=(14, 7))
scatterplot = sns.scatterplot(
    x='yearOfRegistration',
    y='isSexualExploit',
    hue='countriesWhereProstitutionIsLegal_model',
    data=df_grouped,
    palette=custom_palette,
    alpha=0.6,
    s=50
)


plt.title('Scatter Plot of Sex Trafficking Instances by Year and Legislation Type')
plt.xlabel('Year of Registration')
plt.ylabel('Number of Sex Trafficking Instances')

# Adjust layout for x-axis labels and legend
plt.subplots_adjust(bottom=0.2, top=0.9)

# Show the plot
plt.show()




#%%

# Verify numbers

import pandas as pd

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Convert 'isSexualExploit' to binary format (1 for yes, 0 for no)
if df['isSexualExploit'].dtype != 'int64' or df['isSexualExploit'].max() > 1:
    df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)

# Group by 'countriesWhereProstitutionIsLegal_model' and count the instances of sex trafficking
grouped_data = df.groupby('countriesWhereProstitutionIsLegal_model')['isSexualExploit'].sum().reset_index()

grouped_data


#%%

'''
RESULTS

Out[16]: 
  countriesWhereProstitutionIsLegal_model  isSexualExploit
0                            Abolitionism             1682
1                       Decriminalization               17
2                            Legalization             1059
3                        Neo-Abolitionism               16
4                          Prohibitionism            51533

'''

#%%

# Pie chart of differnt types of human trafficking in the dataset

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)


# Convert 'isForcedLabour', 'isSexualExploit', 'isOtherExploit' to binary format (1 for yes, 0 for no)
df['isForcedLabour'] = df['isForcedLabour'].notnull().astype(int)
df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)
df['isOtherExploit'] = df['isOtherExploit'].notnull().astype(int)

# Sum the instances of each type of human trafficking
trafficking_counts = {
    'Forced Labour': df['isForcedLabour'].sum(),
    'Sexual Exploitation': df['isSexualExploit'].sum(),
    'Other Exploitation': df['isOtherExploit'].sum()
}

# Define a custom color palette for the pie chart
custom_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green

# Create a pie chart with the custom color palette
plt.figure(figsize=(8, 8))
plt.pie(trafficking_counts.values(), labels=trafficking_counts.keys(), colors=custom_colors, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Trafficking Types in Dataset')
plt.show()

#%%

# Bar chart of human trafficking category by gender

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Convert trafficking indicators to binary format (1 for yes, 0 for no)
trafficking_columns = ['isForcedLabour', 'isSexualExploit', 'isOtherExploit']
for col in trafficking_columns:
    df[col] = df[col].notnull().astype(int)

# Assuming the dataset has a 'gender' column
if 'gender' in df.columns:
    # Melt the DataFrame to make it suitable for a seaborn bar plot
    df_melted = df.melt(id_vars='gender', value_vars=trafficking_columns, var_name='Trafficking Type', value_name='Count')

    # Group by gender and trafficking type, then sum the counts
    grouped_df = df_melted.groupby(['gender', 'Trafficking Type']).sum().reset_index()

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Trafficking Type', y='Count', hue='gender', data=grouped_df)
    plt.title('Human Trafficking Categories by Gender')
    plt.xlabel('Trafficking Type')
    plt.ylabel('Count')
    plt.show()
else:
    print("The dataset does not have a 'gender' column.")


#%%

# To accurately depict exploitation by both gender and age categories, we need to create a faceted plot.

file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Creating a faceted plot using seaborn's catplot
g = sns.catplot(x='ageBroad', y='Count', hue='Exploitation Type', col='gender', data=grouped_long_df, 
                kind='bar', ci=None, palette=custom_palette, height=5, aspect=1)

# Adjusting plot details
g.fig.suptitle('Exploitation Types by Gender and Age Categories', y=1.05)
g.set_axis_labels("Age Category", "Count")
g.set_xticklabels(rotation=45)
plt.tight_layout()
plt.show()


#%%

# Count of exploitation instances for each country with over 500 reports

file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Modifying the previous code to add actual counts above each bar in the graph

plt.figure(figsize=(15, 8))
barplot = sns.barplot(x='CountryName', y='Count', data=country_counts_greater_500)

# Adding count labels above each bar
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.0f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha = 'center', va = 'center', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

plt.title('Countries with More Than 500 Instances of Exploitation')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotating the country names for better visibility
plt.tight_layout()
plt.show()


#%%

"""
Created on Tue Dec 12 08:28:56 2023

@author: amyfo

Machine Learning Algorithm to Detect Sex Trafficking 

"""

#%%

# Find categorical and numerical columns in df

import pandas as pd

# Load your dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path)

# Initialize lists to hold the names of categorical and numerical features
categorical_features = []
numerical_features = []

# Loop through the columns and classify them based on data type
for column in df.columns:
    if df[column].dtype == 'object' or df[column].dtype.name == 'category':
        categorical_features.append(column)
    else:
        numerical_features.append(column)

# Print the lists
print("Categorical Features:", categorical_features)
print("Numerical Features:", numerical_features)


#%%

# Apply balancing methods as shown in class
# Use Logistic Regression with a balanced class weight
# Apply stratified splitting to balance data
# Use GridSearchCV for hyperparameter tuning

import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Convert 'isSexualExploit' to binary format (1 for "yes", 0 for "no" or NaN)
df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)

# Encode 'countriesWhereProstitutionIsLegal_model' with numerical values
encoder = LabelEncoder()
df['countriesWhereProstitutionIsLegal_model'] = encoder.fit_transform(df['countriesWhereProstitutionIsLegal_model'])

# Define features (X) and target variable (y)
X = encoded_features
y = df['isSexualExploit']

# Split the data into training and testing sets with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# Standardize the feature variables
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Setting up the hyperparameters for GridSearch
param_grid = {
    'solver': ['lbfgs', 'liblinear', 'newton-cg', 'sag', 'saga'],
    'C': [0.001, 0.01, 0.1, 1, 10, 100]
}

# Create a Logistic Regression model with balanced class weight
log_reg = LogisticRegression(max_iter=10000, class_weight='balanced')

# Set up StratifiedKFold cross-validation
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Apply GridSearchCV for hyperparameter tuning
grid_search = GridSearchCV(log_reg, param_grid, cv=stratified_kfold, scoring='accuracy')
grid_search.fit(X_train_scaled, y_train)

# Best model parameters and estimator
print("Best Parameters:", grid_search.best_params_)
best_log_reg = grid_search.best_estimator_

# Predict on the test set using the best estimator
y_pred = best_log_reg.predict(X_test_scaled)

# Print classification report
print(classification_report(y_test, y_pred, target_names=["Not Sex Trafficking", "Sex Trafficking"]))


#%%

'''
RESULTS 

Best Parameters: {'C': 0.001, 'solver': 'lbfgs'}
                     precision    recall  f1-score   support

Not Sex Trafficking       0.88      0.28      0.42     21046
    Sex Trafficking       0.51      0.95      0.66     16292

           accuracy                           0.57     37338
          macro avg       0.69      0.62      0.54     37338
       weighted avg       0.72      0.57      0.53     37338

'''


#%%

# Find out which features/columns in this dataset are most important to the models accuracy
# List as many features/columns as is 'logically' possible without being redundant

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Load data
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, dtype={5: 'object', 48: 'object'})

# Transform 'isSexualExploit' column to a binary format: 
# Set to 1 if a value is present, and 0 if the value is missing (NaN)
df['isSexualExploit'] = df['isSexualExploit'].apply(lambda x: 0 if pd.isna(x) else 1)

# Define numerical and categorical features
numerical_features = [
    'meansOfControlDebtBondage', 'meansOfControlTakesEarnings', 'meansOfControlThreats', 
    'meansOfControlPsychologicalAbuse', 'meansOfControlPhysicalAbuse', 'meansOfControlSexualAbuse', 
    'meansOfControlFalsePromises', 'meansOfControlPsychoactiveSubstances', 'meansOfControlRestrictsMovement', 
    'meansOfControlRestrictsMedicalCare', 'meansOfControlExcessiveWorkingHours', 'meansOfControlThreatOfLawEnforce', 
    'meansOfControlWithholdsNecessities', 'meansOfControlWithholdsDocuments', 'meansOfControlOther', 
    'isForcedLabour', 'isOtherExploit', 'typeOfLabourAgriculture', 'typeOfLabourConstruction', 
    'typeOfLabourDomesticWork', 'typeOfLabourHospitality', 'typeOfLabourOther', 'typeOfSexProstitution', 
    'typeOfSexPornography', 'typeOfSexOther', 'recruiterRelationIntimatePartner', 'recruiterRelationFriend', 
    'recruiterRelationFamily', 'recruiterRelationOther', 'pop2023', 'growthRate', 'yearOfRegistration'
]

categorical_features = [
    'gender', 'ageBroad', 'majorityStatusAtExploit', 'traffickMonths', 'CountryOfExploitation', 
    'subregion', 'countriesWhereProstitutionIsLegal_model', 'citizenship'
]

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='median')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Define the model
model = RandomForestClassifier(n_estimators=100, random_state=0)

# Bundle preprocessing and modeling code in a pipeline
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('model', model)
                     ])

# Split data into train and test sets
X = df.drop('isSexualExploit', axis=1)  # Drop the target column to create the feature set
y = df['isSexualExploit']  # Use the correct target column
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fit the model
clf.fit(X_train, y_train)

# Get feature importances
feature_importances = clf.named_steps['model'].feature_importances_

# Get feature names after One-Hot Encoding
ohe = (clf.named_steps['preprocessor']
        .named_transformers_['cat']
        .named_steps['onehot'])
feature_names = ohe.get_feature_names_out(input_features=categorical_features)

# Add numerical features to the feature names
feature_names = np.concatenate([numerical_features, feature_names])

# Create a DataFrame for feature importances
importances_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importances})

# Aggregate the importances for One-Hot Encoded features back to the original column names
importances_df['OriginalFeature'] = importances_df['Feature'].apply(lambda x: x.split('_')[0])
column_importances = importances_df.groupby('OriginalFeature')['Importance'].sum().sort_values(ascending=False)

print(column_importances)

#%%

'''
RESULTS

OriginalFeature
CountryOfExploitation                   0.214267
citizenship                             0.153854
subregion                               0.146896
gender                                  0.112881
yearOfRegistration                      0.098233
pop2023                                 0.094634
growthRate                              0.062849
ageBroad                                0.041637
countriesWhereProstitutionIsLegal       0.040536
majorityStatusAtExploit                 0.017579
traffickMonths                          0.016634
typeOfLabourAgriculture                 0.000000
recruiterRelationFriend                 0.000000
recruiterRelationIntimatePartner        0.000000
recruiterRelationOther                  0.000000
typeOfLabourConstruction                0.000000
typeOfLabourDomesticWork                0.000000
typeOfLabourHospitality                 0.000000
typeOfLabourOther                       0.000000
typeOfSexOther                          0.000000
typeOfSexPornography                    0.000000
typeOfSexProstitution                   0.000000
recruiterRelationFamily                 0.000000
meansOfControlWithholdsDocuments        0.000000
meansOfControlWithholdsNecessities      0.000000
isForcedLabour                          0.000000
meansOfControlThreats                   0.000000
meansOfControlTakesEarnings             0.000000
meansOfControlSexualAbuse               0.000000
meansOfControlRestrictsMovement         0.000000
meansOfControlRestrictsMedicalCare      0.000000
meansOfControlPsychologicalAbuse        0.000000
meansOfControlPsychoactiveSubstances    0.000000
meansOfControlPhysicalAbuse             0.000000
meansOfControlOther                     0.000000
meansOfControlFalsePromises             0.000000
meansOfControlExcessiveWorkingHours     0.000000
meansOfControlDebtBondage               0.000000
isOtherExploit                          0.000000
meansOfControlThreatOfLawEnforce        0.000000
Name: Importance, dtype: float64

'''


#%%

# Take out Features that dont contirbute or negatively effect the accuracy of this model
# Incorporate the stratified sampling based on the 'CountryOfExploitation' column 
# Ensure that the proportion of each country's data is the same in both the training and testing datasets as in the full dataset 
# This helps to avoid bias in the model due to unequal representation of countries

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.inspection import permutation_importance
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Load data
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path, low_memory=False)

# Transform 'isSexualExploit' column to a binary format: 
df['isSexualExploit'] = df['isSexualExploit'].apply(lambda x: 0 if pd.isna(x) else 1)

# Define numerical and categorical features
numerical_features = ['yearOfRegistration', 'pop2023', 'growthRate']
categorical_features = [
    'gender', 'citizenship', 'ageBroad', 'majorityStatusAtExploit', 'traffickMonths',
    'subregion', 'countriesWhereProstitutionIsLegal_model', 'CountryOfExploitation',
]


# Preprocessing for numerical data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Define features (X) and target variable (y)
X = df[numerical_features + categorical_features]
y = df['isSexualExploit']

# Create the model pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', RandomForestClassifier(random_state=42, n_estimators=50))
])

# Split the data with stratified sampling based on 'CountryOfExploitation'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=df['CountryOfExploitation'], random_state=42)

# Hyperparameter grid
param_grid = {
    'classifier__max_depth': [None, 10],
    'classifier__min_samples_split': [2, 5]
}

# StratifiedKFold
n_splits = 5
stratified_kfold = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

# GridSearchCV
grid_search = GridSearchCV(pipeline, param_grid, cv=stratified_kfold, scoring='f1_macro', n_jobs=-1)

# Fit the model
try:
    grid_search.fit(X_train, y_train)
    print("Best Parameters:", grid_search.best_params_)
except Exception as e:
    print("An error occurred during grid search:", e)

# Predict and evaluate
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["Not Sex Trafficking", "Sex Trafficking"]))


#%%

'''

RESULTS

Best Parameters: {'classifier__max_depth': None, 'classifier__min_samples_split': 5}
                     precision    recall  f1-score   support

Not Sex Trafficking       0.96      0.80      0.87     21005
    Sex Trafficking       0.79      0.95      0.86     16333

           accuracy                           0.87     37338
          macro avg       0.87      0.88      0.87     37338
       weighted avg       0.88      0.87      0.87     37338

'''

#%%

# Use Legalization as the baseline legislation
# This change shows how other legislative approaches differ from 'Legalization'
# in terms of their impact on the target variable ('isSexualExploit')
# Account for imbalance in the data with startified sampleing

import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path)

# Convert 'isSexualExploit' to binary format (1 for "yes", 0 for "no" or NaN)
df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)

# Creating dummy variables for the 'countriesWhereProstitutionIsLegal_model' column
# 'Legalization' will be used as the new baseline, so it should be excluded from the dummy variables
categories = df['countriesWhereProstitutionIsLegal_model'].unique()
categories = [cat for cat in categories if cat != 'Legalization']
legislation_dummies = pd.get_dummies(df['countriesWhereProstitutionIsLegal_model'])[categories]

# Add the dummy variables to the dataframe
df = pd.concat([df, legislation_dummies], axis=1)

# Define features (X) and target variable (y)
X = df[legislation_dummies.columns]  # Use only the dummy variables as features
X['LegislationType'] = df['countriesWhereProstitutionIsLegal_model'] # Add original legislation column for stratification
y = df['isSexualExploit']

# Split the data into training and testing sets with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=X['LegislationType'], random_state=42)

# Drop the 'LegislationType' column after stratification
X_train.drop('LegislationType', axis=1, inplace=True)
X_test.drop('LegislationType', axis=1, inplace=True)

# Convert boolean columns to integers
X_train = X_train.astype(int)

# Add a constant to the model (for statsmodels)
X_train_sm = sm.add_constant(X_train)

# Ensure indices of X_train_sm and y_train are consistent
X_train_sm = X_train_sm.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

# Fit the logistic regression model using statsmodels
logit_model = sm.Logit(y_train, X_train_sm)
result = logit_model.fit()

# Display the summary
print(result.summary())


#%%

'''
RESULTS

Optimization terminated successfully.
         Current function value: 0.630439
         Iterations 9
                           Logit Regression Results                           
==============================================================================
Dep. Variable:        isSexualExploit   No. Observations:                87122
Model:                          Logit   Df Residuals:                    87117
Method:                           MLE   Df Model:                            4
Date:                Wed, 13 Dec 2023   Pseudo R-squ.:                 0.08042
Time:                        18:44:39   Log-Likelihood:                -54925.
converged:                       True   LL-Null:                       -59728.
Covariance Type:            nonrobust   LLR p-value:                     0.000
=====================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                -1.4883      0.041    -36.120      0.000      -1.569      -1.407
Prohibitionism        1.5250      0.042     36.413      0.000       1.443       1.607
Abolitionism         -0.4652      0.052     -8.997      0.000      -0.567      -0.364
Decriminalization    -3.6192      0.292    -12.375      0.000      -4.192      -3.046
Neo-Abolitionism     -2.3285      0.308     -7.570      0.000      -2.931      -1.726
=====================================================================================


'''


'''
RESULTS


DESCRIPTION

This logistic regression analysis that aims to model the relationship between different legislative approaches related to prostitution (specifically, 'Prohibitionism,' 'Abolitionism,' 'Decriminalization,' and 'Neo-Abolitionism') and the likelihood of 'isSexualExploit.' Let's break down the key components of these results:

Intercept and Coefficients:

Intercept (const): -1.1945699610221387
Coefficients: [ 1.47346622 -0.47514572 -3.72410321 -2.09195361]
The intercept represents the estimated log-odds of 'isSexualExploit' when all predictor variables are zero. In this case, it is approximately -1.195.

The coefficients represent the estimated effects of each legislative approach on the log-odds of 'isSexualExploit.' These coefficients indicate how a one-unit change in each predictor variable affects the log-odds of the outcome.

'Prohibitionism' coefficient: 1.47346622
'Abolitionism' coefficient: -0.47514572
'Decriminalization' coefficient: -3.72410321
'Neo-Abolitionism' coefficient: -2.09195361
Model Summary:

Dependent Variable: 'isSexualExploit'
Number of Observations: 87,122
Model: Logistic Regression
Degrees of Freedom (Df) Residuals: 87117 (reflects the degrees of freedom associated with the model)
Degrees of Freedom (Df) Model: 4 (number of predictor variables)
Pseudo R-squared: 0.07829
The pseudo R-squared value indicates the proportion of variance in 'isSexualExploit' explained by the model. In this case, the model explains approximately 7.83% of the variance in the outcome.

Convergence and Likelihood:

Converged: True
Log-Likelihood: -54994.
LL-Null: -59665.
The 'Converged' field indicates whether the optimization algorithm successfully converged to a solution. In this case, it converged successfully.

Log-Likelihood: The log-likelihood of the model is -54994., which represents the overall goodness of fit. The goal in logistic regression is to maximize the log-likelihood, and this value helps assess how well the model fits the data.

LL-Null: The log-likelihood of a null model with no predictors. The model's log-likelihood is compared to this value to assess its goodness of fit.

Covariance Type and LLR p-value:

Covariance Type: nonrobust
LLR p-value: 0.000
The covariance type indicates the type of covariance matrix used in the model. In this case, it's "nonrobust."

The LLR (Likelihood Ratio Test) p-value is 0.000, indicating that the logistic regression model is statistically significant compared to the null model (i.e., it provides a better fit than a model with no predictors).

Overall, these results provide information on the estimated coefficients of the legislative approaches and their impact on the likelihood of 'isSexualExploit' compared to the reference category (the constant or intercept term). The p-values suggest that all four legislative approaches are statistically significant in predicting 'isSexualExploit.' The coefficients themselves provide insights into the direction and magnitude of these effects on the log-odds of the outcome.










'''
#%%

# Use Prohibitionism as the baseline legislation
# This change shows how other legislative approaches differ from 'Legalization'
# in terms of their impact on the target variable ('isSexualExploit')
# Account for imbalance in the data with startified sampleing

import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = r'C:\Users\amyfo\OneDrive\Laptop Desktop\Digital Scholarship MSc\AI and Machine Learning\AI and Machine Learning Paper\Datasets\UpdatedwMissingCTDCLegislation_merged_df_with_USA_LegislationFilteredandTaiwan.csv'
df = pd.read_csv(file_path)

# Convert 'isSexualExploit' to binary format (1 for "yes", 0 for "no" or NaN)
df['isSexualExploit'] = df['isSexualExploit'].notnull().astype(int)

# Creating dummy variables for the 'countriesWhereProstitutionIsLegal_model' column
# 'Legalization' will be used as the new baseline, so it should be excluded from the dummy variables
categories = df['countriesWhereProstitutionIsLegal_model'].unique()
categories = [cat for cat in categories if cat != 'Prohibitionism']
legislation_dummies = pd.get_dummies(df['countriesWhereProstitutionIsLegal_model'])[categories]

# Add the dummy variables to the dataframe
df = pd.concat([df, legislation_dummies], axis=1)

# Define features (X) and target variable (y)
X = df[legislation_dummies.columns]  # Use only the dummy variables as features
X['LegislationType'] = df['countriesWhereProstitutionIsLegal_model'] # Add original legislation column for stratification
y = df['isSexualExploit']

# Split the data into training and testing sets with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=X['LegislationType'], random_state=42)

# Drop the 'LegislationType' column after stratification
X_train.drop('LegislationType', axis=1, inplace=True)
X_test.drop('LegislationType', axis=1, inplace=True)

# Convert boolean columns to integers
X_train = X_train.astype(int)

# Add a constant to the model (for statsmodels)
X_train_sm = sm.add_constant(X_train)

# Ensure indices of X_train_sm and y_train are consistent
X_train_sm = X_train_sm.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

# Fit the logistic regression model using statsmodels
logit_model = sm.Logit(y_train, X_train_sm)
result = logit_model.fit()

# Display the summary
print(result.summary())

#%%


'''
RESULTS

Optimization terminated successfully.
         Current function value: 0.630439
         Iterations 9
                           Logit Regression Results                           
==============================================================================
Dep. Variable:        isSexualExploit   No. Observations:                87122
Model:                          Logit   Df Residuals:                    87117
Method:                           MLE   Df Model:                            4
Date:                Wed, 13 Dec 2023   Pseudo R-squ.:                 0.08042
Time:                        18:55:27   Log-Likelihood:                -54925.
converged:                       True   LL-Null:                       -59728.
Covariance Type:            nonrobust   LLR p-value:                     0.000
=====================================================================================
                        coef    std err          z      P>|z|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                 0.0367      0.007      4.899      0.000       0.022       0.051
Legalization         -1.5250      0.042    -36.413      0.000      -1.607      -1.443
Abolitionism         -1.9902      0.032    -61.950      0.000      -2.053      -1.927
Decriminalization    -5.1442      0.290    -17.760      0.000      -5.712      -4.576
Neo-Abolitionism     -3.8534      0.305    -12.638      0.000      -4.451      -3.256
=====================================================================================

'''