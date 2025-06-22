import re
import tkinter as tk
from tkinter import ttk, messagebox

def test_regex():
    pattern = pattern_entry.get()
    text = test_text.get("1.0", tk.END)

    # Clear previous results
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)

    try:
        compiled_pattern = re.compile(pattern)
        matches = list(compiled_pattern.finditer(text))

        if matches:
            for match in matches:
                result_box.insert(tk.END, f"Matched: '{match.group()}' at position {match.start()} to {match.end()}\n")
        else:
            result_box.insert(tk.END, "❌ No matches found.")
    except re.error as e:
        messagebox.showerror("Regex Error", f"Invalid pattern:\n{e}")

    result_box.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("🧪 Regex Tester GUI")

# Fonts and layout
root.geometry("600x500")
root.resizable(False, False)

# Pattern input
ttk.Label(root, text="Regex Pattern:").pack(pady=(10, 0))
pattern_entry = ttk.Entry(root, width=80)
pattern_entry.pack(pady=5)

# Test text input
ttk.Label(root, text="Test Text:").pack(pady=(10, 0))
test_text = tk.Text(root, height=10, width=70)
test_text.pack(pady=5)

# Test button
ttk.Button(root, text="Test Regex", command=test_regex).pack(pady=10)

# Result box
ttk.Label(root, text="Results:").pack()
result_box = tk.Text(root, height=10, width=70, state=tk.DISABLED, bg="#f4f4f4")
result_box.pack(pady=5)

# Start GUI
root.mainloop()
