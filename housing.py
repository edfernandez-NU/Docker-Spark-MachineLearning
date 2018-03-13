#! /usr/bin/python

from com.databricks.ml.local import ModelFactory

print("Enter information about the house below.")
bedrooms = float(raw_input('number of bedrooms: '))
bathrooms = float(raw_input('number of bathrooms: '))
sqft_living = float(raw_input('sq footage of living area: '))
sqft_lot = float(raw_input('sq footage of the lot: '))
zipcode = raw_input('zipcode: ')
condition = int(raw_input('condition: '))

input = '{"bedrooms": %f, "bathrooms": %f, "sqft_living": %f, "sqft_lot": %f, "zipcode": "%s", "condition": %i}' % (bedrooms, bathrooms, sqft_living, sqft_lot, zipcode, condition)

localModel = ModelFactory.loadModel("dbfs/mnt/ved-demo/housing/pipeline/")
localModel.setOutputCols("prediction")

pred = localModel.transform(input)
print(pred)

