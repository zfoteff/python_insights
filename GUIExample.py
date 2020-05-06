<<<<<<< HEAD
import PySimpleGUI as sg

# This design pattern simulates button callbacks
# Note that callbacks are NOT a part of the package's interface to the
# caller intentionally.  The underlying implementation actually does use
# tkinter callbacks.  They are simply hidden from the user.

# The callback functions
def button1():
    print('Button 1 callback')


def button2():
    print('Button 2 callback')


# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Quit()]]

# Show the Window to the user sg.Window(title, layout)
window = sg.Window('Button callback example', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.Read()
    # Take appropriate action based on button
    if event == '1':
        button1()
    elif event == '2':
        button2()
    elif event == 'Quit' or event is None:
        window.Close()
        break

    # All done!
sg.PopupOK('Done')
=======
import PySimpleGUI as sg


# This design pattern simulates button callbacks
# Note that callbacks are NOT a part of the package's interface to the
# caller intentionally.  The underlying implementation actually does use
# tkinter callbacks.  They are simply hidden from the user.

# The callback functions
def button1():
    print('Button 1 callback')


def button2():
    print('Button 2 callback')


# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Quit()]]

# Show the Window to the user sg.Window(title, layout)
window = sg.Window('Button callback example', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.Read()
    # Take appropriate action based on button
    if event == '1':
        button1()
    elif event == '2':
        button2()
    elif event == 'Quit' or event is None:
        window.Close()
        break

    # All done!
sg.PopupOK('Done')
>>>>>>> 3471f8313e09e50bfa87d62ccf04de395c2b0361
