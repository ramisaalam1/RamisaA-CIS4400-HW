import pandas as pd
from google.cloud import storage
import io
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/ramisaalam/Downloads/silver-bird-412916-cd24855ad9db.json'

storage_client = storage.Client()

bucket_name = 'cis4400-hw-ra'
file_name = 'nypd_arrest_data.csv'  

bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(file_name)

blob_data = blob.download_as_bytes()
data_io = io.BytesIO(blob_data)

df = pd.read_csv(data_io)

print(df.head())

#Transformation
df['arrest_date'] = pd.to_datetime(df['arrest_date'])
df['year'] = df['arrest_date'].dt.year
df['month'] = df['arrest_date'].dt.month
df['day'] = df['arrest_date'].dt.day

df = df.dropna()

df = df.drop_duplicates()

df['pd_cd'] = pd.to_numeric(df['pd_cd'], errors='coerce')
df['ky_cd'] = pd.to_numeric(df['ky_cd'], errors='coerce')
df['arrest_precinct'] = pd.to_numeric(df['arrest_precinct'], errors='coerce')
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

print(df.head())

#Transformation - New Columns 
df['is_felony'] = (df['law_cat_cd'] == 'F')
df['is_misdemeanor'] = (df['law_cat_cd'] == 'M')
df['is_violation'] = (df['law_cat_cd'] == 'V')

df['is_felony'] = df['is_felony'].astype(int)
df['is_misdemeanor'] = df['is_misdemeanor'].astype(int)
df['is_violation'] = df['is_violation'].astype(int)

df['arrest_count'] = 1

df['boro_precinct'] = df['arrest_boro'] + '_' + df['arrest_precinct'].astype(str)

def age_category(age_group):
    if age_group in ['<18', '18-24']:
        return 'Young Adult'
    elif age_group in ['25-44']:
        return 'Adult'
    elif age_group in ['45-64']:
        return 'Middle Aged'
    else:
        return 'Senior'
df['age_category'] = df['age_group'].apply(age_category)

print(df.head())

#Load transformed data to GCS 
transformed_data = df.to_csv(index=False)

bucket_name = 'cis4400-hw-ra'
transformed_file_name = 'transformed_nypd_arrest_data.csv'

bucket = storage_client.bucket(bucket_name)

blob = bucket.blob(transformed_file_name)
blob.upload_from_string(transformed_data, content_type='text/csv')

print(f'Transformed data uploaded to {bucket_name}/{transformed_file_name}')
