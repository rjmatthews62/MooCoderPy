# MooCoderPy
Python/Tkinter version of Moocoder

Still a bit rough around the edges, but actually functional as a Moo Coding tool

Can be installed via pip:
* pip install moocoderpy-rjmatthews62
* python -m MooCoderPy

Setup -> Server Config : set server address (and port) 

File -> Connect - Connect to server
File -> Disconnect - Disconnect from server
File -> Open - Open a local file in the editor

External Editor support:

If you set @edit-option local+ on your MOO server, the @edit command will be redirected to MooCoderPy's internal editor.
Selecting Edit->Send Update (or F5) will issue the correct command to update whatever you are currently editing.

Project->New Tab (Ctrl+N) - Loads a verb into its own tab. Press F5 to compile.
Project->Get Verbs - Load all the verbs for an object into the verbs window.
    You can double click in the Verbs pane to edit that verb.

Basic error checking and stack trace implemented.

Syntax Highlighting implemented.

Command History is supported using the up and down arrow keys

Each code window has an optional single-line test command which will run on successful compile (F5)

Ctrl+G will got to a line no in a code window.

== TODO ==
* Double click on errors

== Release History ==

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
