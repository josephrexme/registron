Registron
=========

Registron is a speech-based registration program

#### Build Information
- Python 2.7
- PyQt4
- Pyuic 4.9.3
- Qt 4.8.3

#### Third Party Modules
- Pyttsx (Python Text To Speech)

> To run from source files directly, switch to the source branch and simply run

```python registron.py``` or ```./registron.py``` in *nix like systems. Windows users can also run this from Idle.

```flow
st=>start: Start
e=>end
op=>operation: Run Registron
cond=>condition: Exit program?

st->op->cond
cond(yes)->e
cond(no)->op
```
