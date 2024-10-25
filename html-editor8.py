import tkinter as tk
from tkinter import filedialog, messagebox
import re

def load_html_file():
    global html_content, html_file_path
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            html_file_path = file_path
            messagebox.showinfo("Success", "HTML file loaded successfully.")

def save_html_file():
    global html_content
    if html_content:
        # Replace Company Name
        html_content = re.sub(r'\[company-name\]', company_name_var.get(), html_content)

        # Replace Registration Number
        html_content = re.sub(r'\[reg-number\]', reg_number_var.get(), html_content)

        # Replace Audit Reference Number
        html_content = re.sub(r'\[audit-reference-number\]', audit_ref_var.get(), html_content)

        # Replace Certified Number
        html_content = re.sub(r'\[certified-number\]', cert_number_var.get(), html_content)

        # Replace Effective Date
        html_content = re.sub(r'\[effective-date\]', eff_date_var.get(), html_content)

        # Replace Scope of Certification
        html_content = re.sub(r'\[scope-of-certification\]', scope_var.get(), html_content)

        # Save modified HTML
        output_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(html_content)
            messagebox.showinfo("Success", "HTML file saved successfully.")

# Create Tkinter GUI
root = tk.Tk()
root.title("HTML Editor")

# Variables to store user inputs
company_name_var = tk.StringVar()
reg_number_var = tk.StringVar()
audit_ref_var = tk.StringVar()
cert_number_var = tk.StringVar()
eff_date_var = tk.StringVar()
scope_var = tk.StringVar()

# GUI Layout
tk.Label(root, text="Company Name").grid(row=0, column=0)
tk.Entry(root, textvariable=company_name_var).grid(row=0, column=1)

tk.Label(root, text="Registration Number").grid(row=1, column=0)
tk.Entry(root, textvariable=reg_number_var).grid(row=1, column=1)

tk.Label(root, text="Audit Reference Number").grid(row=2, column=0)
tk.Entry(root, textvariable=audit_ref_var).grid(row=2, column=1)

tk.Label(root, text="Certified Number").grid(row=3, column=0)
tk.Entry(root, textvariable=cert_number_var).grid(row=3, column=1)

tk.Label(root, text="Effective Date").grid(row=4, column=0)
tk.Entry(root, textvariable=eff_date_var).grid(row=4, column=1)

tk.Label(root, text="Scope Of Certification").grid(row=5, column=0)
tk.Entry(root, textvariable=scope_var).grid(row=5, column=1)

# Buttons to load and save HTML
tk.Button(root, text="Load HTML File", command=load_html_file).grid(row=6, column=0)
tk.Button(root, text="Save HTML File", command=save_html_file).grid(row=6, column=1)

root.mainloop()
