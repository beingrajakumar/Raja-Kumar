#make the list to hold onto our item
shopping_list =[]
#print out instraction how to use app
print("what shoud you pick at the store")
print("enter 'Done'  to stop adding ieam")
while True:
    # ask for new item
    new_item=input(" ")

    # be able to quit the app
    if new_item == 'Done':
        break

    # add a new item for list
    shopping_list.append(new_item)

print("Here is your list")
for item  in shopping_list:
    # print out the list
    print(item)






