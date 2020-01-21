print()
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_______")
print("    >>> Loading JSaH... ", end="\r")

from videospliter import *

file_path = ""

#def find_files
print("    >>> Loading JSaH... | Loading Complete, Starting")
print()

def menu_home():
    global menu_state
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\____")
    print("  /- Just Shapes and Heatmaps -\\")
    print()
    questions = [
        {
            'type': 'list',
            'name': 'main',
            'message': '',
            'choices': ['Load', 'Quit'],
            'filter': lambda val: val.lower()
        }
    ]
    menu_state = prompt(questions, style=style)["main"]

def menu_load():
    global file_path, root
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\____")
    print("  /- Loading -\\")
    print()
    root.update()
    file_path = filedialog.askopenfilename(initialdir=data_folder)
    root.update()

menu_state = "load"

while 1:
    print()
    if menu_state == "home":
        menu_home()
    elif menu_state == "quit":
        break
    elif menu_state == "load":
        menu_load()
    else:
        print("Unknown menu state | Reverting")
        menu_state = "home"
