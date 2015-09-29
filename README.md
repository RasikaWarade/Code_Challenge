# Code_Challenge

#Features
1. Python and Bottle framework was used to build the API

   To run , first install Bottle framework and then pass the CSV file as argument to the program:
   
   python challenge.py listings.csv

2. Access the API as below :
   GET /listings

  It accepts the below parameters to filter data of listings:
  
  min_price: The minimum listing price in dollars.
  
  max_price: The maximum listing price in dollars.
  
  min_bed: The minimum number of bedrooms.
  
  max_bed: The maximum number of bedrooms.
  
  min_bath: The minimum number of bathrooms.
  
  max_bath: The maximum number of bathrooms.
  
3. It accepts any combination of parameters

4. Response: GeoJSON FeatureCollection of 

5. It generates 'listings.geojson' file which stores the result. 
   It can be further used to check the output at http://geojson.io

#Improvements
1. Pagination can be implemented as suggested
2. PUT, DELETE, POST endpoints can be added to further increase the functionality to add or delete a listing
3. A better HTML form can be provided to the user which will take input for the maximum and minimum values for price, bed and bath instead of giving parameters  and redirect the page to get the results
4. Added functionality to get listings based on sq_ft as well
5. The mapping of the GeoJSON response can be displayed at the client side
6. DB can be provided to avoid parsing of the CSV input everytime
