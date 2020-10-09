weight_lb = int(input('How much do you weigh in pounds?'))
weight_kg = weight_lb * .453592


print('Your weight in kilograms is %s', weight_kg)

for years in range(1, 16):
    weight_kg += 1
    print(years, weight_kg)