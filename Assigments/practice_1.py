#1 Create two variables – one with your name and one with your age
name = 'Pamela'
age = 22

#2 Create a function which prints your data as one string
def display_data():
    print(name + " " + str(age))

#3 Create a function which prints ANY data (two arguments) as one string
def display_random_data(data1, data2):
    print(str(data1) + " " + str(data2))

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def calculate_decades(years):
    decades = int(years/10)
    return decades

display_data()
display_random_data(1, "hola")
print(calculate_decades(23))