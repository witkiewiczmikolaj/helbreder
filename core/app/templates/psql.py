import psycopg2
import os

psql_user = os.environ.get('POSTGRES_USER') 
psql_pass = os.environ.get('POSTGRES_PASSWORD') 
psql_ip = os.environ.get('POSTGRES_IP') 
psql_port = os.environ.get('POSTGRES_PORT') 
psql_db_helbreder = 'helbreder'
c = psycopg2.connect(database=psql_db_helbreder, user=psql_user, password=psql_pass, host=psql_ip, port=psql_port)
cur = c.cursor()