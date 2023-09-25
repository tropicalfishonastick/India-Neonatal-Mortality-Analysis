import pandas as pd

def read_unicef_data(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    return df

def check_missing_values(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Check for missing values
    missing_values = df.isnull().sum()
    return missing_values

def clean_unicef_data(df):
    # Select the relevant columns using square brackets for columns with special characters
    selected_columns = [
        'TIME_PERIOD:Time period',
        'OBS_VALUE:Observation Value',
        'SEX:Sex',
        'WEALTH_QUINTILE:Wealth Quintile',
        'INDICATOR:Indicator',
        'COUNTRY_NOTES:Country notes',
        'UNIT_MEASURE:Unit of measure',
        'LOWER_BOUND:Lower Bound',
        'UPPER_BOUND:Upper Bound'
    ]
    
    # Create a new DataFrame with only the selected columns
    cleaned_df = df[selected_columns].copy()
    
    # Rename the columns for clarity
    cleaned_df.columns = [
        'Year',
        'Neonatal_Mortality_Rate',
        'Sex',
        'Wealth_Quintile',
        'Indicator',
        'Country_Notes',
        'Unit_Measure',
        'Lower_Bound',
        'Upper_Bound'
    ]
    
    return cleaned_df
