import sys,emoji,re


while True:
  try:
    a=input("Enter 'emoji' or 'unicode', or enter 'q' to exit: ").lower()
    if a=="emoji":
      ii=input("Enter a single character to find its unicode (split by a comma): ").split(',')
      p=r"0x([^\W]+)"
      for io in ii:
        i=io.strip()
        try:
          print(f"{i.encode('unicode-escape').decode()}")
        except Exception as e:
          print(e)
          print(f"Invalid input: {io}, is it a single character?")
      break                        
    elif a=="unicode":
      gg=input("Enter unicode, split by a comma: ").split(',')
      for g in gg:
        get=g.strip()[2:]       
        em=f"Invalid unicode: {g}\nformat: \\U000*****"  
        if(len(get)==8):
          try:                
            print(f"{chr(int(get,16))}")
          except exception as e:
            print(e)
            print(em)
        else:
          print(em)
      break
    elif a=="q":
      print("bye")
      break
    else:
      print(f"Invalid input: {a}")
  except Exception as e:
    print(e)
    break
