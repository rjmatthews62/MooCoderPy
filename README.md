# MooCoderPy
Python/Tkinter version of Moocoder

Very much a work in progress, but it currently works as a simple Moo client.

Can be installed via pip:
* pip install moocoderpy-rjmatthews62
* python -m MooCoderPy

Setup -> Server Config : set server address (and port) 

File -> Connect - Connect to server
File -> Disconnect - Disconnect from server
File -> Open - Open a local file in the editor

External Editor support:

If you set @edit-option local+ on your MOO server, the @edit command will be redirected to MooCoderPy's internal editor.
Selecting Edit->Send Update will issue the correct command to update whatever you are currently editing.

Command History is support using the up and down arrow keys

== Release History ==
0.1.1 - Added external editor support, command history
