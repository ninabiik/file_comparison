import tkinter as tk
from tkinter import filedialog
import os
from diff_match_patch import diff_match_patch

def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            dmp = diff_match_patch()
            diffs = dmp.diff_main(content1, content2)
            dmp.diff_cleanupSemantic(diffs)

            diff_html = dmp.diff_prettyHtml(diffs)
            return diff_html

    except FileNotFoundError:
        return "One or both files were not found."

# def compare_files(file1_path, file2_path):
#     try:
#         with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#             content1 = file1.read()
#             content2 = file2.read()
#
#             if content1 == content2:
#                 return "Both files have identical content."
#             else:
#                 # Use difflib to generate differences
#                 d = difflib.Differ()
#                 diff = list(d.compare(content1.splitlines(), content2.splitlines()))
#                 return '\n'.join(diff)
#     except FileNotFoundError:
#         return "One or both files were not found."

def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()

def browse_file(entry_widget):
    file_path = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)

def clear_fields():
    file1_entry.delete(0, tk.END)
    file2_entry.delete(0, tk.END)
    result_label.config(text="")

def compare_button_clicked():
    file1_path = file1_entry.get()
    file2_path = file2_entry.get()

    file1_extension = get_file_extension(file1_path)
    file2_extension = get_file_extension(file2_path)

    if file1_extension in {'.txt', '.csv', '.dat', '.json','.xml'} and file2_extension in {'.txt', '.csv', '.dat','.json','.xml'}:
        result = compare_files(file1_path, file2_path)
        result_label.config(text=result)
    else:
        result_label.config(text="Unsupported file format. Please provide two text (.txt), CSV (.csv), or DAT (.dat) files for comparison.")

# Create the main window
root = tk.Tk()
root.title("File Comparison Tool")
root.geometry("300x150")

# Create and configure the widgets
file1_label = tk.Label(root, text="File 1:")
file1_label.grid(row=0, column=0, sticky=tk.W)

file1_entry = tk.Entry(root)
file1_entry.grid(row=0, column=1)

file1_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(file1_entry))
file1_browse_button.grid(row=0, column=2)

file2_label = tk.Label(root, text="File 2:")
file2_label.grid(row=1, column=0, sticky=tk.W)

file2_entry = tk.Entry(root)
file2_entry.grid(row=1, column=1)

file2_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(file2_entry))
file2_browse_button.grid(row=1, column=2)

compare_button = tk.Button(root, text="Compare", command=compare_button_clicked)
compare_button.grid(row=2, column=0, columnspan=2)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=2, column=2)

result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=3, columnspan=3)

# Start the GUI event loop
root.mainloop()

# import os
# import tkinter as tk
# from tkinter import filedialog
# import difflib
#
# def compare_files(file1_path, file2_path):
#     try:
#         with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#             content1 = file1.read()
#             content2 = file2.read()
#
#             if content1 == content2:
#                 return "Both files have identical content."
#             else:
#                 return "Files have different content."
#
#     except FileNotFoundError:
#         return "One or both files were not found."
#
# def get_file_extension(file_path):
#     _, extension = os.path.splitext(file_path)
#     return extension
#
# def browse_file1():
#     file_path = filedialog.askopenfilename()
#     file1_entry.delete(0, tk.END)
#     file1_entry.insert(0, file_path)
#
# def browse_file2():
#     file_path = filedialog.askopenfilename()
#     file2_entry.delete(0, tk.END)
#     file2_entry.insert(0, file_path)
#
# def clear_fields():
#     file1_entry.delete(0, tk.END)
#     file2_entry.delete(0, tk.END)
#     result_label.config(text="")
#
# def compare_button_clicked():
#     file1_path = file1_entry.get()
#     file2_path = file2_entry.get()
#
#     file1_extension = get_file_extension(file1_path).lower()
#     file2_extension = get_file_extension(file2_path).lower()
#
#     if file1_extension in {'.txt', '.csv', '.dat'} and file2_extension in {'.txt', '.csv', '.dat'}:
#         result = compare_files(file1_path, file2_path)
#         result_label.config(text=result)
#     else:
#         result_label.config(text="Unsupported file format. Please provide two text (.txt), CSV (.csv), or DAT (.dat) files for comparison.")
#
# # Create the main window
# root = tk.Tk()
# root.title("File Comparison Tool- Versent/karenina.comia")
# root.geometry("300x100")
#
# # Create and configure the widgets
# file1_label = tk.Label(root, text="File 1:")
# file1_label.grid(row=0, column=0, sticky=tk.W)
#
# file1_entry = tk.Entry(root)
# file1_entry.grid(row=0, column=1)
#
# file1_browse_button = tk.Button(root, text="Browse", command=browse_file1)
# file1_browse_button.grid(row=0, column=2)
#
# file2_label = tk.Label(root, text="File 2:")
# file2_label.grid(row=1, column=0, sticky=tk.W)
#
# file2_entry = tk.Entry(root)
# file2_entry.grid(row=1, column=1)
#
# file2_browse_button = tk.Button(root, text="Browse", command=browse_file2)
# file2_browse_button.grid(row=1, column=2)
#
# compare_button = tk.Button(root, text="Compare", command=compare_button_clicked)
# compare_button.grid(row=3, column=2)
#
# clear_button = tk.Button(root, text="Clear", command=clear_fields)
# clear_button.grid(row=3, column=3)
#
# result_label = tk.Label(root, text="")
# result_label.grid(row=5, columnspan=3)
#
# # Start the GUI event loop
# root.mainloop()
