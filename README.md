# ISE535project
A small geospatial data analysis project I made for my ISE 535 class.

### Problem statement:

Geospatial data analysis: The goal is to build a choropleth map portraying different parameters to see how a variable varies across a geographical area. 
Currently, I have chosen to create a choropleth map of variables Happiness Index and Air Quality Index solely due to the ease of availability of their data sets. 
However, this approach of code can easily be applied to visualize any other variable with minor changes in the script.


### Data used:

The Happiness Index, Air Quality Index and Countries file are the 3 data sets used in this project.
The Happiness Index and Air Quality Index are data sets in excel file format, and are retrieved from Kaggle.
These files contain happiness and air quality scores of most countries respectively. 
The Countries GeoJSON file contains the geometrical data and co-ordinates of all the countries in the world. This file also was obtained online.


### Python techniques/ libraries used:

This python script uses 3 libraries: NumPy, Pandas and Folium. 
NumPy is used here to take the array of AQI/ Happiness scores and form a threshold scale, by dividing it into 6 equal parts. 
Pandas is used to create data frames in Python using data stored in csv files. 
Furthermore, it is used to manipulate and filter these data sets to extract and plot only the useful information. 
Last but not the least, Folium is used to plot the base map and add the layer of our data in the Choropleth form using its built-in functions.  


### How the code accomplishes the task:

After executing the code, it asks the user for input, whether it wants to see the choropleth of Air Quality Index or The Happiness Score. 
As per user’s decision it saves a ‘.html’ file containing the plotted map.
On the back end, there are 2 separate functions: “happiness_index” and “aqi_index”. 
As per user’s choice the respective function is called and executed. Both the functions work in a similar manner. 
First, a data frame containing necessary information is imported from a csv file using Pandas. 
Then, the data frame is filtered and manipulated to have only the data required to plot the choropleth. 
Next, the geoJSON file containing geometries and coordinates of all the countries is imported into the script. 
Now, a base map is created using the Folium library. Now, our parameter of interest is parsed into threshold scale and divided into 6 equal parts using NumPy. 
This acts as a legend for the chart, on how the different values will be displayed. 
Furthermore, choropleth chart is formed as a layer on top of our previously loaded base map. 
One of the important methods here is the “key_on” method which points Folium to the values of geoJSON file that matches with the corresponding values in our tabular data (imported csv files).
Finally, this map is saved as a “.html” file in the local device. The following is the output of my script. 
Folium base map allows us to zoom in and out quite easily. It also shows you the names of the country at a specific zoom level. 


Output 1:

![Picture1](https://media.github.ncsu.edu/user/27281/files/a703b344-2870-42c5-8044-afbec779ba3b)



Output 2:

![Picture2](https://media.github.ncsu.edu/user/27281/files/b3263ccb-49f5-4279-ac93-dcf220ba459f)
 

### Issues:

The only issue with the current implementation is missing data, which is seen by the black patches in Outputs 1 and 2. 


### There is a lot of potential/ future work that can implemented. To state a few:
1. Currently, there are some missing values in our data set so that can be changed to get a complete picture.
2. Data can be retrieved from more authentic sources to give a better representation the parameter in focus.
3. Various other types of parameters such as walkability index, GDP per capita etc can be plotted using the same code and just modifying the data sets.
4. We can create a Choropleth animation of change in parameters (e.g., AQI) over the past, say 50 years.


### How can any user run this code?

The user only needs latest python version installed in the device. 
The user then can run a code simply by installing the necessary libraries. 
Apart from that the user will need to download the datasets and geoJSON file available in the repository as well. 
The only change user has to make in the script is the location of files. 
However, this can be resolved by linking the datasets in the scripts with a URL directing to the repository in the source code.

