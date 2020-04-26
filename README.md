# The Battle of Neighborhoods - New York Hospital Bed Density

## Project Motivation        

Are the hospitals near me ready for Coronavirus?              
Until April 25th, the confirmed COVID-19 cases in New York City have reached 150,000 and the confirmed deaths 10,961. New York City State now has more COVID-19 cases than any single coutry outside the US, according to latest figures.      

This project was motivated by the current national battle to beat the pandemic. It aims to analyze the hospital bed density for each neighborhood in the five boroughs of New York City.     
Hospital Bed Density provides the number of hospital beds per 1,000 people; It serves as a general measure of inpatient service availability, especially in  the battles to beat pandemic. Hospital beds include inpatient beds available in public, private, general, and specialized hospitals and rehabilitatiion centers. Because the level of inpatient services required depends on several factors - such as demographic issues and the burden of disease - there is no global target for the number of hospital beds percountry. In United States, the hospital bed density is measured as 2.9 beds per 1,000 people.        


## Data Source

1. NYC Hospital Data ([hospital_beds.csv](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/hospital_beds.csv)) was scrapped from New York State [Department of Health](https://profiles.health.ny.gov/hospital). It contains hospital name, bed type and the corresponding bed numbers in each type. 76 hospitals data in NYC are collected.


2. [NYC Neiborhood Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/newyork_data.json)) is a json file dowloaded from [New York City Neighborhoods Names](https://geo.nyu.edu/catalog/nyu_2451_34572). After cleaning and transorming, it includes latitude and longitude for each neighborhood of the 5 boroughs in NYC.

3. [NYC Population Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/data_output/new_york_data.csv) includes population data per neighborhood that were scrapped from Wikipedia, and then integrated with [New York Neiborhood Data](https://github.com/lisu1222/The-Battle-of-Neighborhoods-New-York-Hospital-Density/blob/master/newyork_data.json)). It has 5 fileds: Borough, Neighborhood, Population, Longitude and Latitude.



