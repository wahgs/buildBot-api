import mariadb, os

try:
    conn = mariadb.connect(
        user=os.environ["MARIADB_USER"],
        password=os.environ["MARIADB_PASSWORD"],
        host=os.environ["MARIADB_HOST"],
        port=os.environ["MARIADB_PORT"],
        database=os.ennviron["MARIADB_DATABASENAME"]
    )
except Exception as e:
    print(f'couldn\'t connect to the mariadb database: \'{e}\'')

cur = conn.cursor()