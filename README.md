# The Battle of Neighborhoods - New York Hospital Bed Density

## Project Motivation        

Are the hospitals near me ready for Coronavirus?              
Until April 25th, the confirmed COVID-19 cases in New York City have reached 150,000 and the confirmed deaths 10,961. New York City State now has more COVID-19 cases than any single coutry outside the US, according to latest figures.      

This project was motivated by the current national battle to beat pandemic. It aims to analyze the hospital bed density for each neighborhood in the five boroughs of New York City.     
Hospital Bed Density provides the number of hospital beds per 1,000 people; It serves as a general measure of inpatient service availability, especially in  the battles to beat pandemic. Hospital beds include inpatient beds available in public, private, general, and specialized hospitals and rehabilitatiion centers. Because the level of inpatient services required depends on several factors - such as demographic issues and the burden of disease - there is no global target for the number of hospital beds percountry. In United States, the hospital bed density is measured as 2.9 beds per 1,000 people.        


## Data Source

1. NYC Hospital Data ([hospital_beds.csv](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/hospital_beds.csv)) was scrapped from New York State [Department of Health](https://profiles.health.ny.gov/hospital). It contains hospital name, bed type and the corresponding bed numbers in each type. 76 hospitals data in NYC are collected.


2. [NYC Neiborhood Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/newyork_data.json)) is a json file dowloaded from [New York City Neighborhoods Names](https://geo.nyu.edu/catalog/nyu_2451_34572). After cleaning and transorming, it includes latitude and longitude for each neighborhood of the 5 boroughs in NYC.

3. [NYC Population Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/new_york_data.csv) includes population data per neighborhood that were scrapped from Wikipedia, and then integrated with [New York Neiborhood Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/newyork_data.json)). It has 5 fileds: Borough, Neighborhood, Population, Longitude and Latitude.


## Project Plan

This project will include the following steps:
    
- Collect and clean New York Hospital Data 
- Collect and clean New York Neighborhood Data
- Collect and clean New York Population Data
- Collect Hospital Latitude and Longitude Data
- Data Integration 
- Statistical Analysis and Visulization
- K-Means Neighborhood Clustering Analysis on Hospital Bed Density 
- Visulize the Neighborhood Clusters 
- Analyze Results


## Method
 
1. **Web Scrapping with Selenium**    

[Selenium](https://www.selenium.dev/) is a framework which is designed to automate test for web applications. It can be used to control the browser interactions automatically such as link clicks and form submissions.       

In our case of collecting NYC Hospital Data ([hospital_beds.csv](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/hospital_beds.csv)), we need a click on the target webpage to upfold the 'Bed Types' table for fetching, selenuium is suitable in this scenario. The cleaned dataframe looks like this:         
       
[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/1.png)       
             

2. **Fetching Hospital Latitude and Longitude using [Foursquare](https://foursquare.com/) API**    

Since we will combine hospital data with NYC neighborhood data later, we need to have each hospital's latitude and longitude information using Foursquare API. The cleaned dataframe looks like this:         
     
[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/2.png)

3. **Fetching NYC Neighborhood Data using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**   

I dowloaded json file from [New York City Neighborhoods Names](https://geo.nyu.edu/catalog/nyu_2451_34572). It contains four fileds: NYC Borough, Neighborhood, Latitude and Longitude. The cleaned dataframe looks like this:         

[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/3.png)

4. **Fetching NYC Population per Neighborhood from Wikipedia using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**     
The [Neighborhoods in New York City]("https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City") page from [Wikipedia]("https://en.wikipedia.org") has a list of neighborhoods names and each name contains a anchor tag connecting to its own Wikipedia page, where populatiion data on the right hand side table can be found.      
I use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to fetch each neighborhood name from Wikepedia, and run iteration via requests to visit each page of the neighborhood, and scrap its population data. The dataframe fetched include Neighborhood name, its Anchor tag and Population:

[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/4.png)        


5. **Combine NYC Neighborhood Data and Population Data**    
Merge NYC neighborhood data wiith population data and get:      
[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/5.png)   

Here is a box chart of Neighborhood per Borough:    
[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Neighborhood%20per%20Borough.png)

Here is a box chart of Population per Borough:
[](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Population%20per%20Borough.png)

6. ** Hospital Data









3. Statistical Analysis and Visulization






## Result and Discussion

## Conclusion
