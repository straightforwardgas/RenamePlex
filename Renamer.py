import os

def main():
    print("Welcome to Jae's renaming program, to rename movie files for Plex")

    #use os to get current directory
    current_directory = os.getcwd()

    menu = True
    file_list = []

    while(menu == True):

        print("\nCurrent working directory " + current_directory)

        question1 = "\n1. Work in this directory"
        question2 = "\n2. Change directory"
        question3 = "\n3. List files in current directory"
        question4 = "\n4. Quit"
        select_option = "\n\nPlease select from the following above, input 1, 2, 3, 4: "

        user_choice = input(question1 + question2 + question3 + question4 + select_option)

        if user_choice == '1':
            file_list.clear()

            dirs = os.listdir(current_directory)

            for file in dirs:
                file_list.append(file)
                
            ChangeName(file_list, current_directory)

        elif(user_choice == '2'):
            current_directory = ChangeDirectory(current_directory)

            print(os.getcwd())

        elif(user_choice == '3'):
            print(os.listdir(current_directory))

        elif(user_choice == '4'):
            menu = False
            print('\nQuitting\n\n')

    return

def ChangeName(original_list, working_directory):
    menu = True
    new_list = []

    while (menu == True):
        print("\nCurrent working directory " + working_directory)

        question1 = '\n1. Insert Season apart of name by finding episode int ex. 01, 02, 03, etc'
        question2 = '\n2. See original list'
        question3 = '\n3. See new list'
        question4 = '\n4. Change name'
        question5 = '\n5. Clear new list (start over)'
        question6 = '\n6. Go back'

        select_option = '\n\nPlease select from the following above, input 1, 2, 3, 4, 5, 6: '

        user_choice = input(question1 + question2 + question3 + question4 + question5 + question6 + select_option)

        if user_choice == '1':
            for file in original_list:
                for i in range(len(file)):
                    if file[i].isdigit() == True:
                        break
                

        
        elif(user_choice == '2'):
            for file in original_list:
                print(file)

        elif(user_choice == '3'):
            print('test')

        elif(user_choice == '4'):
            print('test')

        elif(user_choice == '5'):
            print('test')

        elif(user_choice == '6'):
            print('test')

    return


def ChangeDirectory(working_directory):
    menu = True
    while(menu == True):
        print("\nCurrent working directory " + working_directory)

        question1 = '\n1. Go up one level'
        question2 = '\n2. Manually input full pathname'
        question3 = '\n3. List files in current directory'
        question4 = '\n4. Go back'
        question5 = '\n\nOr input directory name to open: '

        user_choice = input(question1 + question2 + question3 + question4 + question5)

        if user_choice == '1':
            print('go up one level')
            os.path.dirname(os.getcwd())
            working_directory = os.path.dirname(os.path.dirname(os.getcwd()))

        elif(user_choice == '2'):
            working_directory = input("\nPlease insert full pathway now: ")
        
        elif(user_choice == '3'):
            dirs = os.listdir(working_directory)
            for file in dirs:
                print(file)

        elif(user_choice == '4'):
            menu = False
            print('\nGoing back to main menu')

        else:
            print('m')

    return working_directory

if __name__ == "__main__":
    main()