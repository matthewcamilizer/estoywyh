#pip install mysql-connector-python
import mysql.connector

def tomysql():
  user=input("Enter SQL user: ")
  pw=input("Enter SQL password: ")
  host=input("Enter SQL host: ")
  mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=pw
  )
  print(f"Succesfully connected to {user}@{host}")
  while True:
    try:
      # Create a cursor object to interact with the database
      mycursor = mydb.cursor()
      com=input("Enter SQL commands: ")
      # Execute a SQL query
      mycursor.execute(com)

      num=mycursor.rowcount
      print(f"\nAffected {num} rows\n")

      info=mycursor.fetchwarnings()
      if info:
        for i in info:
          print(i)
      else:
        print("no warnings")

      # Fetch all the rows in the result set
      result = mycursor.fetchall()
      # Print the rows
      for row in result:
        print(row)
      ask=input("y?").lower()
      if ask=='y':
        continue
      else:
        break
    except Exception as e:
      print(f"inner:\n{e}")
      break
  
while True:
  try:
    tomysql()
  
    To=input("out in y?\n").lower()
    if To == 'y':
      continue
    else:
      break
  except Exception as e:
    print(f"out\n{e}")
    To=input("out out y?\n").lower()
    if To == 'y':
      continue
    else:
      break