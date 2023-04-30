# buildBot-data-api
 RESTful API for buildBot's database - written in python flask

environment variables required:

MONGO_URI: connection string to the mongodb database





imports:
mongo, flask,


for json object references - refer to the jsons folder in the repository. PLEASE take note of the types of the values to the keys - they are validated in mongodb



#for you own usage - change 0.0.0.0 to the api's connection information
usage:

0000.api/inject-weapon - post request with json object following the weapon format

0000.api/inject-build - post requrest with json object following the build foramt


inject-weapon:

