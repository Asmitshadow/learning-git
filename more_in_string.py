language ="python"
version = "3.13.2"

s1 ="4" # it is a string
s2= "6"

s3 = 4 # it is a integer 
s4 = 6

print(language + version)
print( s1 + s2)
print(s3 + s4)

#membership opreator

# in opreator

s1 = "java is more difficult than python"

print("java" in s1)
print("than" in s1)
print("lava" in s1)

# not in opreator

print("lava" not in s1)
print("asmit" not in s1)



# strip function

print ("python" == "python   ")


s1= "print          "

print(s1.strip() == "print")

#s1 = " surprise       its"

#print(s1.strip() == "surpriseits")


# replace function

s1 = "i am learnig "

print(s1)
print(s1.replace("i","we",1))
print(s1.replace("am","are"),s1.replace("i am","we are"))



# count function 
 
s3 = "i am going on a journey of sikkim" \
"with 2 friends , i am telling you this because after that " \
"i start a business ."
s4 = "i"
print(f"we are ready  for this and how many times i use i word {s3.count(s4)} ")


# upper(), lower() ,title() , capitalize()
s3 = "i am going on a journey of sikkim" \
"with 2 friends , i am telling you this because after that " \
"i start a business ."
print(s3.upper())
print(s3.capitalize())
print(s3.lower())
print(s3.title())


# startswith(), endswith()

s9 = " q w e r t y"
print(s9.startswith(" "))
print(s9.endswith("q"))
