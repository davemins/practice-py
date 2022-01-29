def std_weight(height, gender):
    if gender == "man":
        standard_weight = height ** 2 * 0.0001 * 22
    else:
        standard_weight = height ** 2 * 0.0001 * 21
    
    return standard_weight

height = 175
gender = "man"

standard_weight = round(std_weight(height, gender), 2)
print("The standard weight of a {} who tall {}cm is {}kg.".format(gender, height, standard_weight))

