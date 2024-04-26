import pandas as pd
from openpyxl import load_workbook

data_map = [
    {
        'Source Column': 'arrest_date',
        'Destination Column': 'arrest_date',
        'Data Type': 'datetime',
        'Description': 'This is the date when the arrest was made. It was converted to a datetime format YYYY-MM-DD.',
    },
    {
        'Source Column': 'pd_cd',
        'Destination Column': 'pd_cd',
        'Data Type': 'float64',
        'Description': 'The police department code for the offense, it was converted from string to numeric.',
    },
    {
        'Source Column': 'ky_cd',
        'Destination Column': 'ky_cd',
        'Data Type': 'float64',
        'Description': 'The key code for the offense, it was converted from string to numeric.',
    },
    {
        'Source Column': 'arrest_precinct',
        'Destination Column': 'arrest_precinct',
        'Data Type': 'float64',
        'Description': 'The precinct where the arrest occurred, it was converted from string to numeric.',
    },
    {
        'Source Column': 'latitude',
        'Destination Column': 'latitude',
        'Data Type': 'float64',
        'Description': 'Geographic latitude where the arrest occurred, it was converted from string to numeric.',
    },
    {
        'Source Column': 'longitude',
        'Destination Column': 'longitude',
        'Data Type': 'float64',
        'Description': 'Geographic longitude where the arrest occurred, it was converted from string to numeric.',
    },
    {
        'Source Column': 'law_cat_cd',
        'Destination Column': 'is_felony',
        'Data Type': 'boolean',
        'Description': 'Tells us if the arrest was considered a felony or not.',
    },
    {
        'Source Column': 'arrest_boro',
        'Destination Column': 'boro_precinct',
        'Data Type': 'object',
        'Description': 'The combination of arrest borough and precinct, it is a new key.',
    },
    {
        'Source Column': 'age_group',
        'Destination Column': 'age_category',
        'Data Type': 'object',
        'Description': 'Categorical representation of age group. Derived from age_group.',
    },
]

map_df = pd.DataFrame(data_map)

excel_file_path = '/Users/ramisaalam/Desktop/NYPD_Arrest_YTD_DataDictionary.xlsx'

excel = load_workbook(excel_file_path)

with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
    writer.book = excel
    writer.sheets = {ws.title: ws for ws in excel.worksheets}
    map_df.to_excel(writer, sheet_name='Data Mapping', index=False)

print("Data mapping was added to the Excel file.")