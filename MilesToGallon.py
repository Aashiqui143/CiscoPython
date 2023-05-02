def liters_100km_to_miles_gallon(liters):
    #
    # Write your code here.
    #
    mi=(1/1.61)*100
    ga=liters*(1/3.785411)
    return mi/ga
def miles_gallon_to_liters_100km(miles):
    #
    # Write your code here.
    #
    
    km=(miles*1.61)/100
    li=3.7854
    
    return li/km
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

