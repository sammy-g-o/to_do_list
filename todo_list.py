"""creating a terminal based to-do list"""
list_of_tasks = []

def add_task():
    """adding the taks """
    while True:
        task= input()
        if task == 'q':
            break

        list_of_tasks.append(task)

def show_list():
    """show the list"""
    sn =0
    for l_o_t in list_of_tasks:
        sn +=1
        print(f'{sn}.', l_o_t)

def clear_list():
    """clear the list"""
    list_of_tasks.clear()

while True:
    print('this is a to do list')
    print('click A to create new list')
    print('click D to display the list')
    print('click cl to clear the list')
    options = input()
    if options.upper() == 'A':
        add_task()
    elif options.upper() == 'D':
        show_list()
    elif options.lower() == 'cl':
        clear_list()
    else:
        print('enter one of the options A,D,cl')
