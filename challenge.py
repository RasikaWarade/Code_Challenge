from bottle import Bottle, route, run,template, error, post, get, static_file, abort, redirect, response, request,time
import csv
import sys
import json
 
@route('/')
@route('/listings',method='GET')
def read_listings():
	min_price = request.query.min_price or '1'
	max_price = request.query.max_price or str(sys.maxint)
	min_bed = request.query.min_bed or '1'
	max_bed = request.query.max_bed or str(sys.maxint)
	min_bath = request.query.min_bath or '1'
	max_bath = request.query.max_bath or str(sys.maxint)
	
	# Template to format csv to GeoJSON
	template = \
	'''\
	    {
      "type": "Feature",
      "properties": {
        "id": %s,
		"price": %s,
        "street": "%s",
        "bedrooms": %s,
        "bathrooms": %s,
        "sq_ft": %s
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          %s,
          %s
        ]
      }
    },
	'''
	
	# HEAD of GeoJSON file
	output = \
	'''\
{
  "type": "FeatureCollection",
  "features": [
  '''
		
	f=open(sys.argv[1],'rt')
	iterator=1
	try:
		reader = csv.reader(f)
		for row in reader:
			iterator += 1 #ignore first row
			if iterator > 2:
				#Read the columns
				id = row[0]
				street = row[1]
				price = row[3]
				bed = row[4]
				bath = row[5]
				sqft=row[6]
				lat=row[7]
				lang=row[8]
				
				if float(bed) >= float(min_bed) and float(bed) <= float(max_bed) and float(bath) >=float(min_bath) and float(bath) <=float(max_bath) and float(price) >= float(min_price) and float(price) <= float(max_price):
					output += template % ( id, price, street,bed,bath,sqft,lang,lat)
				
	finally:
		f.close()
		
	#removing the extra comma character from the template
	output = output[:-3]
	# Tail of GeoJSON file
	output += \
	'''
	]
}
	'''
	# Opens an GeoJSON file to write the output to
	outFileHandle = open("listings.geojson", "w")
	outFileHandle.write(output)
	outFileHandle.close()

	return '<h5>%s</h5>' % (output)

	

@error(404)
def err404(code):
    return '404 error!'
	
run(host='localhost', port=8080, debug=True)