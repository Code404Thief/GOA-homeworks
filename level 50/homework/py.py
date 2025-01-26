try:
    print(car_price)
except NameError:
    print("the cars price has not yet been set")

top_grades = [6, 8, 9]
try:
    print(top_grades[7])
except IndexError:
    print("no kid has gotten 7/10")
