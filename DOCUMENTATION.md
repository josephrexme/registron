Documentation for Registron
============================
- [Registron as a python program](#chapter1)
- [GUI Basics](#chapter2)
- [Program utils module](#chapter3)
- [Using Qt designer with pyrcc and pyuic](#chapter4)
- [The program logic](#chapter5)
- [Creating the windows exe with pyinstaller](#chapter6)
- [References](#chapter7)

<h3 id="chapter1" name="chapter1">Registron as a python program</h3>
Registron is a student registration program built in python 2.7
Python as an interpreted programming language which is of two
main types which are python2 and python3. Python 2 was in use a
long time before its predecessor. Python 3 has some strict rules
that make it notbackward compatible with Python 2. With this,
a program written in python 2 syntax will not run with a python3
interpreter. A vice versa action running python 3 program with
python2 will likely be properly interpreted. An example of a
difference between python 2 and python 3 is the following hello
world program.
##### Python 2
```>>>print "Hello World!"```

##### Python 3
```>>>print("Hello World!")```

As shown in the examples, the python 3 requires the print function
to have its argument in braces like any other function where python
2 allows more flexibility. This ease of use allowed this project
to be implemented speedily.

<h3 id="chapter2" name="chapter2">GUI Basics</h3>
Computers have operated in CLI (Command Line Interface) from its
early days of use till date. However, in the ancient days of
computing, they only had the CLI to work with. This is just the
console where we type a bunch of digital text to execute program
instructions. After Xerox found GUI (Graphical User Interface), Apple
and Microsoft took the idea and implemented it in their ways.
Ever since, GUI has been known to be the most user friendly environment
to work with on computers. Registron could have been built as a CLI
program but then it will serve less of its purpose as students who are
less enlightened about computers will find it difficult to use.
There are 4 modules that can be used to build GUI programs in python
and they are:
- Tkinter
- wxPython
- PyGTK
- PyQt
PyQt was chosen for development because:
- It is stable for cross-platform GUI development
- It has a Qt designer which is WYSIWYG editor to draw the GUI before
importing to the code to work with
- The development machine (noxiux) has a KDE desktop and Qt applications
run really fine on KDE as GTK works on Gnome.

<h3 id="chapter3" name="chapter3">Program utils module</h3>
Before getting started with the actual GUI development of registron, we
put to consideration some simple python functions that will be required
in the program. These are the core functions and they will work just fine
even in a CLI environment. Python as a speech based program needs to talk
so we create a simple talking function for it. For this implementation,
[pyttsx][1] was used to interpret text to speech. As voices were 
programmatically written as text, the pyttsx function translates it to a
voice. We have a function that hashes passwords to MD5 (Message digest
 algorithm) and also checks for admin password authentication in comparison
with the stored hashed password.
The information storage system for registron is a JSON file rather than a
database. Even as sqlite had been thought of on initial development, the
information to be stored on registron does not seem much of enough for a
relational database and this led to a change of thoughts to make use of the
JSON file instead. If there is a future need for a larger data storage then
the program can be re-adjusted to work with a sqlite or mysql database.
SQL Alchemy may also be thought of for use. With the use of the JSON file,
our program has to write data to the file and it does so by opening the JSON
file and converting it to a dictionary object to append and modify data in it.
To achieve this, we create a dict_object function to handle the operation.
Finally, a simple function that opens the users web browser to show the online
documentation.
<h3 id="chapter4" name="chapter4">Using Qt designer with pyrcc and pyuic</h3>
The GUI basics section reveals that one of the major reasons why PyQt is the
GUI module option for registron is its WYSIWYG Qt designer. Qt designer allows
the development to be with ease as they are buttons, labels and display items
that can be dragged to a window frame to determine how the program should look.
After this whole simple design process, a .ui file is generated in XML format.
To convert this XML data to a python program, we leverlage the pyuic installation
we have. This is a python UI compiler and its goal is to translate our XML ui
to a python module. This module should be imported into our actual program as
we can't make direct changes to it since it may change each time we make GUI
updates and compile into python. Pyuic is used as shown:

```pyuic designfile.ui -o design.py```

That may be considered all that is required for the program from Qt designer but
in cases like registron where we have some images added with resource files that
are listed in a app.qrc file, we have to convert this resource files into binary
to work properly with the program. For this we use pyrcc which is python resource
compiler.

```pyrcc app.qrc > app_rc.py```

That generates a app_rc.py python module for use with our GUI module. For images
that vary in the GUI we use QPixmap to dynamically add images to the canvas so it
needs to prior compilation of binary as it just fetches the image from its source.

<h3 id="chapter5" name="chapter5">The program logic</h3>
Registron has a very simple I/O logic which will be summarized in a pseudo
code and a flow chart.
>start program

>if student: enter matric; else if administrator: goto 2;

>if matric number exists: grant access: else: display unauthorized user warning;

>if access granted: check wanted courses and click update

>while 2:

>if admin username and password is correct: grant access; else: display error;

>admin modifies program and school preferences

> end while;

> stop program

<img src="http://i.imgur.com/ELyV6AK.png" alt="Registron Flowchart">

<h3 id="chapter6" name="chapter6">Creating the windows exe with pyinstaller</h3>
Pyinstaller allows binaries for various operating system(Windows, Mac OS X, and Linux)
to be created. To create an exe for windows, it has to be bundled on a windows machine.
It also integrates [UPX (Ultimate packer for Executables)][2] into build processes when
installed. We start by running the *configure.py* file to customize pyinstaller
for our installation of python.
```python configure.py```

Now we install [UPX][2] for compressing the exe file and we navigate to our Pyinstaller
directory to run the following

```python makespec.py --onefile --upx registron.py```

```python build.py registron.spec```

Now this creates our registron.exe file and it takes a longer build time because upx
takes extra time compressing the executable.

<h3 id="chapter7" name="chapter7">References</h3>
Some useful references:
- [http://pyttsx.readthedocs.org/en/latest/][0]
- [https://github.com/parente/pyttsx][1]
- [http://upx.sourceforge.net/#download][2]
- [http://josephrex.me/getting-started-with-gui-development-in-python/][3]
- [http://pyqt.sourceforge.net/Docs/PyQt4/classes.html][4]
- [http://pyqt.sourceforge.net/Docs/PyQt4/designer.html][5]
- [https://wiki.python.org/moin/PyQt4][6]
- [http://doc.qt.digia.com/4.6/index.html][7]
- [http://www.riverbankcomputing.com/software/sip/intro][8]
- [http://pythonkit.com/PyQt-pdf.html][9]
- [http://zetcode.com/gui/pyqt4/][10]
- [http://pyqt.sourceforge.net/Docs/PyQt4/designer.html][11]
- [http://pyinstaller.org/][12]
- [https://www.google.ca/#q=text+to+speech+implementation][13]

[0]:http://pyttsx.readthedocs.org/en/latest/
[1]:https://github.com/parente/pyttsx
[2]:http://upx.sourceforge.net/#download
[3]:http://josephrex.me/getting-started-with-gui-development-in-python/
[4]:http://pyqt.sourceforge.net/Docs/PyQt4/classes.html
[5]:http://pyqt.sourceforge.net/Docs/PyQt4/designer.html
[6]:https://wiki.python.org/moin/PyQt4
[7]:http://doc.qt.digia.com/4.6/index.html
[8]:http://www.riverbankcomputing.com/software/sip/intro
[9]:http://pythonkit.com/PyQt-pdf.html
[10]:http://zetcode.com/gui/pyqt4/
[11]:http://pyqt.sourceforge.net/Docs/PyQt4/designer.html
[12]:http://pyinstaller.org/
[13]:https://www.google.ca/#q=text+to+speech+implementation