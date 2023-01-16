# MooCoderPy
Python/Tkinter version of Moocoder

MooCoder is an IDE for programming MOO Code in LambdaMOO or similar servers. It incorporates a built in
MOO/MUSH client, supports the local edit option, and allows you to load and edit object verbs in different tabs.
It supports syntax highlighting, jump to error location and a stack trace window.

This should run on Python 3.6 (or better) and uses the tkinter with no external dependencies.

This requires a desktop environment: Linux running X11 (if it has a Desktop it's running X11), Windows, MacOS should all work.

The original Delphi implementation can be found at https://github.com/rjmatthews62/MooCoder

## Installation ##
Can be installed via pip:
* pip install --upgrade moocoderpy-rjmatthews62
* python -m MooCoderPy 

### Python3 Notes ###
* Ubuntu
    *  For reasons that are not clear, the default Python3 install on Ubuntu is quite minimalist.  Tk and pip are in separate packages, so the minimum python3 install becoms:
    *  `sudo apt install python3 python3-tk python3-pip`

## Setup ##
* **Settings -> Server Config** : set server address (and port). You can also set font size. 
* **File -> Connect** - Connect to server
* **File -> Disconnect** - Disconnect from server
* **File -> Open** - Open a local file in the editor
* **File -> Save** - Save contents of current window to local file

### External Editor support: ###

If you set **@edit-option local+** on your MOO server, the **@edit** command will be redirected to MooCoderPy's internal editor.
Selecting **Edit->Send Update (or F5)** will issue the correct command to update whatever you are currently editing.
Each edited item will have its own tab, and you can use the test line as for the verbs.

**Project->New Tab (Ctrl+N)** - Loads a verb into its own tab. Press F5 to compile.

**Project->Get Verbs (Ctrl+Shift+V)** - Load all the verbs for an object into the verbs window.
    You can double click or hit Enter in the Verbs pane to edit that verb.

**Project->Get Verbs and Properties** - Load both Verbs and [Properties](#property-editing) in one operation.

**Project->Clear Project** - Close all code windows and clear verb list

**View->Toggle View Ctrl+Shift+T** - Toggle between terminal and previous edit view.

**View->Stack** - Toggle Stack Pane

**View->Help F1** - Opens this README file in browser

Basic error checking and stack trace implemented.

Syntax Highlighting implemented.

Command History is supported using the **up and down arrow keys**

Each code window has an optional single-line test command which will run on successful compile (F5)

Bracket Matching implemented

Right-Click in code window will bring up a context menu.
* **Goto Line Ctrl+G** will got to a line no in a code window.
* **Find Ctrl+F** - find text in current window
* **Find Again F3** - repeat last find
* **Replace Ctrl+H** - search and replace text
* **Refresh Ctrl+R** - Reload page from server
* **Redo Syntax** - redo syntax highlighting on page
* **Close** - Close current window.
* **Undo - Ctrl+Z** - undo last changes
* **Redo - Shift+Ctrl+Z** - redo last changes

A double-click on an error message or stack trace in either the stack or the main terminal window will go the the relevent source code.

## Property Editing ##
**Project-->Get Properties** Will load all the properties of an object into the "Properties" tab.
* Double clicking or Enter will allow editing of the property.
* Simple types (String, Int, Float, Object) will be edited in a popup window. 
* More complicated types (Map, List) are edited in an edit window. The lists and maps are split into lines for ease of reading and editing. The extra lines will be removed on update.
* Use  F5 to write the update back to the server.
* List Properties can be converted to plain text for ease of editing. This will only work with simple lists, and will save as a flattened list of strings.
* You can add a test command for each property page.

## SCRATCHPAD ##
**Edit-->Scratchpad** - Opens a scratchpad window, allowing uploading of multiline commands. F5 will send the contents of the scratchpad to the server. Use with care.

## List Navigation ##
* Property and Verb lists can be sorted by column, by clicking on the column header
* Ctrl+F and F3 work in lists for find and find again.

## Editing Shortcuts ##
Standard editing key functions should all work as expected.
* Ctrl+/ can be used for select all.
* Standard Tk key binds are here: https://www.tcl.tk/man/tcl8.4/TkCmd/text.html#M152

## Icons ##
Icons sourced from https://icons8.com/

## Release History ##
0.5.8 - Included fix for properties with periods (contrib by Katelyn Gigante)

0.5.7 - Improved handling of error lines to reduce chance of spoofing.

0.5.6 - Added type icons to tabs

0.5.5 - Project Get Verbs and Properties in one command.

0.5.4 - Fixed an issue with '%' in saving history

0.5.3 - List sort and find implemented, link to Help page.

0.5.1 - Perfomance improvments in terminal window.

0.5.0 - Fixed issue with shortcut keys going to wrong window. Tided up highlighting on refresh.

0.4.9 - Force focus to command line in Terminal Window.

0.4.8 - Solved issue with word wrap and double lines, fixed command history issue, improved syntax highlight performance.

0.4.6 - Set edit windows to be non-wrapping

0.4.5 - Save windows to text

0.4.4 - Scratchpad.

0.4.3 - Line numbers and autoindent implemented.

0.4.2 - Selections now show correctly.

0.4.1 - Fix to error message in Edit as Text

0.3.9 - Property Editing.

0.3.8 - Readme Correction

0.3.7 - Make stack pane sizable

0.3.6 - Adjustable font size (in Setup-->Server Config). Local Edit refresh now works

0.3.5 - Fixed bug with Ctrl+N adding to verb list

0.3.4 - External edit can have test lines, Ctrl+Shift+T toggle view, additional detail shown in edit window.

0.3.3 - External edit now opens in a seperate tab per item, supports syntax.

0.3.2 - Double-click on error messages or stack to go to source line.

0.3.1 - Fixed windows maximized for linux environment

0.3.0 - Fixed disconnect handling issue, set default window state to maximized.

0.2.9 - Tweaked selection handling.

0.2.8 - Replace working, Undo and Redo implemented

0.2.7 - Additional icon error checking.,

0.2.6 - Bracket Matching

0.2.5 - removed unwanted checkbox import

0.2.4 - Edit find, context menu, refresh, close, clear

0.2.3 - Added Syntax highlighting, Goto Line, Cursor Location

0.2.2 - Added Auto-test functionality

0.2.1 - Sorting out window icon on linux

0.2.0 - Fighting with packaging tools

0.1.9 - Type definition fix for older pythons and include icon in package.

0.1.5 - Added icon, tidied up Verb window sizing and include docstring in verb window.

0.1.4 - Get Verb and Verbs window working.

0.1.3 - Edit Verb (Edit->New Tab)

0.1.2 - Show version, added F5 shortcut, save recent history, set config file to home folder.

0.1.1 - Added external editor support, command history
