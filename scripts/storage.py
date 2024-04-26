import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/ramisaalam/Downloads/silver-bird-412916-cd24855ad9db.json'

storage_client = storage.Client()

print("Buckets:")
for bucket in storage_client.list_buckets():
    print(bucket.name)
    
#Storage
import requests
from google.cloud import storage

url = 'https://data.cityofnewyork.us/resource/uip8-fykc.csv'

response = requests.get(url)
data = response.text  

bucket_name = 'cis4400-hw-ra'
file_name = 'nypd_arrest_data.csv'  

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)

blob = bucket.blob(file_name)
blob.upload_from_string(data, content_type='text/csv')

print(f'File uploaded to {bucket_name}/{file_name}')