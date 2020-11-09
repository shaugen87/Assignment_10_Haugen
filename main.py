import os
import time


def main():
    print("Welcome to the file creator.")

    directory = input("Enter the directory you wish to save the file in: ")
    p = 0
    while p < 3:
        time.sleep(0.3)
        print("...\n")
        p += 1

    if os.path.isdir(directory):
        file_list = os.listdir(directory)
        print("Directory found. Files in current user directory: ")
        print(file_list)
        print()
        time.sleep(1)

        file_name = input("Enter new file name: ")
        user_name = input("Enter user name: ")
        user_address = input("Enter user address: ")
        phone_number = input("Enter user phone number: ")

        print()
        p = 0

        while p < 3:
            time.sleep(0.3)
            print("...\n")
            p += 1

        new_file = open(os.path.join(directory, file_name), 'w')
        new_file.write(user_name + ', ' + user_address + ', ' + phone_number + '\n')
        new_file.close()

        time.sleep(1)
        print("New file created successfully.\n Contents of new file: ")

        read_file = open(os.path.join(directory, file_name), "r")
        for line in read_file:
            print(line)

        read_file.close()

        while True:
            user_selection = input("Press 1 to create a new file or 2 to exit. \n")

            if user_selection == "1" :
                main()
            if user_selection == "2" :
                print("Thank you. Goodbye!")
                exit()
            else:
                print("Invalid selection.")
                continue
    else:
        print("Invalid directory selected. Please check if you path name is correct.")


main()
