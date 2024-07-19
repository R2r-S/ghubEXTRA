# GHubEXTRA

This repository contains a Python program with a graphical user interface (GUI) to manage and run various configuration scripts for Debian-based systems. The program uses `tkinter` for the GUI and `git` for cloning repositories.

## Prerequisites

Before running the program, you need to install the following packages:


sudo apt install python3-tk python3-git

Installation:

git clone https://github.com/R2r-S/ghubEXTRA.git

cd ghubEXTRA

python3 ghubEXTRA.py


The program provides a graphical interface to clone and run various configuration scripts for your Debian system.
Scripts

The following repositories are cloned and managed by the program:

    configuration: Configures drivers, exports /sbin directory to the PATH variable, disables sound on logout, adds repositories using terminal commands, and configures language settings.
    xfce-look: Provides themes, wallpapers, and icons.
    debian_extra: Installs codecs, multimedia applications, and additional tools like vim, neofetch, etc.

Translation

The program supports both English and Polish languages. The language is detected automatically based on the system settings. If the detected language is not supported, the default language is English.
Contributions

Feel free to fork this repository and contribute by submitting pull requests. Any improvements or suggestions are welcome!
License

This project is licensed under the MIT License - see the LICENSE file for details.


Authors

    Artur Stachera - R2r-S
