import tkinter as tk
from tkinter import messagebox, ttk
import git
import subprocess
import os
import threading
import gettext

# Setup translation
locale_path = os.path.join(os.path.dirname(__file__), 'locale')
lang = gettext.translation('messages', locale_path, fallback=True)
lang.install()
_ = lang.gettext

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

def run_script(script_path):
    try:
        subprocess.run(['xfce4-terminal', '--hold', '--working-directory', os.path.dirname(script_path), '--command', f"bash -c '{script_path}; exec bash'"])
    except subprocess.CalledProcessError as e:
        messagebox.showerror(_("Error"), _("An error occurred while running the script: ") + str(e))

def clone_repo(repo_url, download_path):
    def download_and_run():
        progress_window = tk.Toplevel(root)
        progress_window.title(_("Cloning Repository"))
        progress_window.configure(bg="#575656")
        
        progress_label = ttk.Label(progress_window, text=_("Cloning repository, please wait..."))
        progress_label.pack(pady=10)
        
        progress_bar = ttk.Progressbar(progress_window, mode="indeterminate")
        progress_bar.pack(pady=10, padx=10)
        progress_bar.start()

        def clone_and_run():
            try:
                git.Repo.clone_from(repo_url, download_path)
                progress_bar.stop()
                progress_window.destroy()
                messagebox.showinfo(_("Success"), _("Repository cloned successfully."))
                run_script(os.path.join(download_path, 'install.sh'))
            except Exception as e:
                progress_bar.stop()
                progress_window.destroy()
                messagebox.showerror(_("Error"), _("Failed to clone repository: ") + str(e))

        threading.Thread(target=clone_and_run).start()

    answer = messagebox.askyesno(_("Confirmation"), _("Do you want to continue?"))
    if answer:
        download_and_run()

def download_and_run_configuration():
    repo_url = "https://github.com/R2r-S/configuration.git"
    download_path = os.path.join(script_directory, 'configuration')
    clone_repo(repo_url, download_path)

def xfce_look():
    repo_url = "https://github.com/R2r-S/xfce_look.git"
    download_path = os.path.join(script_directory, 'xfce_look')
    clone_repo(repo_url, download_path)

def extras():
    repo_url = "https://github.com/R2r-S/extra.git"
    download_path = os.path.join(script_directory, 'debian_extra')
    clone_repo(repo_url, download_path)

root = tk.Tk()
root.title(_("Extra Features"))
root.configure(bg="#575656")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background="#4CAF50", foreground="white", font=("TkDefaultFont", 12), padding=10, focuscolor="none")
style.map("TButton", background=[("active", "#45a049")])
style.configure("TLabel", background="#575656", foreground="white", font=("TkDefaultFont", 12))
style.configure("TEntry", fieldbackground="#2E2E2E", foreground="white")
style.configure("TListbox", background="#2E2E2E", foreground="white", selectbackground="#4CAF50", selectforeground="white")

button2_label = ttk.Label(root, text=_("Configuration"), font=("TkDefaultFont", 15, "bold"), background="#575656", foreground='#ffffff')
button2_label.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

button2_button = ttk.Button(root, text=_("Run"), command=download_and_run_configuration)
button2_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

button2_label = ttk.Label(root, text=_("Drivers, export /sbin directory to PATH variable\nDisable sound on logout\nAdd repositories using terminal command\nLanguage configuration"), font=("TkDefaultFont", 12, "bold"), background="#575656", foreground='#000000')
button2_label.grid(column=2, row=1, padx=10, pady=10, sticky=tk.W)

button3_label = ttk.Label(root, text=_("xfce-look"), font=("TkDefaultFont", 15, "bold"), background="#575656", foreground='#ffffff')
button3_label.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

button3_button = ttk.Button(root, text=_("Run"), command=xfce_look)
button3_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

button3_label = ttk.Label(root, text=_("Themes, wallpapers, icons"), font=("TkDefaultFont", 12, "bold"), background="#575656", foreground='#000000')
button3_label.grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)

button4_label = ttk.Label(root, text="debian_extra", font=("TkDefaultFont", 15, "bold"), background="#575656", foreground='#ffffff')
button4_label.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)

button4_button = ttk.Button(root, text=_("Run"), command=extras)
button4_button.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)

button4_label = ttk.Label(root, text=_("Codecs, multimedia\nvim, neofetch, etc..."), font=("TkDefaultFont", 12, "bold"), background="#575656", foreground='#000000')
button4_label.grid(column=2, row=3, padx=10, pady=10, sticky=tk.W)

root.mainloop()
