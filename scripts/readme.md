API EndPoint: https://data.cityofnewyork.us/resource/uip8-fykc.csv

In the datasourcing.py file, I sourced the data using the web API that was provided. 

In the storage.py file, I included the python code that I used to connect to my google cloud storage account and used the API endpoint to store the CSV file into my bucket. 

In the transformation.py file, I included the python code that shows how I transformed and cleaned up the data to make it easier to understand. I first read the csv file from my storage bucket and converted it into a pandas data frame. I then changed the arrest_date column and made it into a unified format. I also removed the null values and duplicate rows. I added new columns that are more descriptive and can be included in the facts table for my dimensional model. I also made sure to correct any data types for existing and new columns. Lastly, I loaded the transformed data back into my GCS, so that I can use it to make visuals later. 

In the datamapping.py file it shows the format that I used to write my new columns into the data dictionary. I made a connection to my excel file and added a new sheet that includes the columns, data types and each description. 


