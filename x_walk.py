#!/usr/bin/python3
__author__ = 'Eric Cartagena'

import pandas as pd
import os
import os.path
import xlrd # Used to handle inproperly formatted .xls(x) files
from pyfiglet import Figlet

# More font styles @ https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts
def banner():
    # Displays banner
    f = Figlet(font='cybermedium')
    print('\n{}'.format(f.renderText('X Walk')))
    print('Welcome to X Walk!\n\n')

def display_menu(lst, cycle, columns=None):
    # Displays the menu depending on what cycle the main function is running
    if cycle == 'files':    # Sorts lst to display if displaying files
        lst.sort()
    for i in range(len(lst)):
        print('{0}) {1}'.format(i + 1, lst[i]))
    if cycle != 'files':
        print('\nb) <- Back to Files\nx) Exit\n')
    else:
        print('\nx) Exit\n')
    if cycle == 'files':
        print('total excel files: {0}\n'.format(len(lst)))
        list_choice = input("Which file do you want to work with?: ")
    elif cycle == 'column to rename':
        print('total columns: {0}\n'.format(len(lst)))
        list_choice = input("Column to rename?: ")
    elif cycle == 'columns to use':
        print('total columns: {0}\n'.format(len(lst)))
        list_choice = input("Column to use: ")
    return list_choice

def farewell():
    # Ending message before user exits the program
    f = Figlet(font='pepper')
    print('\n{}'.format(f.renderText('Until next time...')))
    print('\nThank you for using X Walk\n\nGoodbye!\n')
    exit()

def PromptResponse(main_prompt):
    # prompt the user for a yes or no answer
    response = input(main_prompt)
    while response not in ['y', 'n']:
        print('\nPlease enter a valid response: (y/n)\n')
        response = input(main_prompt)
    return response

def rename(root, file, renamed_files):
    # Renames requested file
    extension = file.split('.')[-1]
    original_index = int(original_files[original_files == file].index[0])
    os.rename(os.path.join(root, file), os.path.join(root, file_names[original_index].strip() + '.' + extension))

def revert(files):
    # Reverts all renamed files and columns to their original names
    for i in range(len(files)):
        if find(files[i], path):
            extension = files[i].split('.')[-1]
            os.rename(os.path.join(path, files[i]), original_files[i] + '.' + extension)

def scan_columns(file):
    # Inserts all columns to columns_list array as str format and returns it
    columns_list = []
    for column in file.columns:
        columns_list.append(column)
    return columns_list

def scan_files(path, format):
    # Inserts all xls(x) files to files_list array as str format and returns it
    files_list = []
    for root, dirs, files in os.walk(path):
        for i in range(len(files)):
            if files[i].startswith('~'): # Does not include ~*.xls(x) files
                continue
            extension = files[i].split('.')[-1]
            if extension in format:
                files_list.append(files[i])
    return files_list

def scan_void(files):
    # Scans every filename for NaN and replaces it with '' string
    # to avoid TypeError while executing the rename function
    for file in files:
        if file.isna():
            file = ''

def walk(path, original_files, renamed_files):
    # Iterates through all files within the path and renames them
    for root, dirs, files in os.walk(path):
        for i in range(len(files)):
            if files[i] in str(original_files):
                rename(root, files[i], renamed_files)

if __name__ == '__main__':
    main_path = os.getcwd()
    # Inserts all xlsx and xls files into excel_files array initiated here
    excel_files = scan_files(main_path, ['xlsx', 'xls'])
    while True: # Inside the main menu = 'files' cycle
        banner()
        # Inform the user and close the program if x_walk scans no excel files
        if len(excel_files) == 0:
            print('There are no excel files work with')
            farewell()
        print('Your excel files:\n')
        file_choice = display_menu(excel_files, 'files')
        if file_choice == 'x':
            farewell()
        try:
            file_choice = int(file_choice)
            if file_choice >= 1 and file_choice <= len(excel_files):
                try:
                    main_file = pd.read_excel(excel_files[file_choice - 1])
                    if not len(main_file):
                        print('\n{0} contains no columns to work with\n'.format(excel_files[file_choice - 1]))
                        input('Press Enter to continue...')
                        continue
                    print('\nyour file choice: {0}\n'.format(excel_files[file_choice - 1]))
                    print('your columns:\n')
                    total_columns = list(main_file)
                    while True: # 'column to rename' cycle
                        try:
                            column_to_rename = display_menu(total_columns, 'column to rename')
                            if column_to_rename == '0':
                                raise ValueError('You cannot enter 0');
                            elif column_to_rename == 'b':
                                print('\n')
                                break
                            elif column_to_rename == 'x':
                                farewell()
                            column_to_rename = int(column_to_rename)
                            print('\n')
                            total_columns = scan_columns(main_file)
                            total_columns.pop(column_to_rename - 1)
                            break
                        except ValueError as e: # exception for column_to_rename not as integer type
                            print('ValueError exception: {0}'.format(e))
                            input('Press Enter to continue...')
                        except IndexError as e: # exception for column_to_rename out of range
                            print('IndexError exception: {0}'.format(e))
                            input('Press Enter to continue...')
                    if column_to_rename == 'b': # redirects user back to the main menu if
                        continue                # user pressed 'b' and skips next cycle
                    # Create a backup of total_columns if the user decides not to rename columns
                    # since the original total_columns array is already modified (popped)
                    total_columns_backup = [value for value in total_columns]
                    columns_to_use = []
                    while True: # 'columns to use' cycle
                        try:
                            column_choice = display_menu(total_columns, 'columns to use')
                            if column_choice == '0':
                                raise ValueError('You cannot enter 0')
                            elif column_choice == 'b':
                                print('\n')
                                break
                            elif column_choice == 'x':
                                farewell()
                            column_choice = int(column_choice)
                            print('\nColumn choice: {0}\n'.format(total_columns[column_choice - 1]))
                            columns_to_use.append(total_columns[column_choice - 1])
                            print('Total columns you\'re using: {0}\n'.format(columns_to_use))
                            user_response = PromptResponse('Use another column (y/n)?: ')
                            if user_response == 'y':
                                if (len(total_columns) - 1) != 0:
                                    total_columns.pop(column_choice - 1)
                                    continue # resume loop starting from the top again
                                else:
                                    print('\nNo more columns to work with!\n')
                                    input('Press Enter to continue...')
                                    break # back to main menu
                            # execute the following code if user_response == 'n'
                            # or if there are no more columns left in the total_columns array
                            file_names = None
                            # Create a copy of your pandas main_file object as file_names
                            for i in range(len(columns_to_use)):
                                if i == 0:
                                    file_names = main_file[columns_to_use[i]].fillna('').copy()
                                    continue
                                file_names += ' ' + main_file[columns_to_use[i]].fillna('')
                            original_files = main_file[list(main_file)[column_to_rename - 1]]
                            original_file = main_file[list(main_file)[column_to_rename - 1]].iloc[0]
                            extension = '.' + original_file.split('.')[-1]
                            user_response = PromptResponse('\nrename files like {0} to {1}?: '.format(original_file, str(file_names[0]).strip() + extension))
                            if user_response == 'n':
                                total_columns = [value for value in total_columns_backup]
                                columns_to_use.clear()
                                continue
                            walk(main_path, original_files, file_names)
                            break
                        except ValueError as e: # exception for column_to_rename not as integer type
                            print('ValueError exception: {0}'.format(e))
                            input('Press Enter to continue...')
                        except IndexError as e: # exception for column_to_rename out of range
                            print('IndexError exception: {0}'.format(e))
                            input('Press Enter to continue...')
                except xlrd.XLRDError as e:
                    # exception for inproperly formatted files
                    # for example:
                    # if you create a file this way without opening Excel:
                    #   touch file.xls(x) -> Excel will not recognize this as an .xls(x) file
                    # ...as compared to just opening Excel and saving the file
                    print('\n{0} is not in the proper .xls(x) format\n'.format(excel_files[file_choice - 1]))
                    input('Press Enter to continue...')
                except FileNotFoundError as e:
                    # If the user deletes a file after x walk scanned it as an available file
                    # it will display to the user the file selected does not exist
                    print('\n{0} was not found. Please choose another file.\n'.format(str(e).split('\'')[1]))
                    input('Press Enter to continue...')
        except ValueError:
            print('\nPlease enter a valid input between {0} and {1}\n'.format(1, len(excel_files)))
            input('Press Enter to continue...')
