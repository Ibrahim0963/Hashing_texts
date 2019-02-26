#!/usr/bin/python

import hashlib 
print("""
         _      __              __         _ __ 
   _____(_)____/ /_  ___  _____/ /_  ___  (_) /_
  / ___/ / ___/ __ \/ _ \/ ___/ __ \/ _ \/ / __/
 (__  ) / /__/ / / /  __/ /  / / / /  __/ / /_  
/____/_/\___/_/ /_/\___/_/  /_/ /_/\___/_/\__/  
               mit ibrahim                               
""")

text = input("Enter your text : >>> ")
print()

t = hashlib.algorithms_available

print("\t\t\t## You can choose one of this types ##\n\n",t)
print()

Hash_type = input("Enter your hash type : >>>")
ty = hashlib.new(Hash_type)
ty.update(b"text")
print_text = ty.hexdigest()

print("your text has been hashed >> : "+print_text)



