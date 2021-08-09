#1) Create a list of names and use a for loop to output the length of each name (len() ).
names = ['Max', 'Anna', 'Manuel', 'Chris', 'Steven']

for name in names:
    print('#1 -' + name + ' ' + str(len(name)))
#2) Add an if  check inside the loop to only output names longer than 5 characters.
for name in names:
    if len(name) > 5:
        print('#2 -' + name + ' ' + str(len(name)))

#3) Add another if  check to see whether a name includes a “n”  or “N”  character.
for name in names:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print('#3 -' + name + ' ' + str(len(name)))
#4) Use a while  loop to empty the list of names (via pop())
while len(names) >= 1:
    names.pop()
print('#4 -')
print(names)