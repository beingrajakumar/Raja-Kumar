
#code refactoring
###   congratulation  ####

#have a help command
def  show_help():
    print("what shoud you pick at the store")
    print("""Enter 'Done'  to stop adding ieam \nEter 'show'  to view your shopping list  \nEnter 'help'  to  to show help command""")

#have a help command
def show_list():
    print("Here is your list")
    for item in shopping_list:
        # print out the list
        print(item)

def add_to_list():
    # add a new item for list
    shopping_list.append(new_item)
    print("ADDED {} list now has {} items".format(new_item,len(shopping_list)))

#make the list to hold onto our item
shopping_list =[]
#print out instraction how to use app

show_help()
while True:
    # ask for new item
    new_item=input(">> ")

    # be able to quit the app
    if new_item == 'Done':
        break
    elif new_item == 'Help':
        show_help()
        continue
    elif new_item== 'Show':
        show_list()
        continue
    add_to_list()






