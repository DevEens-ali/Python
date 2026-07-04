from tkinter import * 
from PIL import ImageTk, Image  # Fixed capitalization of ImageTk

root = Tk() 
root.title('login form') 
root.geometry('370x520') 

# Note: Ensure 'book-icon.ico' is in the same folder, or comment this line out
# root.iconbitmap('book-icon.ico') 

root.configure(background='#0096DC')  # Fixed hex color format

root.mainloop() 
