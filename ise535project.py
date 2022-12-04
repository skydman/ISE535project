# importing necessary libraries 
import numpy as np
import pandas as pd
import geopandas as gpd
import folium 

def air_quality():
    df_aqi = pd.read_csv(r'D:\Aakash\School Work\ISE535\New folder\AQI\data_date.csv') # loading the world AQI dataset as a df in pandas
   
    df_aqi2 = df_aqi.groupby('Country', as_index=False).mean()         # 'as_index' used to flatten/unstack the index labels
   
    world_json = r'D:\Aakash\School Work\ISE535\New folder\countries.geojson'   # importing world's GEOjson file
   
    world_map = folium.Map(location= [0,0], zoom_start=1, control_scale=True, min_zoom=0.8)     # creating a base map
   
    threshold_scale = np.linspace(df_aqi2['AQI Value'].min(), df_aqi2['AQI Value'].max(), 6, dtype=int)     # create a numpy array of length 6 and has a linear spacing from the minimum value to max value         
    threshold_scale = threshold_scale.tolist()
    threshold_scale[-1] = threshold_scale[-1] + 1
    
    folium.Choropleth(
        geo_data=world_json,        # extracting countries data from the GeoJSON file
        name='choropleth',          # type of visualization
        data= df_aqi2,              # data to be plotted on basemap
        columns=["Country", "AQI Value"],   
        threshold_scale = threshold_scale,
        key_on="feature.properties.ADMIN",      # pointing folium to the column of geojson(world_json) that matches the location column in tabular data(df_hps_use)
        fill_color="YlOrRd",        # selecting the colorscheme
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="AQI score",
    ).add_to(world_map)
    
    world_map.save("aqi.html")      # saving the plotted map


def happiness_index():          # follows the same procedure as air_quality(), except different data set
    df_hps = pd.read_csv(r'D:\Aakash\School Work\ISE535\New folder\archive (5)\2015.csv')
    
    df_hps_use = df_hps[['Country', 'Happiness Score']]         # extracting the necessary data into another data frame
    
    world_json = r'D:\Aakash\School Work\ISE535\New folder\countries.geojson'
    
    world_map = folium.Map(location= [0,0], zoom_start=1, control_scale=True, min_zoom=0.8)
    
    threshold_scale = np.linspace(df_hps_use['Happiness Score'].min(), df_hps_use['Happiness Score'].max(), 6, dtype=int)
    threshold_scale = threshold_scale.tolist()
    threshold_scale[-1] = threshold_scale[-1] + 1
    
    folium.Choropleth(
        geo_data=world_json,
        name='choropleth',
        data= df_hps_use,
        columns=["Country", "Happiness Score"],
        threshold_scale = threshold_scale,
        key_on="feature.properties.ADMIN",
        fill_color="PuBuGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Happiness index",
    ).add_to(world_map)

    world_map.save("hps.html")

if __name__== '__main__':
    y = input('Please enter "happiness_index" or "air_quality" as input: ')
    if y == "happiness_index":
        happiness_index()
    elif y == "air_quality":
        air_quality()
    else:
        print('Sorry, incorrect input!')



