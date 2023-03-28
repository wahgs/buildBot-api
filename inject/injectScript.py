import os, sys, time, json
import "./weaponObjectTemplate.json"

#this script is so you can inject sample data into a database instance for testing

#connects to the database using environmentally stored variables.
conn = mariadb.connect(
    user=os.environ["MARIADB_USER"],
    password=os.environ["MARIADB_PASSWORD"],
    host=os.environ["MARIADB_HOST"],
    port=os.environ["MARIADB_PORT"],
    database=os.environ["MARIADB_HOST"]
)
print("Connection ok, moving forward.")
cur = conn.cursor()

#imports the json object

cur.commit()