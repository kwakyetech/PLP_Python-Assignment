# File Handling and Exception Handling Assignment

## Overview
This project demonstrates basic file handling and exception handling in Python.  
It includes two main tasks:

1. **File Read & Write Challenge 🖋️**  
   - Reads an input file.  
   - Modifies the content (converts text to uppercase).  
   - Writes the modified content to a new file.  

2. **Error Handling Lab 🧪**  
   - Prompts the user for a filename.  
   - Handles errors gracefully if the file does not exist, cannot be opened, or any other issue occurs.  

## Features
- Reads text from a user-specified file.
- Creates a new file (`modified_<filename>`) containing modified content.
- Handles common errors using `try-except` blocks:
  - `FileNotFoundError`  
  - `PermissionError`  
  - Generic `Exception`

## How to Run
1. Clone or download this project.  
2. Create a sample text file in the same folder, e.g., `example.txt`.  
3. Run the Python script:  

   ```bash
   python file_handling.py
