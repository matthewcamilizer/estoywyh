#pip install mysql-connector-python
import mysql.connector

def tomysql():
  user=input("Enter SQL user: ")
  host=input("Enter SQL host: ")
  pw=input("Enter SQL password: ")
  mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=pw
  )
  print(f"Succesfully connected to {user}@{host}")

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
  
while True:
  try:
    tomysql()
  
    To=input("y?\n").lower()
    if To == 'y':
      continue
    else:
      break
  except Exception as e:
    print(e)
    To=input("y?\n").lower()
    if To == 'y':
      continue
    else:
      break