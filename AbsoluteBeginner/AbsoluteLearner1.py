# Convert km to metres and centimeters

km = int(input("Number in km: "))

def converter(km):
    m = km * 1000
    cm = km * 100000
    print("The km in in metres: ", m)
    print("The km in in centi metres: ", cm)
converter(km)
