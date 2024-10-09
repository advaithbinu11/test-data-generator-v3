import tkinter as tk
from tkinter import filedialog, messagebox
import os
import logging
from PIL import ImageTk, Image
from proccessing import process 
# Custom function to process the input file, output folder, and output file name
def process_file(input_file, output_folder, output_file_name):
    # Example: Display the file path and output details (replace with actual logic)
    output_file_path = os.path.join(output_folder, output_file_name)
    print(f"Processing file: {input_file}")
    print(f"Saving output to: {output_file_path}")
    logging.basicConfig(filename=output_file_path+".log", level=logging.INFO)
    # Process logic using input_file, output_folder, and output_file_name
    logging.info("Saving File")
    #file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
    filepath = process(input_file,output_file_path)

# Function to open file dialog and select input file
def select_input_file():
    file_path = filedialog.askopenfilename(title="Select Input File")
    if file_path:
        input_file_var.set(file_path)


# Function to open folder dialog and select output folder
def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    if folder_path:
        output_folder_var.set(folder_path)


# Function to run the custom script
def run_script():
    input_file = input_file_var.get()
    output_folder = output_folder_var.get()
    output_file_name = output_file_name_var.get()

    if not input_file or not output_folder or not output_file_name:
        messagebox.showwarning("Missing Information",
                               "Please select an input file, output folder, and enter an output file name.")
        return

    # Calling core function
    process_file(input_file, output_folder, output_file_name)
    messagebox.showinfo("Success", "Script executed successfully!")


# Main window
root = tk.Tk()
root.title("Test data Generator")
tk.Label(root, text="""Example JSON input:""").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="""{"tests":350, "regex": {"user_id":"\\d*","email_address": "\\w{8,15}@gmail.com",
    "Groupname":"[ABCDEFG]","phone_number": "\\d{10}",
    "birth_date": "\\d{4}-\\d{2}-\\d{2}","postal_code": "\\d{5}"}}""").grid(row=0, column=1, padx=10, pady=10)

# Variables to store the file path, folder path, and file name
input_file_var = tk.StringVar()
output_folder_var = tk.StringVar()
output_file_name_var = tk.StringVar()

# Input file section
tk.Label(root, text="Input File with Reg expressions:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_file_var, width=40).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_file).grid(row=1, column=2, padx=10, pady=10)

# Output folder section
tk.Label(root, text="Output Folder:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_folder_var, width=40).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=2, column=2, padx=10, pady=10)

# Output file name section
tk.Label(root, text="Output File Name:").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_file_name_var, width=40).grid(row=3, column=1, padx=10, pady=10)

# Run button
tk.Button(root, text="Generate test data", command=run_script, width=20).grid(row=4, column=1, pady=20)

# Start the GUI loop
root.mainloop()