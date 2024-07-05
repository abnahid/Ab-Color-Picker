from tkinter import *
import tkinter.messagebox

# colors -----------------------
co0 = "#444466"  # black
co1 = "#feffff"  # white
co2 = "#004338"


# Function to update the color preview and hexadecimal code
def scale(value):
    r = red_scale.get()
    g = green_scale.get()
    b = blue_scale.get()

    rgb = f'{r}, {g}, {b}'

    hexadecimal = "#%02x%02x%02x" % (r, g, b)
    screen['bg'] = hexadecimal

    color_entry.delete(0, END)
    color_entry.insert(0, hexadecimal)

# Function to copy the hexadecimal code to clipboard
def onclick():
    tkinter.messagebox.showinfo('Color', "Copied Successfully!")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(color_entry.get())
    clip.destroy()


# Initialize main window
window = Tk()
window.geometry("530x205")
window.configure(bg=co1)
window.resizable(width=FALSE, height=FALSE)

# Color preview screen
screen = Label(window, bg=co0, width=40, height=10)
screen.grid(row=0, column=0)

# Frame for RGB sliders
right_frame = Frame(window, bg=co1)
right_frame.grid(row=0, column=1, padx=5)

# Frame for additional controls
down_frame = Frame(window, bg=co1)
down_frame.grid(row=1, column=0, columnspan=2, padx=15)

# Red slider and label
rad = Label(right_frame, text="Rad", bg=co1, fg='red', width=7, anchor=NW, font=("Ivy", 12, "bold"))
rad.grid(row=0, column=0)
red_scale = Scale(right_frame, bg=co1, fg="red", from_=0, to=255, length=150, orient=HORIZONTAL, command=scale)
red_scale.grid(row=0, column=1)

# Green slider and label
green = Label(right_frame, text="Green", bg=co1, fg='green', width=7, anchor=NW, font=("Ivy", 12, "bold"))
green.grid(row=1, column=0)
green_scale = Scale(right_frame, bg=co1, fg="green", from_=0, to=255, length=150, orient=HORIZONTAL, command=scale)
green_scale.grid(row=1, column=1)

# Blue slider and label
blue = Label(right_frame, text="Blue", bg=co1, fg='blue', width=7, anchor=NW, font=("Ivy", 12, "bold"))
blue.grid(row=2, column=0)
blue_scale = Scale(right_frame, bg=co1, fg="blue", from_=0, to=255, length=150, orient=HORIZONTAL, command=scale)
blue_scale.grid(row=2, column=1)

# Hexadecimal code display and copy button
rgb_label = Label(down_frame, text="HEX CODE", bg=co1, anchor=NW, font=("Ivy", 10, "bold"))
rgb_label.grid(row=0, column=0, pady=5)

color_entry = Entry(down_frame, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
color_entry.grid(row=0, column=1, padx=5)

copy_button = Button(down_frame, text="Copy color", bg=co1, font=("Ivy", 10, "bold"), command=onclick)
copy_button.grid(row=0, column=2, padx=5)

app_name = Label(down_frame, text="Ab Color Picker", bg=co1, font=("Ivy", 15, "bold"))
app_name.grid(row=0, column=3, padx=40)

window.mainloop()
