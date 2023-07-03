#pip install mysql-connector-python
import mysql.connector

host=input("Enter SQL host: ")
user=input("Enter SQL user: ")
pw=input("Enter SQL password: ")
db=input("Enter SQL database: ")

while True:
  try:
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=pw,
      database=db
    )
    print(f"Succesfully connected to {host}.{user}.{db}")

    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()
    com=input("Enter SQL commands: ")
# Execute a SQL query
    mycursor.execute(com)

# Fetch all the rows in the result set
    result = mycursor.fetchall()
# Print the rows
    for row in result:
      print(row)
    
  except:
    print(f"Failed to connected to {host}.{user}.{db}")
    break  
