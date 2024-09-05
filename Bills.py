import mysql.connector

connection = mysql.connector.connect(
    host='138.68.140.83',        
    database='dbVarsha', 
    user='varsha',     
    password='Varsha@123'  
    )

if connection.is_connected():
    print("Successfully connected to the database\n")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Item") 
rows = cursor.fetchall()
print("Item table:")
for row in rows:
    print(row)

cursor.close()
connection.close()
