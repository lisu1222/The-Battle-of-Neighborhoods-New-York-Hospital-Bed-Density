# The Battle of Neighborhoods - New York Hospital Bed Density

## Project Motivation        

Are the hospitals near me ready for Coronavirus?              
Until April 25th, the confirmed COVID-19 cases in New York City have reached 150,000 and the confirmed deaths 10,961. New York City State now has more COVID-19 cases than any single country outside the US, according to latest figures.      

This project was motivated by the current national battle to beat pandemic. It aims to analyze the hospital bed density for each neighborhood in the five boroughs of New York City.     
Hospital Bed Density provides the number of hospital beds per 1,000 people; It serves as a general measure of inpatient service availability, especially in  the battles to beat pandemic. Hospital beds include inpatient beds available in public, private, general, and specialized hospitals and rehabilitatiion centers. Because the level of inpatient services required depends on several factors - such as demographic issues and the burden of disease - there is no global target for the number of hospital beds percountry. In United States, the hospital bed density is measured as 2.9 beds per 1,000 people.        


## Data Source

1. NYC Hospital Data ([hospital_beds.csv](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/hospital_beds.csv)) was scrapped from New York State [Department of Health](https://profiles.health.ny.gov/hospital). It contains hospital name, bed type and the corresponding bed numbers in each type. 76 hospitals data in NYC are collected.


2. [NYC Neighborhood Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/newyork_data.json)) is a json file dowloaded from [New York City Neighborhoods Names](https://geo.nyu.edu/catalog/nyu_2451_34572). After cleaning and transforming, it includes latitude and longitude for each neighborhood of the 5 boroughs in NYC.

3. [NYC Population Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/new_york_data.csv) includes population data per neighborhood that were scrapped from Wikipedia, and then integrated with [New York Neiborhood Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/newyork_data.json)). It has 5 fields: Borough, Neighborhood, Population, Longitude and Latitude.


## Project Plan

This project will include the following steps:
    
- Collect and clean New York Hospital Data 
- Collect and clean New York Neighborhood Data
- Collect and clean New York Population Data
- Collect Hospital Latitude and Longitude Data
- Data Integration 
- Statistical Analysis and Visualization
- K-Means Neighborhood Clustering Analysis on Hospital Bed Density 
- Visualize the Neighborhood Clusters 
- Analyze Results


## Method
 
### 1. Scrapping NYC Hospital Beds with Selenium    

[Selenium](https://www.selenium.dev/) is a framework which is designed to automate test for web applications. It can be used to control the browser interactions automatically such as link clicks and form submissions.       

In our case of collecting NYC Hospital Beds Data ([hospital_beds.csv](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/hospital_beds.csv)), we need a click on the target webpage to unfold the 'Bed Types' table for fetching, selenium is suitable in this scenario. The cleaned DataFrame looks like this:         
       
![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/1.png)       
  
### 2. Fetching NYC Neighborhood Data using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)   

I dowloaded json file from [New York City Neighborhoods Names](https://geo.nyu.edu/catalog/nyu_2451_34572). It contains four fields: NYC Borough, Neighborhood, Latitude and Longitude. The cleaned DataFrame looks like this:         

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/3.png)

### 3. Fetching NYC Population per Neighborhood from Wikipedia using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

The [Neighborhoods in New York City]("https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City") page from [Wikipedia]("https://en.wikipedia.org") has a list of neighborhoods names and each name contains a anchor tag connecting to its own Wikipedia page, where population data on the right hand side table can be found.      

I use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to fetch each neighborhood name from Wikipedia, and run iteration via requests to visit each page of the neighborhood, and scrap its population data. The DataFrame fetched includes Neighborhood name, its Anchor tag and Population:

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/4.png)        


### 4. Combine NYC Neighborhood Data and Population Data    
Merge NYC neighborhood data with population data and get:      
![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/5.png)   

Here is a box chart of Neighborhood per Borough:    
![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Neighborhood%20per%20Borough.png)

Here is a box chart of Population per Borough:
![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Population%20per%20Borough.png)           

### 5. Fetching Hospital Data per Neighborhood using [Foursquare](https://foursquare.com/) API      

Since we will need to combine hospital beds data with NYC neighborhood data, we need to have each hospital's latitude and longitude information using Foursquare API.     

We run iterations to search for hospitals in each neighborhood based on its latitude and longitude we've collected in step 2 using [Foursquare](https://foursquare.com/) API.

The cleaned dataframe looks like this:         
     
![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/2.png)      

After that we move to combine hospital beds data we collected in step 1 and hospital data per neighborhood collected in this step by matching hospital names using string matching package [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/). 

The combined DataFrame looks like this:        


![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/6.png)

Since we're interested to know hospital beds number per neighborhood and borough, we then group the data by 'Borough' and 'Neighborhood' and sum the number of beds for each neighborhood of borough.     

Now we have dataframe like this:

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/7.png)

Here is a bar chart of Total Beds per Borough: 

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Total%20Beds%20per%20Borough.png)     

Here is a bar chart of Intensive Care Beds per Borough:  

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Intensive%20Care%20Beds%20per%20Borough.png)

Here is a bar chart of Medical/ Surgical Beds per Borough:  

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Medical%20Beds%20per%20Borough.png)


### 6. Integrating Population per Neighborhood and Beds per Neighborhood    

We then join the two tables on neighborhood and borough and get:         

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/8.png)

Since we need to compare each neighborhood's medical care capability with a ratio metric instead of the total number of beds. For this purpose, we add two new columns: Intensive Care Bed Per Hundred People and Bed Per Hundred People. 

The DataFrame looks like this:    

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/9.png)


Here is a bar plot of Total Beds per Hundred per Borough:     

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Total%20Beds%20per%20Hundred%20per%20Borough.png)


Here is a bar plot of Intensive Care Beds per Hundred per Borough:   

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/Intensive%20Care%20Beds%20per%20Hundred%20per%20Borough.png)


### 7. Neighborhood Clustering Analysis

We will use K-means to cluster NYC neighborhoods on their hospital beds per hundred people. 

First we select features for clustering: Population, Intensive Care Bed Per Hundred People and Bed Per Hundred People.    
We then normalize the data since K-Means algorithm requires standardized dataset to calculate distances.     

Then we use elbow method to find the optimum number of clusters and the output optimum number of k is 4.    

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/10.png)

**Examine Clusters** 

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/cluster1.png)    

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/cluster2.png)   

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/cluster3.png)   

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/cluster4.png)     


**Visualize Geo Clusters**   

We use geopy library to get the latitude and longitude values of New York City, and create a NYC map using [folium](https://python-visualization.github.io/folium/).      
Total Beds per Hundred People:       

![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/map1.png)

Intensive Care Beds per Hundred People:


![](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/image_output/map2.png)



## Result and Discussion

Looking into the results of our neighborhoods clusters, we find that cluster 3 only includes one neighborhood: Murray Hill of Manhattan. It has the sufficient beds number and bed density that is extremely higher than other neighborhoods, making it the most equipped neighborhood to fight pandemic.   
Cluster 1 which contains 7 neighborhoods ranks as the second highest in inpatient availability. And the neighborhoods in cluster 2 should be paid more attention as they have the most shortage of beds/intensive care beds for their residents. People who live in these neighborhoods are at the high risk of not being able to receive medical care during pandemic.    

**Limitations**

- We only looked into neighborhoods that have hospital data. However, we should also analyze neighborhood that does not have hospitals. And this group of neighborhoods can be considered an additional cluster of NYC neighborhoods.

- The hospital beds data we collected from New York State [Department of Health](https://profiles.health.ny.gov/hospital) may not include the latest information. 

- The NYC population data we collected from Wikipedia pages are from 2010, that is not very accurate.

- It would be more insightful to include NYC COVID-19 data in our project, if we can get the data about confirmed cases and death numbers of each neighborhoods of New York City.

## Conclusion

This project collected various sources of data, cleaned, transformed and combined these datasets to get helpful insights on the inpatient availability of neighborhoods in New York City. NYC neighborhoods were then grouped into 4 clusters based on their similarities on population, hospital beds per hundred people to indicate their ability in combating pandemics. 


