import psycopg2
import os

def psql_connect_(psql_db):
    psql_user = os.environ.get('POSTGRES_USER')
    psql_pass = os.environ.get('POSTGRES_PASSWORD')
    psql_ip = os.environ.get('POSTGRES_IP')
    psql_port = os.environ.get('POSTGRES_PORT')

    c = psycopg2.connect(database=psql_db, user=psql_user, password=psql_pass, host=psql_ip, port=psql_port)
    cur = c.cursor()

    return c, cur

def drop_connections_(psql_db):
    c, cur = psql_connect_(psql_db)
    cur.execute(f'''SELECT pg_terminate_backend(pg_stat_activity.pid)
        FROM pg_stat_activity
        WHERE pg_stat_activity.datname = '{psql_db}'
        AND pid <> pg_backend_pid();''')
    c.commit()
