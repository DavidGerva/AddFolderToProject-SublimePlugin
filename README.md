Add Folder To Project
=====================

**NOTE 30.01.2015: I recently noticed that the plugin doesn't work if there isn't already a project in the current sublime session. From this condition you can just use the command "Create new project from file". I'll fix it ASAP. Thank you!** "

With this plugin you can **open a file in sublime and easily add the file folder to the project**, **add a generic folder (asked by a prompt dialog) to the project** and you can also **copy into the clipboard the path of the file** you're editing **or the path of the file's directory**.

You can also create a new project starting from the opened file in sublime.

I created this plugin because I often edit files in sublime opening it directly from MS Visual Studio (I created the shortcut Alt+S in VS) or with F4 from TotalCommander and I generally find useful having the directory in the project or copying the file path in the clipboard.

Usage
-----
Just right click on the view or open the command panel and choose the operation.

**Add Folders To Project:**
Opens a list of the directories from the root to the file's directory.

![Add Folders To Project](./images/AddFolders.png)

**Add This Folder To Project:**
Add directly the file's directory to the project. 

![Add This Folders To Project](./images/AddThisFolder.png)

**Copy File Path**:
![Copy Path](./images/CopyPath.png)

Copies the file path to the clipboard.

**Copy Dir Path**:
Copies the file's dir path to the clipboard.

ToDo
----
1. Add the settings file to allow the user to choose which menu item to visualize both in the righ-click menu and in the operation panel (Ctrl+Shift+P).

ChangeLog
=========
AddFolder - 1.1.0
---------------
- Fixed menu item visibility with file without a phisical path
- If there is no phisical paths now the plugin asks for a custom path
- If a directory already exists in the project it won't be shown in the list dialog
- If the file's directory already exists in the project in the left click menu you'll now see not the "add this folder to project" but a new more useful "remove this folder from poject". Quite self-explaining, I think.
- Now you can create a blank new project starting from the opened file with the command (in the Ctrl+Shift+P Menu) "Create Project from File". This command will open a new sublime window with a new project containing only the file's directory. *I can't try it under OsX* so I just copied two lines of code from another project (thanks to the SideBarEnhancements sublime plugin). *OsX Users: can you please tell me if it works?!*. This will be really appreciated.

AddFolder - 1.0.0
---------------
- First Release