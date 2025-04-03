# import os
# import psycopg2
# from psycopg2 import sql
# DATABASE_URL="postgresql://va2pt:passva2pt@172.20.0.2:5432/postgres"
# # DATABASE_URL="postgresql://va2pt:passva2pt@postgres_db:5432/postgres"
# # DATABASE_URL = os.getenv('# put your databse URL over here to communicate with the Database')

# def get_db_connection():
#     return psycopg2.connect(DATABASE_URL)
import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://va2pt:passva2pt@172.18.0.2:5432/va2ptdb")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)
