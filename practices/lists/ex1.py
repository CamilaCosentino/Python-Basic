# Declare an empty list
my_empty_list = []

# Declare a list with more than 5 items
my_five_item_list = ["Alexis","Gomez", "GZ4003", "React.js", "Nodejs","JavaScript","React Native"]

# Find the length of your list
len(my_five_item_list)

# Get the first item, the middle item and the last item of the list
my_five_item_list[0]
my_five_item_list[3]
my_five_item_list[6]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = []
mixed_data_types = ["Camila",23,1.66,"Single", "Nogoyá 3953 1A"]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
it_companies = list()
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])


it_companies[5] = "Samsung"
# Print the list after modifying one of the companies
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Accenture")

# Insert an IT company in the middle of the companies list
it_companies.insert(4,"Oracle")

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4].upper()

# Join the it_companies with a string '#;  '
it_companies.extend("#")

# Check if a certain company exists in the it_companies list.
"Apple" in it_companies

# Sort the list using sort() method 
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)

# Slice out the first 3 companies from the list
slice= it_companies[0:3]

# Slice out the last 3 companies from the 
slice = it_companies[7:10]

# Slice out the middle IT company or companies from the list
slice = it_companies[4:6]

# Remove the first IT company from the list
it_companies.pop(0)

# Remove the middle IT company or companies from the list
it_companies.pop(4)

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ["HTML","CSS","Reactjs","Redux"]
back_end = ["Nodejs","Express","MongoDB"]
join_list = front_end + back_end

# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = join_list.copy()
full_stack.insert(4,"Python")
full_stack.insert(5,"SQL")
print(full_stack)