names = ['iman', 'saynab', 'indie']
print(names)

# for item_placeholder in some_collection:
#      code goes here
# for loop = syntaxtic sugar
# iterator is hidden behind for loop
##############################################
#      continue
#    else:
#        print(popped, 'is odd')
#      print(popped, 'doubled is', popped * 2)
names = ['Rod', 'Jane', 'Freddy']
while names:
    popped_name = names.pop()
    if popped_name == 'Bungle':
        break
    print(popped_name)

print("Game Over")
# for name in names:
#     print(name.upper())







####################################################
for item in names:
    print('I am in the for loop')
    print('hello', item)

for number, item in enumerate(names):
    print('Hello number', number, item)

# range function- stop value
for i in range(5):
    print(i)

# range function- start, stop values
for i in range(10,15):
    print(i)

# range function- start, stop , stop values
for i in range(20,30, 2):
    print(i)

print('The End')
