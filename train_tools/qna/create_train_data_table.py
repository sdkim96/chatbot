import mysql.connector
from chatbot.config.DatabaseConfig import * # parent오류생김

cnx = None

try :
    cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, 
                                host=DB_HOST, port=3306, database=DB_NAME, ssl_ca="{ca-cert filename}", 
                                ssl_disabled=False)
    
    sql = """
        CREATE TABLE IF NOT EXISTS chatbot_train_data (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        intent VARCHAR(45) CHARACTER SET utf8mb4 NULL,
        ner VARCHAR(1024) CHARACTER SET utf8mb4 NULL,
        query TEXT CHARACTER SET utf8mb4 NULL,
        answer TEXT CHARACTER SET utf8mb4 NOT NULL,
        answer_image VARCHAR(2048) CHARACTER SET utf8mb4 NULL,
        PRIMARY KEY (id)
    ) CHARACTER SET=utf8mb4;

    """


    with cnx.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if cnx is not None:
        cnx.close()

    