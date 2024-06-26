The AirBnB Clone Project
Project Description
This repository contains the initial stage of a team project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

Description of the command interpreter:
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website clone.

General Use
Installing
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

git clone https://github.com/The-Leo/AirBnB_clone.git
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

Once the repository is cloned locate the "console.py" file and run it as follows:

/AirBnB_clone$ ./console.py When this command is run the following prompt should appear: (hbnb) This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program. Commands

create - Creates an instance based on given class

destroy - Destroys an object based on class and UUID

show - Shows an object based on class and UUID

all - Shows all objects the program has access to, or all objects of a given class

update - Updates existing attributes an object based on class name and UUID

quit - Exits the program (EOF will as well)

It can work in two different modes:

Interactive and Non-interactive.

In Interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
In Non-interactive mode, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.

$ echo "help" | ./console.py
(hbnb)
