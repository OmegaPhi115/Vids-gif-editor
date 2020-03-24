from PyFiles.imports import *
from PyFiles.separation_fichier import *


class main_menu():

    def __init__(self):
        self.main_win = tk.Tk()
        self.main_state = ""


    def create_project(self):
        """Create a project window"""
        loop = True

        def check_path(path):
            try:
                if os.path.exists(path):
                    if os.path.splitext(path)[1] == ".mp4":
                        try:
                            return [" ", 1]
                        except:
                            return ["No video found", 0]
                else:
                    return ["The path doesn't exist", 0]
            except:
                return ["Invalid path", 0]


        def confirm():
            if check_path(path_entry.get())[1] == 1:
                global loop
                # Create a project folder
                # path of project: CODE_PATH/Projets/NOM_DU_PROJET/
                path_of_project = Path.joinpath(Path.joinpath(CODE_PATH, "Projects/"), name_entry.get())
                os.makedirs(str(path_of_project))

                project_file = data_file(Path.joinpath(path_of_project, name_entry.get() + ".txt"), PROJECT_FILE_DICT)

                # Slice the vid
                os.makedirs(str(Path.joinpath(path_of_project, "images")))

                splitvideoimages(path_entry.get(), str(Path.joinpath(path_of_project, "images")))

                subwin.destroy()
                loop = False

        def path_finder():
            path = fd.askopenfilename()
            path_entry.delete(0, tk.END)
            path_entry.insert(0, path)
        subwin = tk.Tk()

        title = tk.Label(subwin, text="Create a new project")
        name_label = tk.Label(subwin, text="Name: ")
        path_label = tk.Label(subwin, text="Path of the video: ")
        info_label = tk.Label(subwin, text="")

        filesearch_button = tk.Button(subwin, text=">", command=path_finder)
        ok_button = tk.Button(subwin, text="Create project", command=confirm)
        cancel_button = tk.Button(subwin, text="Cancel", command=subwin.destroy)

        name_entry = tk.Entry(subwin)
        path_entry = tk.Entry(subwin)

        title.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=2)
        name_label.grid(row=1, column=0, sticky=tk.W, padx=4)
        path_label.grid(row=2, column=0, sticky=tk.W, padx=4)
        info_label.grid(row=3, column=0, sticky=tk.W, padx=4)

        filesearch_button.grid(row=2, column=2, sticky=tk.E, padx=4)
        ok_button.grid(row=4, column=1, columnspan=2, sticky=tk.E)
        cancel_button.grid(row=4, column=0, sticky=tk.W, padx=4)

        name_entry.grid(row=1, column=1)
        path_entry.grid(row=2, column=1)

        while loop:
            try:
                info_label.configure(text=check_path(path_entry.get())[0])
                subwin.update()
            except:
                return


    def main_menu(self):
        self.main_state = "main"
        main_menu_loop = True

        but_newproject = tk.Button(self.main_win, text="New project", command=self.create_project).grid(row=0, column=0, columnspan=2)

        but_loadproject = tk.Button(self.main_win, text="Load project").grid(row=1, column=0, columnspan=2)

        but_settings = tk.Button(self.main_win, text="settings").grid(row=2, column=0, columnspan=2)

        while main_menu_loop:
            try:
                self.main_win.update()
            except:
                main_menu_loop = False


    def settings_win(self):
        set_win = tk.Tk()


maa = main_menu()
maa.main_menu()
