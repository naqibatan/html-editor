import tkinter as tk
from tkinter import filedialog, messagebox
from bs4 import BeautifulSoup

# Load HTML file
def load_html_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            global soup, html_file_path
            soup = BeautifulSoup(file, 'html.parser')
            html_file_path = file_path
            messagebox.showinfo("Success", "HTML file loaded successfully.")

# Save modified HTML file
def save_html_file():
    if soup:
        # Update the HTML with user inputs

        # Update Company Name
        company_name_tag = soup.find('h1', class_='contentheading')
        if company_name_tag:
            company_name_tag.string = company_name_var.get()

        # Update Registration Number
        reg_number_tag = soup.find('h3', text=lambda t: t and 'Registration Number' in t)
        if reg_number_tag:
            br_tag = reg_number_tag.find_next('br')
            if br_tag and br_tag.next_sibling:
                br_tag.next_sibling.replace_with(f"\n{reg_number_var.get()}")

        # Update Audit Reference Number
        audit_ref_tag = soup.find('h3', text=lambda t: t and 'Audit Reference Number' in t)
        if audit_ref_tag:
            br_tag = audit_ref_tag.find_next('br')
            if br_tag and br_tag.next_sibling:
                br_tag.next_sibling.replace_with(f"\n{audit_ref_var.get()}")

        # Update Certified Number
        cert_number_tag = soup.find('h3', text=lambda t: t and 'Certified Number' in t)
        if cert_number_tag:
            br_tag = cert_number_tag.find_next('br')
            if br_tag and br_tag.next_sibling:
                br_tag.next_sibling.replace_with(f"\n{cert_number_var.get()}")

        # Update Effective Date Until
        eff_date_tag = soup.find('h3', text=lambda t: t and 'Effective Date Until' in t)
        if eff_date_tag:
            br_tag = eff_date_tag.find_next('br')
            if br_tag and br_tag.next_sibling:
                br_tag.next_sibling.replace_with(f"\n{eff_date_var.get()}")

        # Update Scope Of Certification
        scope_tag = soup.find('h3', text=lambda t: t and 'Scope Of Certification' in t)
        if scope_tag:
            br_tag = scope_tag.find_next('br')
            if br_tag and br_tag.next_sibling:
                br_tag.next_sibling.replace_with(f"\n{scope_var.get()}")

        # Save modified HTML
        output_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(str(soup))
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

tk.Label(root, text="Effective Date Until").grid(row=4, column=0)
tk.Entry(root, textvariable=eff_date_var).grid(row=4, column=1)

tk.Label(root, text="Scope Of Certification").grid(row=5, column=0)
tk.Entry(root, textvariable=scope_var).grid(row=5, column=1)

# Buttons to load and save HTML
tk.Button(root, text="Load HTML File", command=load_html_file).grid(row=6, column=0)
tk.Button(root, text="Save HTML File", command=save_html_file).grid(row=6, column=1)

root.mainloop()
