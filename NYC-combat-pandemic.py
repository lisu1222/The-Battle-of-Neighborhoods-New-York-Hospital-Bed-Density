import pandas as pd
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import time

def get_nyc_neighborhoods():
	with open('newyork_data.json') as json_data:
		newyork_data = json.load(json_data)
	neighborhoods_data = newyork_data['features']

	# instantiate a dataframe
	neighborhoods = pd.DataFrame(columns = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'])
	for data in neighborhoods_data:
    borough = data['properties']['borough'] 
    neighborhood_name = data['properties']['name']
        
    neighborhood_lat = data['geometry']['coordinates'][1]
    neighborhood_lon = data['geometry']['coordinates'][0]
    
    neighborhoods = neighborhoods.append({'Borough': borough,
                                          'Neighborhood': neighborhood_name,
                                          'Latitude': neighborhood_lat,
                                          'Longitude': neighborhood_lon}, ignore_index=True)

    print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(neighborhoods['Borough'].unique()),
        neighborhoods.shape[0]
        )
    )
    return neighborhoods


def get_neighborhood_pop():
	wiki_link = "https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City"
	page = requests.get(wiki_link)
	soup = BeautifulSoup(page.text, 'html.parser')

	neighborhood_pop_df = pd.DataFrame(columns = ['Neighborhood','Anchor'])
    
    neighborhood_list = []
    neighborhood_anchor = []
    for i in range(1,60):
        for element in soup.select("table.wikitable tr")[i].findAll('a')[1:]:
            neighborhood_list.append(element.text)
            neighborhood_anchor.append(element['href'])
            
    neighborhood_pop_df['Neighborhood'] = neighborhood_list
    neighborhood_pop_df['Anchor'] = neighborhood_anchor
    neighborhood_pop_df['Population'] = np.zeros(len(neighborhood_list))

    
    wiki_search = "https://en.wikipedia.org"

    for i, anchor in enumerate(neighborhood_pop_df['Anchor']):
        neighborhood_page = requests.get(wiki_search+anchor)
        soup2 = BeautifulSoup(neighborhood_page.text, 'html.parser')
        table = soup2.select("table.infobox tr")
    
        for j in range(len(table)):
            try:
                if 'Population' in table[j].find('th').text: 
                    neighborhood_pop_df['Population'][i] = int(table[j+1].find('td').text.replace(',', ''))
            except:
                pass 
    
    neighborhood_pop_df = neighborhood_pop_df[neighborhood_pop_df['Population'] != 0]
    neighborhood_pop_df.to_csv('neighborhood_pop.csv', index = False)
    
    return neighborhood_pop_df


def combine_borough_neighborhood_population():
	new_york_data = neighborhoods.merge(neighborhood_pop_df, on = 'Neighborhood', how = 'inner').drop('Anchor', axis =1)
	return new_york_data

def get_hospital_beds():
	ROOT_URL = "https://profiles.health.ny.gov/hospital/view/{}"
	NYM_NYC = [
        103016, 106804, 102908, 103035, 102934, 1256608, 105117, 103009, 102974, 103006, 103041, 105086, 103056, 103086, 102973,
        102970, 102950, 103074, 103008, 103007, 102985, 103012, 106809, 102937, 103068, 102944, 102995, 106803, 102916, 105109,
        102914, 102960, 103038, 106810, 106811, 102961, 102940, 102933, 103078, 254693, 103065, 103021, 103080, 103033, 102919,
        105116, 106825, 103084, 103087, 102989, 102929, 106817, 106819, 103073, 103085, 103025
    ]  # New York Metro: New York City Hospitals' IDs 
	NYM_LI = [
        102999, 103062, 102928, 103002, 102980, 103077, 103049, 103011, 102918, 102965, 102994, 102966, 103069, 1189331, 102926,
        103088, 103045, 103000, 103070, 105137, 103082, 102954, 103072
    ] # New York Metro: Long Iceland Hospitals' IDs
	BRONX = [
        102908, 106804, 105117, 102973, 102950, 106809, 102937, 103068, 102944, 103078, 103087
    ] # New York Metro: Bronx Hospitals' IDs
	QUEENS = [
	102974, 103006, 102912, 103074, 103008, 105109, 102933, 103033, 103084
	] # New York Metro: Queens Hospitals' IDs

	HOSPITALS = list(set(NYM_LI + NYM_NYC + BRONX + QUEENS))
	print('Total hospitals', len(HOSPITALS))

	hospital_data = []
	for val in HOSPITALS:
	    print("Processing hospital id", val)
	    url = ROOT_URL.format(val)
	    driver = webdriver.Chrome()
	    try:
	        driver.get(url)
	        time.sleep(3)
	        driver.find_element_by_xpath('//*[@id="bed-types"]/a').click()
	        name_list = driver.find_elements_by_xpath('.//*[@id="main-content"]/div[2]/div/h2')
	        for name in name_list:
	            hospital_name = name.text
	        
	        table = []
	        for rows in driver.find_elements_by_xpath('//*//*[@id="bed-types"]//tr'):
	            time.sleep(2)
	            row = [item.text for item in rows.find_elements_by_xpath(".//*[self::td]")]
	            table.append(row)
	            
	        data = pd.DataFrame.from_records(table)
	        data.columns = ['Bed_Type', hospital_name]
	        data[hospital_name] = pd.to_numeric(data[hospital_name])
	        hospital_data.append(data)
	  
	    except Exception as e:
	        print(e)
	    driver.quit()
	    
	print('End of scrapping!')
	print(len(hospital_data),'hospitals data scrapped!')

	df = pd.concat(hospital_data, axis = 0, sort = False)
	df = df.groupby('Bed_Type').sum().astype(int).T
	df.index.rename('Hospital', inplace = True)
	final_df = df[['Intensive Care Beds', 'Medical / Surgical Beds', 'Total Beds']].reset_index() 

	return final_df
	df.to_csv('hospital_beds_.csv')
