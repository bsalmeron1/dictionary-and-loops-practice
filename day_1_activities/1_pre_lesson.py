# this is what we will use for the video intro to dictionaries

#dic= collection of {key:value} pairs prdered and changeable no dupes
capitals={ "USA" : "Washington D.C",
"India" : "New Dehli",
"China" : "Beijing",
"Russia" : "moscow"}

print(capitals.get("USA"))

if capitals.get("China") :
    print ("that capital exists")
else:
        print("That capital doesnt exist")

keys= capitals.keys()
for key in capitals.keys():
      print(key)
#capitals.popitem
#capitals.keys to get them without values
values= capitals.values() #will return value object fro every
for value in capitals.values():
      print(value)

#items method
for key, value in capitals.items():
      print(f"{key}:{value}")