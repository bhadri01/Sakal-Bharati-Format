# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from tkinter import filedialog


def format_text():
    # Get input text from the text area
    input_text = input_text_area.get("1.0", tk.END)

    # List of replacements (as in your original example)
    replacements = [
        {"oldText": "கொ", "newText": "கொ"},
        {"oldText": "ஙொ", "newText": "ஙொ"},
        {"oldText": "சொ", "newText": "சொ"},
        {"oldText": "ஞொ", "newText": "ஞொ"},
        {"oldText": "டொ", "newText": "டொ"},
        {"oldText": "ணொ", "newText": "ணொ"},
        {"oldText": "தொ", "newText": "தொ"},
        {"oldText": "நொ", "newText": "நொ"},
        {"oldText": "பொ", "newText": "பொ"},
        {"oldText": "மொ", "newText": "மொ"},
        {"oldText": "யொ", "newText": "யொ"},
        {"oldText": "ரொ", "newText": "ரொ"},
        {"oldText": "லொ", "newText": "லொ"},
        {"oldText": "வொ", "newText": "வொ"},
        {"oldText": "ழொ", "newText": "ழொ"},
        {"oldText": "ளொ", "newText": "ளொ"},
        {"oldText": "றொ", "newText": "றொ"},
        {"oldText": "னொ", "newText": "னொ"},
        {"oldText": "கோ", "newText": "கோ"},
        {"oldText": "ஙோ", "newText": "ஙோ"},
        {"oldText": "சோ", "newText": "சோ"},
        {"oldText": "ஞோ", "newText": "ஞோ"},
        {"oldText": "டோ", "newText": "டோ"},
        {"oldText": "ணோ", "newText": "ணோ"},
        {"oldText": "தோ", "newText": "தோ"},
        {"oldText": "நோ", "newText": "நோ"},
        {"oldText": "போ", "newText": "போ"},
        {"oldText": "மோ", "newText": "மோ"},
        {"oldText": "யோ", "newText": "யோ"},
        {"oldText": "ரோ", "newText": "ரோ"},
        {"oldText": "லோ", "newText": "லோ"},
        {"oldText": "வோ", "newText": "வோ"},
        {"oldText": "ழோ", "newText": "ழோ"},
        {"oldText": "ளோ", "newText": "ளோ"},
        {"oldText": "றோ", "newText": "றோ"},
        {"oldText": "னோ", "newText": "னோ"},
        {"oldText": "கௌ", "newText": "கெள"},
        {"oldText": "ஙௌ", "newText": "ஙெள"},
        {"oldText": "சௌ", "newText": "செள"},
        {"oldText": "ஞௌ", "newText": "ஞெள"},
        {"oldText": "டௌ", "newText": "டெள"},
        {"oldText": "ணௌ", "newText": "ணெள"},
        {"oldText": "தௌ", "newText": "தெள"},
        {"oldText": "நௌ", "newText": "நெள"},
        {"oldText": "பௌ", "newText": "பெள"},
        {"oldText": "மௌ", "newText": "மெள"},
        {"oldText": "யௌ", "newText": "யெள"},
        {"oldText": "ரௌ", "newText": "ரெள"},
        {"oldText": "லௌ", "newText": "லெள"},
        {"oldText": "வௌ", "newText": "வெள"},
        {"oldText": "ழௌ", "newText": "ழெள"},
        {"oldText": "ளௌ", "newText": "ளெள"},
        {"oldText": "றௌ", "newText": "றெள"},
        {"oldText": "னௌ", "newText": "னெள"},
    ]

    # Apply replacements to decoded text
    formatted_text = input_text
    for replacement in replacements:
        formatted_text = formatted_text.replace(
            replacement["oldText"], replacement["newText"])

    # Display the formatted text in the output text area
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, formatted_text)

    # Save the formatted text to a text file
    save_to_file(formatted_text)


def save_to_file(text):
    # Open file dialog to choose the location and name of the text file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
                                             ("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
        messagebox.showinfo("Info", f"Text successfully saved to {file_path}")


def clear_text():
    input_text_area.delete("1.0", tk.END)
    output_text_area.delete("1.0", tk.END)


def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text_area.get("1.0", tk.END))
    messagebox.showinfo("Info", "Text copied to clipboard!")


# Initialize main window
root = tk.Tk()
root.title("Sakal Bharati Format")

# Define GUI elements with the loaded Latha font
input_text_area = tk.Text(root, height=10, width=40)
input_text_area.pack(pady=(10, 5))

# Create a frame to hold the "Convert Text" button
convert_frame = tk.Frame(root)
convert_frame.pack(pady=5)

convert_button = tk.Button(
    convert_frame, text="Convert Text", command=format_text)
convert_button.pack()

output_text_area = tk.Text(root, height=10, width=40)
output_text_area.pack(pady=(5, 10))

# Create a frame for the "Clear Text" and "Copy Text" buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

clear_button = tk.Button(btn_frame, text="Clear Text", command=clear_text)
clear_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(btn_frame, text="Copy Text", command=copy_text)
copy_button.grid(row=0, column=1, padx=5)

# Start the Tkinter main loop
root.mainloop()
