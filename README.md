Registron
=========

Registron is a speech-based registration program

#### Build Information
- [Python 2.7][1]
- PyQt4
- Pyuic 4.9.3
- [Qt Designer 4.8.2][2]
- [py2exe][3] (For Windows executable bindings)

#### Third Party Modules
- Pyttsx (Python Text To Speech)

> To run from source files directly, switch to the source branch and simply run

```python registron.py``` or ```./registron.py``` in *nix like systems. Windows users can also run this from Idle.

#### Adding student images
Edit app.qrc resource file and append the location of the image in the ```<file>``` tag. Make sure this image exists and also that that the tags are properly closed. after this, run the following command
sh```pyrcc4 app.qrc > app_rc.py```
#### Contributors
- [Joseph Rex](http://josephrex.me)
- [James Olanipekun][4]

[1]:http://python.org
[2]:http://qt-project.org
[3]:http://www.py2exe.org/
[4]:https://www.google.ca/#q=james+olanipekun
