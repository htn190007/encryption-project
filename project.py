import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog
from tkinter import messagebox

# Function to handle encryption
def encrypt_files():
    secret_key = secret_key_entry.get()
    # encryption stuff


    messagebox.showinfo("Encryption Result", "Files encrypted with the provided secret key")

# Function to handle decryption
def decrypt_files():
    secret_key = secret_key_entry.get()
    # decryption stuff


    messagebox.showinfo("Decryption Result", "Files decrypted with the provided secret key")

# Creating a window
root = tk.Tk()

# For changing the title of the title bar
root.title("title ig")

# To set the dimensions of the window
screen_height = root.winfo_screenheight()
half_height = screen_height // 2
desired_width = int(3/4 * half_height)
root.geometry(f"{desired_width}x{half_height}")  # width x height

# Creating a canvas
canvas = tk.Canvas(root, height=half_height, width=desired_width, bg="LightGray")
canvas.pack()

# Set the family, size, and style of the font
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Creating a label with text and attaching it to the root
label1 = tk.Label(root, text="Select Files", width=20, bg="LightGray")
label1.config(font=bold_font)
canvas.create_window(desired_width // 2, 50, window=label1)

# Function to open a file dialog and display the selected file paths
def open_file_dialog():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        file_label.config(text="Selected Files:\n" + "\n".join(file_paths))

# Create a button to open the file dialog
select_files_button = tk.Button(root, text="Select Files", command=open_file_dialog, relief="flat", borderwidth=0)
select_files_button.config(font=bold_font)
canvas.create_window(desired_width // 2, 100, window=select_files_button)

# Label to display the selected file paths
file_label = tk.Label(root, text="", bg="LightGray", justify="left")
canvas.create_window(desired_width // 2, 150, window=file_label)

# Add a label for the secret key
secret_key_label = tk.Label(root, text="Secret Key:", bg="LightGray")
secret_key_label.config(font=bold_font)
canvas.create_window(desired_width // 2, 200, window=secret_key_label)

# Add an Entry widget for the secret key
secret_key_entry = tk.Entry(root, width=20, relief="flat", borderwidth=0)
canvas.create_window(desired_width // 2, 240, window=secret_key_entry)

# Create an Encrypt button (green) with a flat style
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_files, bg="green", fg="white", relief="flat", borderwidth=0)
encrypt_button.config(font=bold_font)
canvas.create_window(desired_width // 4, 280, window=encrypt_button)

# Create a Decrypt button (red) with a flat style
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_files, bg="red", fg="white", relief="flat", borderwidth=0)
decrypt_button.config(font=bold_font)
canvas.create_window(desired_width // 4 * 3, 280, window=decrypt_button)

root.mainloop()
