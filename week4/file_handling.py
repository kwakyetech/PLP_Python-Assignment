# File Handling and Exception Handling Assignment

def read_and_write_file():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file you want to read: ")
    
    try:
        # Try opening the file for reading
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (example: make it uppercase)
        modified_content = content.upper()
        
        # Create a new file to save the modified content
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)
        
        print(f"File has been successfully read and modified content written to '{output_filename}'")
    
    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
