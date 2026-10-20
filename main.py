import database_ops
from art import text2art
from termcolor import colored
import inquirer
from prettytable import PrettyTable

def main():
    assci_manner = text2art('TODO TABLE')
    print(colored(assci_manner, 'green'))

    print(" This is my terminal application for managing your tasks. \n")
    print(' Please choose what you want to do : ')

    actions = [
        'create user',
        'create user details',
        'create task',
        'create tag',
        'create task tag',

        'fetch all users',
        'fetch one user',
        'fetch all user details',
        'fetch one user details',
        'fetch all tasks',
        'fetch one task',
        'fetch all tags',
        'fetch one tag',
        'view user details',
        'list tags for task',
        'list tasks for tag',

        'update user',
        'update user details',
        'update task',
        'update tag',
        'update task tag',

        'mark task complete',

        'delete user',
        'delete user details',
        'delete task',
        'delete tag',
        'delete task tag',

        'exit'
    ]

    while True:
        action = inquirer.prompt([
            inquirer.List('action', message='What do you want to do?', choices=actions)
        ])

        if action is None:
            print("No action selected, exiting...")
            break

        choice = action['action'].lower()

        if choice == 'exit':
            print(" Thank you for using the application , Goodbye ! ")
            break

        elif choice == 'create user':
            name = input(' Enter name : ')
            email = input(' Enter email : ')
            database_ops.create_user(name, email)
            print(' User created successfully ')

        elif choice == 'create user details':
            id_user = int(input(' Enter id_user : '))
            phone_number = input(' Enter phone_number : ')
            address = input(' Enter address : ')
            preference = input(' Enter preference : ')
            database_ops.create_user_details(id_user, phone_number, address, preference)
            print(' UserDetails created successfully ')

        elif choice == 'create task':
            id_user = int(input(' Enter id_user : '))
            description = input(' Enter description : ')
            status = input(' Enter status : ')
            due_date = input(' Enter due_date : ')
            database_ops.create_task(id_user, description, status, due_date)
            print(' Task created successfully ')

        elif choice == 'create tag':
            name = input(' Enter name : ')
            database_ops.create_tag(name)
            print(' Tag created successfully ')

        elif choice == 'create task tag':
            id_task = int(input(' Enter id_task : '))
            id_tag = int(input(' Enter id_tag : '))
            database_ops.create_task_tag(id_task, id_tag)
            print(' TaskTag created successfully ')

        elif choice == 'fetch all users':
            users = database_ops.read_users()
            table = PrettyTable(['ID', 'Name', 'Email'])
            table.add_rows(users)
            print(table)

        elif choice == 'fetch one user':
            id_user = int(input(' Enter id_user : '))
            user = database_ops.read_user(id_user)
            if user:
                table = PrettyTable(['ID', 'Name', 'Email'])
                table.add_row(user)
                print(table)
            else:
                print("Record not found.")

        elif choice == 'fetch all user details':
            user_details = database_ops.read_user_details()
            table = PrettyTable(['ID', 'ID_user', 'phone_number', 'address', 'preference'])
            table.add_rows(user_details)
            print(table)

        elif choice == 'fetch one user details':
            id_user_details = int(input(' Enter id_userDetails : '))
            user_details = database_ops.read_user_detail(id_user_details)
            if user_details:
                table = PrettyTable(['ID', 'ID_user', 'phone_number', 'address', 'preference'])
                table.add_row(user_details)
                print(table)
            else:
                print("Record not found.")

        elif choice == 'fetch all tasks':
            tasks = database_ops.read_tasks()
            table = PrettyTable(['ID', 'ID_user', 'description', 'status', 'due_date'])
            table.add_rows(tasks)
            print(table)

        elif choice == 'fetch one task':
            id_task = int(input(' Enter id_task : '))
            task = database_ops.read_task(id_task)
            if task:
                table = PrettyTable(['ID', 'ID_user', 'description', 'status', 'due_date'])
                table.add_row(task)
                print(table)
            else:
                print("Record not found.")

        elif choice == 'fetch all tags':
            tags = database_ops.read_tags()
            table = PrettyTable(['ID', 'name'])
            table.add_rows(tags)
            print(table)

        elif choice == 'fetch one tag':
            id_tag = int(input(' Enter id_tag : '))
            tag = database_ops.read_tag(id_tag)
            if tag:
                table = PrettyTable(['ID', 'name'])
                table.add_row(tag)
                print(table)
            else:
                print("Record not found.")

        elif choice == 'view user details':
            id_user = int(input(' Enter id_user : '))
            user_details = database_ops.view_user_details(id_user)
            if user_details:
                table = PrettyTable(['ID', 'name', 'email', 'phone_number', 'address', 'preference'])
                table.add_row(user_details)
                print(table)
            else:
                print("Record not found.")

        elif choice == 'list tags for task':
            id_task = int(input(' Enter id_task : '))
            tags = database_ops.list_tags_for_task(id_task)
            table = PrettyTable(['name'])
            table.add_rows(tags)
            print(table)

        elif choice == 'list tasks for tag':
            id_tag = int(input(' Enter id_tag : '))
            tasks = database_ops.list_tasks_for_tag(id_tag)
            table = PrettyTable(['description'])
            table.add_rows(tasks)
            print(table)

        elif choice == 'update user':
            id_user = int(input(' Enter id_user : '))
            name = input(' Enter name : ')
            email = input(' Enter email : ')
            database_ops.update_user(id_user, name, email)
            print(' User updated successfully ')

        elif choice == 'update user details':
            id_user_details = int(input(' Enter id_userDetails : '))
            phone_number = input(' Enter phone_number : ')
            address = input(' Enter address : ')
            preference = input(' Enter preference : ')
            database_ops.update_user_details(id_user_details, phone_number, address, preference)
            print(' UserDetails updated successfully ')

        elif choice == 'update task':
            id_task = int(input(' Enter id_task : '))
            description = input(' Enter description : ')
            status = input(' Enter status : ')
            due_date = input(' Enter due_date : ')
            database_ops.update_task(id_task, description, status, due_date)
            print(' Task updated successfully ')

        elif choice == 'update tag':
            id_tag = int(input(' Enter id_tag : '))
            name = input(' Enter name : ')
            database_ops.update_tag(id_tag, name)
            print(' Tag updated successfully ')

        elif choice == 'update task tag':
            id_task = int(input(' Enter id_task : '))
            old_id_tag = int(input(' Enter old id_tag : '))
            new_id_tag = int(input(' Enter new id_tag : '))
            database_ops.update_task_tag(id_task, old_id_tag, new_id_tag)
            print(' TaskTag updated successfully ')

        elif choice == 'mark task complete':
             id_task = int(input(' Enter id_task : '))
             database_ops.mark_task_complete(id_task)
             print(' Task marked as complete ')

        elif choice == 'delete user':
            id_user = int(input(' Enter id_user : '))
            database_ops.delete_user(id_user)
            print(' User deleted successfully ')

        elif choice == 'delete user details':
            id_user_details = int(input(' Enter id_userDetails : '))
            database_ops.delete_user_details(id_user_details)
            print(' UserDetails deleted successfully ')

        elif choice == 'delete task':
            id_task = int(input(' Enter id_task : '))
            database_ops.delete_task(id_task)
            print(' Task deleted successfully ')

        elif choice == 'delete tag':
            id_tag = int(input(' Enter id_tag : '))
            database_ops.delete_tag(id_tag)
            print(' Tag deleted successfully ')

        elif choice == 'delete task tag':
            id_task = int(input(' Enter id_task : '))
            id_tag = int(input(' Enter id_tag : '))
            database_ops.delete_task_tag(id_task, id_tag)
            print(' TaskTag deleted successfully ')

if __name__ == "__main__":
    main()