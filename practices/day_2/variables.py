
# Exercises: Level 1

first_name = "Camila"

last_name ="Cosentino"
full_name ="Camila Cosentino"
country = "Argentina"
city ="Buenos Aires"
age = 22
year = 2023
is_married = False
is_true = True
is_light = False

phone_number, andress, town, height, width = 1560331566, "Nogoyá 3953", "Villa Devoto",1.66, 57



# Exercises: Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(phone_number))
print(type(andress))
print(type(town))
print(type(height))
print(type(width))


print("Firstname length is:", len(first_name), "and lastname length is:", len(last_name))

num_one = 5
num_two = 4
total_num = num_one +  num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
exp = num_two**num_one
floor_division= num_one // num_two

circle_radio = 30
area_of_circle = 3.14 * circle_radio **2
diam = circle_radio *2
circum_of_circe = 3.14 * diam

area_input_value = input("Introduce a inter number: ")
int_value = int(area_input_value)
print(type(int_value))
area_input_result = 3.14 * int_value **2

print(area_input_result)
first_name_input = input("What is your name? ")
last_name_input = input("What is your surname? ")
country_input = input("Where are you from? ")
age_input = input("How old are you? ")
print(f'My name is {first_name_input} {last_name_input}, i born in {country_input} and i am {age} years old')
# help("keywords")