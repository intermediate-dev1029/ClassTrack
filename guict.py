import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
connection = sqlite3.connect("CTdatabase.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS TempInfo (name TEXT, percentage INTEGER)")
connection.commit()

# Function to insert data


def insert_data():
    name = entry_name.get()
    percentage = entry_percentage.get()

    if name and percentage.isdigit():
        cursor.execute(
            "INSERT INTO TempInfo (name, percentage) VALUES (?, ?)", (name, int(percentage)))
        connection.commit()
        messagebox.showinfo("Success", "Data successfully stored!")
        entry_name.delete(0, tk.END)
        entry_percentage.delete(0, tk.END)
    else:
        messagebox.showerror(
            "Error", "Please enter a valid name and percentage.")

# Function to fetch and display data


def view_data():
    cursor.execute("SELECT * FROM TempInfo")
    rows = cursor.fetchall()

    if rows:
        data_text.delete("1.0", tk.END)
        for row in rows:
            data_text.insert(tk.END, f"Name: {row[0]}, Percentage: {row[1]}\n")
    else:
        messagebox.showinfo("Info", "No data found!")

# Function to delete a student record


def delete_data():
    name = entry_name.get()
    percentage = entry_percentage.get()

    if name and percentage.isdigit():
        cursor.execute(
            "DELETE FROM TempInfo WHERE name = ? AND percentage = ?", (name, int(percentage)))
        connection.commit()
        messagebox.showinfo("Success", "Data deleted successfully!")
        entry_name.delete(0, tk.END)
        entry_percentage.delete(0, tk.END)
    else:
        messagebox.showerror(
            "Error", "Please enter a valid name and percentage.")


# GUI Setup
root = tk.Tk()
root.title("ClassTrack - Student Database")
root.geometry("400x400")

# Labels and entry fields
tk.Label(root, text="ClassTrack - Student Database",
         font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Percentage:").grid(row=1, column=0, padx=5, pady=5)
entry_percentage = tk.Entry(frame)
entry_percentage.grid(row=1, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=insert_data).pack(pady=5)
tk.Button(root, text="View Students", command=view_data).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_data).pack(pady=5)

# Text area to display data
data_text = tk.Text(root, height=8, width=40)
data_text.pack(pady=5)

# Close database connection when closing window


def on_closing():
    connection.commit()
    connection.close()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
