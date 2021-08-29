import tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

main_window_padding = 8

main_window = tkinter.Tk()

main_window.title("Calculator")
main_window.geometry('200x200')
main_window['padx'] = main_window_padding

# label = tkinter.Label(main_window, text="Calculator")
# label.grid(row=0, column=0, columnspan=3)


result = tkinter.Entry(main_window)
result.grid(row=0, column=0, sticky='nsew', columnspan=2)

key_pad = tkinter.Frame(main_window)
key_pad.grid(row=1, column=1, sticky='nsew')

row = 0
for key_row in keys:
    col = 0
    for key in key_row:
        tkinter.Button(key_pad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.W + tkinter.E)
        col += key[1]
    row += 1

main_window.update()
main_window.minsize(key_pad.winfo_width() + main_window_padding, result.winfo_height() + key_pad.winfo_height())
main_window.maxsize(key_pad.winfo_width() + 100 + main_window_padding, result.winfo_height()
                    + 100 + key_pad.winfo_height())

# main_window.columnconfigure(0, weight=1)
# main_window.columnconfigure(1, weight=100)
# main_window.columnconfigure(2, weight=1)
# main_window.columnconfigure(3, weight=100)
# main_window.rowconfigure(0, weight=1)
# main_window.rowconfigure(1, weight=100)
# main_window.rowconfigure(2, weight=100)
# main_window.rowconfigure(3, weight=100)
# main_window.rowconfigure(4, weight=100)
# main_window.rowconfigure(5, weight=100)

# Buttons
# c_button = tkinter.Button(main_window, text="C", width=4, height=2)
# ce_button = tkinter.Button(main_window, text="CE", width=4, height=2)
# button7 = tkinter.Button(main_window, text="7", width=4, height=2)
# button8 = tkinter.Button(main_window, text="8", width=4, height=2)
# button9 = tkinter.Button(main_window, text="9", width=4, height=2)
# plus_button = tkinter.Button(main_window, text="+", width=4, height=2)
#
#
# c_button.grid(row=1, column=0, sticky='nw')
# ce_button.grid(row=1, column=1, sticky='nw')
# button7.grid(row=2, column=0, sticky='nw')
# button8.grid(row=2, column=1, sticky='nw')
# button9.grid(row=2, column=2, sticky='nw')
# plus_button.grid(row=2, column=3, sticky='nw')

main_window.mainloop()
