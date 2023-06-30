import mysql.connector
import pandas as pd
import sqlalchemy


DB_HOST = "sangyongkim.mysql.database.azure.com"
DB_USER = "sdkim96"
DB_PASSWORD = "kbstar9294!"
DB_NAME = "sample"

def DatabaseConfig():
    global DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

# cnx = mysql.connector.connect(user="sdkim96", password="", 
#                                 host="sangyongkim.mysql.database.azure.com", port=3306, database="sample", ssl_ca="{ca-cert filename}", 
#                                 ssl_disabled=False)

