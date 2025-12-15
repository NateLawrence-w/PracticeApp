import _tkinter as tk
from tkinter import filedialog

#Create a window so the image appears inside 
window = tk.Tk()
window.title("Notepad")
window.geometry("600,400")

#Create the text area 
text_area = tk.Text(window, wrap = "word")
text_area.pack(expand=True, fill="both")

# Function to save a file
def save_File():
    file = filedialog.asksaveasfile(
        Defaultextension=".txt",
        filetypes=[("Text Files", ".txt")]
    )
    if file:
        file.write(text_area.get("1.0", tk.END))
        file.close()

def open_file():
    file = filedialog.askopenfile(filetypes=[("Text Files", "'.text")]
    )
    if file:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, file.read())
        file.close
        
# buttons taht the user can use 
save_button = tk.Button(window, text="save", command=save_File)
save_button.pack(side="left", padx=5,pady=5)

open_button = tk.button(window, text="Open", command=open_file)
open_button.pack(side="left", padx=5, pady=5)

window.mainloop