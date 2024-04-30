# Ramisa Alam: NYPD Arrest Data

## Explanation of the Data
The NYPD Arrest Dataset can be found through the NYC Open Data website. The dataset is given by the Police Department (NYPD) and is updated quarterly. It provides detailed data about all the New York City arrests that happened throughout the year. It provides information regarding the type of crime, its location, and when it occurred. This data is essential to collect because it allows us to keep track of crime patterns in NYC and identify opportunities for improvement. It also includes demographic information such as the age and gender of the arrested person and what borough it occurred in. These data points can help individuals understand what regions of New York City experience the most crime. 

## Business Problem
Since this dataset holds important information about arrests that are made every day, it can be hard to handle all the information and keep it in the correct and consistent format. For the requirements, I want to create a Data warehouse architecture that can handle large volumes of arrest data and be able to monitor the different arrest information. 

## Business Impact 
Setting up a data warehouse for arrest data can help keep track of all the arrests both past and present. Integrating a data warehouse can help manage the data better and allow for easier access however it can be costly and time-consuming to maintain. 

## Business Persona
The police department, policymakers, and law enforcement agencies will all be interested in this dataset. These individuals can use this data to make better strategic decisions and implement new rules to lower arrest rates.

# Data 
I used the ETL process. I first extracted the data from the API and stored it in a GCS bucket. I then read the data from the storage bucket and made it into a pandas data frame. I then transformed the data by adding new columns, dropping values, and more to make it easier to work with. Lastly, I loaded the data back into storage and created different visuals in Tableau. 

## Metadata
Information about the columns and their description are stored in the data dictionary and can be found in the docs folder. 

## Methods
I created a dimensional model that can help us visualize the different facts and dimensions to understand the relationship between the data. 

## Data Tools 
I stored the data in Google Cloud Storage and used Python code in Jupiter Notebook to process the data. Lastly, I created the visuals in Tableau. 


