# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width = 500, height = 500)
#
# button1 = Button(frame, text = 'button 1')
# button2 = Button(frame, text = 'button 2')
# button3 = Button(frame, text = 'button 3')
#
# button1.pack(side = 'left')
# button2.pack(side = 'left')
# button3.pack(side = 'left')
#
# frame.pack()
#
# bottomFrame = Frame(root)
#
# label = Label(bottomFrame, text = 'hello world')
# label.pack()
#
# bottomFrame.pack(side = BOTTOM)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# l1 = Label(root, text = 'subho', bg ='red')
# l2 = Label(root, text = 'SUBHO', bg = 'green')
# l3 = Label(root, text = 'Subho', bg = 'blue')
#
# l1.pack(fill = X)
# l2.pack(side = LEFT, fill = Y)
# l3.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# user_name = Label(root, text = 'User name')
# password = Label(root, text = 'Password')
#
# entry1 = Entry(root)
# entry2 = Entry(root)
#
# user_name.grid(row = 0, column = 0, sticky = E)
# password.grid(row = 1, column = 0, sticky = E)
#
# entry1.grid(row = 0, column = 1)
# entry2.grid(row = 1, column = 1)
#
# t_c = Checkbutton(root, text = 'I agreed all terms and condition')
# t_c.grid(columnspan = 2)
#
# root.mainloop()
#
# from tkinter import *
#
# def func(event):
#     print('Button clicked')
#
# root = Tk()
#
# button = Button(root, text = 'Click me')
# button.bind("<Button-1>", func)
# button.pack()
#
# root.mainloop()
#

#===========================================================================

# from tkinter import *
#
# def left_click(event):
#     print('left clicked')
#
# def middle_click(event):
#     print('middle clicked')
#
# def right_click(event):
#     print('right clicked')
#
# root = Tk()
#
# frame = Frame(root, width = 300, height = 300)
# frame.bind('<Button-1>', left_click)
# frame.bind('<Button-2>', middle_click)
# frame.bind('<Button-3>', right_click)
#
# frame.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
# root.geometry('640x480+120+120')
#
# root.mainloop()
#
# from tkinter import *
#
# class myButton:
#     def __init__(self, master):
#         self.printButton = Button(master, text = 'print', command = self.printMessage)
#         self.printButton.pack(side = LEFT)
#
#         self.quitButton = Button(master, text = 'quit', command = master.quit)
#         self.quitButton.pack(side = LEFT)
#
#     def printMessage(self):
#         print('Hello World')
#
# root = Tk()
#
# ButtonClassObject = myButton(root)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# main_menu = Menu(root)
# root.config(menu = main_menu)
#
# file_menu = Menu(root)
# main_menu.add_cascade(label = 'File', menu = file_menu)
#
# file_menu.add_command(label = 'New')
# file_menu.add_command(label = 'Open')
#
# save_menu = Menu(file_menu)
# file_menu.add_cascade(label = 'Save', menu = save_menu)
#
# file_menu.add_command(label = 'Quit', command = root.quit)
#
# edit_menu = Menu(root)
# main_menu.add_cascade(label = 'Edtt', menu = edit_menu)
#
# view_menu = Menu(root)
# main_menu.add_cascade(label = 'View', menu = view_menu)
#
# button = Button(root, text = 'Button')
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import messagebox
#
# def call_message_box_info():
#     messagebox.showwarning('This is Info', 'Yes! messagebox info is running as expected')
#
# def call_message_box_warning():
#     messagebox.showwarning('This is Warning', 'Yes! messagebox warning is running as expected')
#
# def call_message_box_error():
#     messagebox.showerror('This is Error', 'Yes! messagebox error is running as expected')
#
# root = Tk()
#
# info = Button(root, text = 'Call Info', command = call_message_box_info)
# warning = Button(root, text = 'Call Warning', command = call_message_box_warning)
# error = Button(root, text = 'Call Error', command = call_message_box_error)
#
# info.pack()
# warning.pack()
# error.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import messagebox
#
# def ask_user():
#     inp = messagebox.askquestion('Exit', 'Do you really want to exit?')
#     if inp == 'yes':
#         root.quit()
#
# root = Tk()
#
# exit_button = Button(root, text = 'Exit', command = ask_user)
# exit_button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import messagebox
#
# def message_box_testing():
#     # rtrn = messagebox.askokcancel('ask ok cancel', 'ask ok cancel')
#     # rtrn = messagebox.askyesno('ask yes no', 'ask yes no')
#     # rtrn = messagebox.askretrycancel('ask retry cancel', 'ask retry cancel')
#     rtrn = messagebox.askyesnocancel('ask yes no cancel', 'ask yes no cancel')
#     print(rtrn)
#
# root = Tk()
#
# call_messagebox = Button(root, text = 'Call messagebox', command = message_box_testing)
# call_messagebox.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
# root.config(bg = 'grey')
# root.geometry('300x300+200+200')
#
# canvus = Canvas(root, width = 200, height = 200, bg = 'yellow')
# canvus.pack()
#
# line = canvus.create_line(0, 0, 200, 100, fill = 'red')
# line = canvus.create_line(200, 100, 0, 200, fill = 'green')
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
# root.geometry('300x300+200+200')
# canvas = Canvas(root, width =300, height = 300, bg = 'gray')
# canvas.pack()
#
# canvas.create_arc(100, 100, 200, 200, start = 30, extent = 90)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# canvas = Canvas(root)
# canvas.pack()
#
# photo = PhotoImage(file = "D:\Downloads\SamplePNGImage_100kbmb.png")
#
# canvas.create_image(0, 0, anchor = 'nw', image = photo)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# canvas = Canvas(root, bg = 'blue')
# canvas.pack()
#
# canvas.create_rectangle(10, 10, 100, 100, fill = 'yellow', outline = 'red')
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# canvas = Canvas(root, bg = 'yellow')
# canvas.pack()
#
# canvas.create_oval(100, 20, 200, 250, fill = 'orange', outline = 'green')
# canvas.create_oval(200, 50, 300, 100, fill = 'magenta', outline = 'red')
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# canvas = Canvas(root, width = 800, height = 600)
# canvas.pack()
#
# points1 = [250, 110, 480, 200, 280, 280, 250, 110]
# points2 = [150, 110, 380, 200, 180, 280, 150, 110]
# canvas.create_polygon(points1, fill = '', outline = 'black', width = 3)
# canvas.create_polygon(points2)
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
# root.geometry('300x300+120+120')
#
# label1 = Label(root, text = 'Hello World', fg = 'red')
# label2 = Label(root, text = 'Hello World', fg = 'green')
# label1.place(x = 50, y = 80)
# label2.place(x = 60, y = 100)
#
# root.mainloop()
#
# from tkinter import *
#
# def click_me():
#     print(get_input.get())
#
# root = Tk()
#
# get_input = Entry(root)
# get_input.pack()
#
# button = Button(root, text = 'Click me', command = click_me)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def click_me():
#     print(txt_var.get())
#
# root = Tk()
#
# txt_var = StringVar()
#
# entry = Entry(root, textvariable = txt_var)
# entry.pack()
#
# button = Button(root, text = 'print', command = click_me)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def check_checkbutton():
#     print(chk_var.get())
#
# root = Tk()
#
# # chk_var = IntVar()
# # chk_box = Checkbutton(root, text = 'test check button', variable = chk_var)
#
# chk_var = StringVar()
# chk_box = Checkbutton(root, text = 'test check button', variable = chk_var, offvalue = 'unchecked', onvalue = 'checked')
#
# chk_box.pack()
#
# button = Button(root, text = 'check chekbutton', command = check_checkbutton)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def check_radio_button():
#     print(r_button_value.get())
#
# root = Tk()
#
# r_button_value = IntVar()
#
# r_button1 = Radiobutton(root, text = 'Male', value = 1, variable = r_button_value)
# r_button2 = Radiobutton(root, text = 'Female', value = 2, variable = r_button_value)
#
# r_button1.pack()
# r_button2.pack()
#
# chk_button = Button(root, text = 'Check', command = check_radio_button)
# chk_button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# # here width means number of character and height means number of lines
# list_box = Listbox(root, width = 30, height = 3)
#
# list_box.insert(1, 'C')
# list_box.insert(2, 'C++')
# list_box.insert(3, 'Java')
# list_box.insert(4, 'Python')
# list_box.insert(5, 'C#')
# list_box.insert(6, 'JavaScript')
#
# list_box.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# # selectmodes : SINGLE, BROWSE (default), MULTIPLE, EXTENDED
# list_box = Listbox(root, selectmode = EXTENDED)
#
# list_box.insert(1, 'C')
# list_box.insert(2,'Python')
# list_box.insert(3,'Java')
# list_box.insert(4,'C++')
# list_box.insert(5,'COBOL')
# list_box.insert(6,'VisualBasic')
# list_box.insert(7,'JavaScript')
# list_box.insert(8,'c#')
# list_box.insert(9,'HTML')
# list_box.insert(10,'CSS')
#
# list_box.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def print_selected():
#     selected_items = list_box.curselection()
#     print(selected_items)
#     for item in selected_items:
#         print(list_box.get(item))
#
# root = Tk()
#
# list_box = Listbox(root, selectmode = EXTENDED)
#
# list_box.insert(1, 'C')
# list_box.insert(2,'Python')
# list_box.insert(3,'Java')
# list_box.insert(4,'C++')
# list_box.insert(5,'COBOL')
# list_box.insert(6,'VisualBasic')
# list_box.insert(7,'JavaScript')
# list_box.insert(8,'c#')
# list_box.insert(9,'HTML')
# list_box.insert(10,'CSS')
#
# list_box.pack()
#
# button = Button(root, text = 'Print selected', command = print_selected)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def delete_item():
#     selected_items = list_box.curselection()
#     for item in selected_items:
#         list_box.delete(item)
#
# root = Tk()
#
# list_box = Listbox(root)
#
# list_box.insert(1, 'one')
# list_box.insert(2, 'two')
# list_box.insert(3, 'three')
#
# list_box.pack()
#
# delete_button = Button(root, text = 'Delete', command = delete_item)
# delete_button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter.ttk import Combobox
#
# def print_selected():
#     print(combo.get())
#
# root = Tk()
#
# items = ['C', 'Python', 'Java', 'C++', 'HTML', 'CSS', 'MySQL', 'JavaScript']
#
# # again here height means number of lines and width means number of character
# combo = Combobox(root, value = items, height = 5, width = 30)
# combo.set('Programming language')
# combo.pack()
#
# button = Button(root, text = 'Print', command = print_selected)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter.font import Font
#
# root = Tk()
# root.geometry('320x240+200+200')
#
# # weight : bold, normal (default); slant = italic, roman (default); underline = 1, 0 (default); overstrike = 1, 0 (default) {strikethrough}
# my_font = Font(family = 'MV Boli', size = 22, weight = 'bold', slant = 'roman', underline = 1, overstrike = 1)
#
# label = Label(root, text = 'This is a label', font = my_font)
# label.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import font
#
# root = Tk()
#
# fonts = list(font.families())
# for i in fonts:
#     print(i)
#
# root.mainloop()
#
# from tkinter import *
#
# def print_text():
#     #kktxt = text.get(1.0, END)
#     txt = None
#     try:
#         txt = text.selection_get()
#     except:
#         print('Nothing is selected')
#     if type(txt) == str:
#         pos = text.search(txt, 1.0, END)
#         print('Position : ', pos)
#         print(txt)
#
#
# root = Tk()
#
# # we can also change font using font parameter as previous
# text = Text(root, width = 20, height = 10, wrap = WORD,
#             padx = 10, pady = 10, border = 5, selectbackground = 'red',
#             selectforeground = 'yellow', bg = 'orange', fg = 'blue')
#
# text.insert(INSERT, 'Subho Basak')
#
# text.pack()
#
# button = Button(root, text = 'Print', command = print_text)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def clear_text_box():
#     text_box.delete(1.0, END)
#
# root = Tk()
#
# text_box = Text(root, width = 30, height = 20)
# # if we pass END instead of INSERT then it will insert it at the end
# text_box.insert(INSERT, 'Hello World!')
# text_box.pack()
#
# clear_button = Button(root, text = 'Clear', command = clear_text_box).pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# text_box_frame = Frame(root)
# text_box_frame.pack()
#
# y_scroll = Scrollbar(text_box_frame)
# y_scroll.pack(side = RIGHT, fill = Y)
#
# text_box = Text(text_box_frame, width = 20, height = 10, yscrollcommand = y_scroll.set)
# text_box.pack(side = LEFT)
#
# y_scroll.config(command = text_box.yview)
#
# root.mainloop()

# ============== Small Project ==============
#
# from tkinter import *
# import wikipedia
#
# def show_details():
#     txt = text_entry.get()
#     text_box.delete(1.0, END)
#     try:
#         text_box.config(fg = 'black')
#         answer = wikipedia.summary(txt)
#         text_box.insert(INSERT, answer)
#     except:
#         text_box.config(fg = 'red')
#         text_box.insert(INSERT, 'Please check your spelling or internet connection')
#
# root = Tk()
#
# text_box_frame = Frame(root)
#
# text_entry = Entry(root)
#
# search_button = Button(root, text = 'search', command = show_details)
#
# text_scroll = Scrollbar(text_box_frame)
#
# text_box = Text(text_box_frame, width = 50, height = 20,
#                 yscrollcommand = text_scroll.set, wrap = WORD)
#
# text_scroll.config(command = text_box.yview)
#
# text_entry.pack()
# search_button.pack()
# text_box_frame.pack()
# text_box.pack(side = LEFT)
# text_scroll.pack(side = RIGHT, fill = Y)
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import simpledialog
#
# def show_pop_up():
#     inp1 = simpledialog.askstring('Input string', 'Please enter your string')
#     inp2 = simpledialog.askfloat('Input float', 'Please enter your floating value')
#     inp3 = simpledialog.askinteger('Input integer', 'Please enter your integer value')
#     print(inp1)
#     print(inp2)
#     print(inp3)
#
# root = Tk()
#
# button = Button(root, text = 'Pop up', command = show_pop_up)
# button.pack()
#
# root.mainloop()
#
# import time
# from tkinter import *
#
# def get_scale_value():
#     print(scale.get())
#     time.sleep(0.5)
#     scale.set(50)
#
# root = Tk()
#
# scale = Scale(root, from_ = 0, to = 100)
# scale.pack()
#
# button = Button(root, text = 'get scale value', command = get_scale_value)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
#
# scale = Scale(root, from_ = 0, to = 100, orient = HORIZONTAL, length = 200,
#               width = 10, sliderlength = 30)
# scale.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def open_window():
#     top = Toplevel()
#     top.title('It\'s a new window')
#     top.geometry('300x300+200+200')
#
#     top_button = Button(top, text = 'Close this window', command = top.destroy)
#     top_button.pack()
#
# root = Tk()
# root.geometry('300x300+150+150')
#
# button = Button(root, text = 'Open window', command = open_window)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# def get_value():
#     print(spin.get())
#
# root = Tk()
#
# spin = Spinbox(root, from_ = 1, to = 10)
# spin.pack()
#
# button = Button(root, text = 'Get value', command = get_value)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
#
# root = Tk()
# root.geometry('300x300')
#
# frame = LabelFrame(root, text = 'Frame name', padx = 5, pady = 5)
# frame.pack()
#
# label = Label(frame, text = 'Hello World', fg = 'red')
# label.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import filedialog
#
# def open_file():
#     result = filedialog.askopenfile(initialdir = 'D:/', title = 'Select file',
#                            filetypes = (('Text files', '.txt'), ('Audio files', '.mp3'),
#                                         ('Video files', '.mp4'), ('All files', '*.*')))
#     print(result)
#     print(result.name)
#     print('====================================')
#     for charecter in result:
#         print(charecter)
#
# root = Tk()
# root.geometry('300x300')
#
# frame = LabelFrame(root, text = 'File', padx = 5, pady = 5)
# frame.pack()
#
# button = Button(frame, text = 'Open file', command = open_file)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import filedialog
#
# def save_file():
#     result = filedialog.asksaveasfile('w', defaultextension = '.txt')
#     if result != None:
#         result.write('Hello World !!!!!!!!')
#     result.close()
#
# root = Tk()
#
# button = Button(root, text = 'Save as', command = save_file)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import colorchooser
#
# def open_color_chooser():
#     color = colorchooser.askcolor(title = 'Choser color')
#     print(color) # first one is the rgb value and the second one is the hex value
#     root.config(bg = color[1])
#
# root = Tk()
#
# button = Button(root, text = 'Color chooser', command = open_color_chooser)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import messagebox
#
# def func(event):
#     messagebox.showinfo('OUTPUT', 'Every thing is working fine!')
#
# root = Tk()
#
# root.bind('<Control-c>', func)
#
# button = Button(root, text = 'Press', command = func)
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter.ttk import Style
#
# style = Style()
#
# print()
#
# style.theme_use('clam')
# print(style.theme_use())
#
# root = Tk()
# root.geometry('300x300+300+300')
#
# label = Label(root, text = 'Hello world')
# label.pack()
#
# button = Button(root, text = 'Ok')
# button.pack()
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import ttk
# from tkinter.ttk import Notebook
#
# root = Tk()
# root.geometry('200x200')
#
# i = 0
# while i < 20:
#     root.rowconfigure(i, weight = 1)
#     root.columnconfigure(i, weight = 1)
#     i += 1
# tab = Notebook(root)
# tab.grid(row = 1, column = 0, columnspan = 20, rowspan = 19, sticky = 'NESW')
#
# tab1 = ttk.Frame(tab)
# tab2 = ttk.Frame(tab)
#
# tab.add(tab1, text = 'tab 1')
# tab.add(tab2, text = 'tab 2')
#
# root.mainloop()
#
# from tkinter import *
# from tkinter import ttk
#
# i = 1
#
# def add_new_tab():
#     global i
#     new_page = ttk.Frame(tab)
#     tab.add(new_page, text = 'tab '+str(i))
#     label = Label(new_page, text = 'Hello World')
#     label.pack()
#     i += 1
#
# root = Tk()
#
# tab = ttk.Notebook()
#
# button = Button(root, text = 'add new tab', command = add_new_tab)
# button.pack()
#
# tab.pack(fill = BOTH)
#
# root.mainloop()