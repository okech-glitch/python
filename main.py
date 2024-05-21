# file_handling_assignment.py

def main():
    # File Creation
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: The number is 123.\n")
            file.write("Line 3: Goodbye!\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred during file creation: {e}")

    # File Reading and Display
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
        print("File contents after initial write:")
        print(contents)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred during file reading: {e}")

    # File Appending
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Line 4: Adding more text.\n")
            file.write("Line 5: Appending numbers 456.\n")
            file.write("Line 6: End of the file.\n")
        print("File appended successfully.")
    except Exception as e:
        print(f"An error occurred during file appending: {e}")

    # Read and display the file again to show appended content
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
        print("File contents after appending:")
        print(contents)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred during file reading: {e}")

if __name__ == "__main__":
    main()
