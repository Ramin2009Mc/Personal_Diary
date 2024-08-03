
import os
import time

directory = 'records'


def slow_print(text : str, end_value : str):
    for char in text:
        print(char, end = end_value, flush=True)
        time.sleep(0.01)


def slow_input(prompt: str) -> str:
    slow_print(prompt, '')
    return input()


def enter_file_contents():
    title = slow_input('Title: ')
    slow_print('Content:\n', '')
    lines = []
    while True:
        text = slow_input('>> ')
        if text == '/exit':
            break
        lines.append(text) 
    content = '\n'.join(lines)
    return title, content


def create_article():
    title, content = enter_file_contents()
    file_name = os.path.join(directory, title + '.txt')
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
                if content == text:
                    return f'File {file_name[8:]} written successfully'
                else:
                    return f'Error writing file {file_name[6:]}'
        else:
            return f'Error: {file_name[8:]} does not exist after writing.'
    except IOError as e:
        return f'Error writing file {file_name[8:]}: {e}'


def view_records_list():
    data = os.listdir(directory)

    if not data:
        print("No records found in the directory.")
        return

    slow_print('\nLIST OF RECORDS\n', '')
    print(*["-" for _ in range(len(max(data)))])
    try:
        for i in range(len(data)):
            print(f'{i+1} | {data[i]}', '')
            print(*["-" for _ in range(len(max(data)))])
    except IOError as e:
        print(e)
        

def read_record(index: int):
    data = os.listdir(directory)
    try:
        index = int(index)
    except ValueError:
        print("Invalid index. Please provide a valid integer index.")
        return
    if index < 1 or index > len(data):
        print("Invalid index. Please provide a valid index.")
        return
    file_name = data[index - 1]
    print(*["-" for _ in range(len(max(data)))])
    slow_print(f'\nTITLE: {file_name[:-4]}\n', '')
    slow_print('CONTENT:\n', '') 
    try:
        with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
            text = file.read()
            slow_print(text, '')
            print('\n')
            print(*["-" for _ in range(len(max(data)))])
    except FileNotFoundError:
        print("File not found.")
    

def delete_record(index : int):
    data = os.listdir(directory)
    try:
        index = int(index)
    except ValueError:
        print("Invalid index. Please provide a valid integer index.")
        return
    if index < 1 or index > len(data):
        print("Invalid index. Please provide a valid index.")
        return
    file_name = data[index - 1]
    print(*["-" for _ in range(len(max(data)))])
    try:
        os.remove(f'{directory + "/" + file_name}')
        print('The deletion was successful.')
    except FileNotFoundError:
        print("File not found.")


def menu():
    help = [' | /create | - create record', ' | /delete | - delete record', 
            ' | /list   | - view record list', ' | /read   | - read record', 
            ' | /help   | - view functions', ' | /clear  | - clear terminal',
            ' | /exit   | - close program']
    while True:
        comm = slow_input('Command Promt> ')
        if comm.lower() == '/help':
            slow_print('\nFUNCTIONS \n', '')
            print(*["-" for _ in range(len(max(help)))])
            for num in range(len(help)):
                slow_print(f'{num+1}){help[num]}', '')
                print('\n')
            print(*["-" for _ in range(len(max(help)))])
        elif comm.lower() == '/clear' : os.system('cls')
        elif comm.lower() == '/exit': break
        elif comm.lower() == '/create': print(create_article())
        elif comm.lower() == '/list': view_records_list()
        elif comm.lower() == '/delete':
            while True:
                ind = input('Index> ')
                if ind.isdigit():
                    break
                else:
                    slow_print('Error', '')
            try:
                delete_record(ind)
            except IndexError:
                print('{e}')
        elif comm.lower() == '/read':
            while True:
                ind = input('Index> ')
                if ind.isdigit():
                    break
                else:
                    slow_print('Error', '')
            try:
                read_record(ind)
            except IndexError:
                print('{e}')
        
        
if __name__ == '__main__':
    menu()