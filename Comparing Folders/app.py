import os
import tkinter as tk
from tkinter import filedialog, messagebox

def list_files_in_folder(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(file)
    return file_list

def compare_folders(folder1, folder2):
    files_in_folder1 = set(list_files_in_folder(folder1))
    files_in_folder2 = set(list_files_in_folder(folder2))

    unique_to_folder1 = files_in_folder1 - files_in_folder2
    unique_to_folder2 = files_in_folder2 - files_in_folder1

    return unique_to_folder1, unique_to_folder2

def summarize_folders(folder1, folder2):
    files_count_folder1 = len(list_files_in_folder(folder1))
    files_count_folder2 = len(list_files_in_folder(folder2))

    print(f"Folder 1 ({folder1}) contains {files_count_folder1} files.")
    print(f"Folder 2 ({folder2}) contains {files_count_folder2} files.")

def browse_button(entry):
    filename = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def generate_report():
    folder1_path = entry_folder1.get()
    folder2_path = entry_folder2.get()

    try:
        unique_to_folder1, unique_to_folder2 = compare_folders(folder1_path, folder2_path)

        report = "Files unique to folder 1:\n{}\n\nFiles unique to folder 2:\n{}".format('\n'.join(unique_to_folder1), '\n'.join(unique_to_folder2))
        
        summarize_folders(folder1_path, folder2_path)
        
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, report)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Folder Comparison Tool")

# Labels and Entry fields
label_folder1 = tk.Label(root, text="Folder 1:")
label_folder1.grid(row=0, column=0, padx=5, pady=5)
entry_folder1 = tk.Entry(root)
entry_folder1.grid(row=0, column=1, padx=5, pady=5)
browse_button1 = tk.Button(root, text="Browse", command=lambda: browse_button(entry_folder1))
browse_button1.grid(row=0, column=2, padx=5, pady=5)

label_folder2 = tk.Label(root, text="Folder 2:")
label_folder2.grid(row=1, column=0, padx=5, pady=5)
entry_folder2 = tk.Entry(root)
entry_folder2.grid(row=1, column=1, padx=5, pady=5)
browse_button2 = tk.Button(root, text="Browse", command=lambda: browse_button(entry_folder2))
browse_button2.grid(row=1, column=2, padx=5, pady=5)

# Button to generate report
generate_button = tk.Button(root, text="Generate Report", command=generate_report)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)

# Text widget to display results
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Start the application
root.mainloop()
