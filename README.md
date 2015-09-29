# Code_Challenge

#Features
1. Python and Bottle framework was used to build the API
2. It give access:
   GET /listings
  It accepts the below parameters to filter data of listings:
  min_price: The minimum listing price in dollars.
  max_price: The maximum listing price in dollars.
  min_bed: The minimum number of bedrooms.
  max_bed: The maximum number of bedrooms.
  min_bath: The minimum number of bathrooms.
  max_bath: The maximum number of bathrooms.
3. It accepts any combination of parameters
4. Response: GeoJSON FeatureCollection of listings
5. It generates 'listings.geojson' file which stores the result. It can be further used to check the output at http://geojson.io

#Improvements
