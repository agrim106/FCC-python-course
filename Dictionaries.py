daysconversion = {
    #key value pairs are defined in dictionaries
    "Som": "monday",
    "Mangal": "tuesday",
    "budh": "wednesday",
    "guru": "thursday",
    "shukra": "friday",
    "shani": "saturday",
    "ravi": "sunday", 
}


print(daysconversion["guru"])
print(daysconversion["ravi"])
print(daysconversion["Mangal"])
print(daysconversion.get("agrim", "Not a valid Day"))