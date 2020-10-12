# ircstyle
**ircstyle** is a Python 3.7+ package for applying and stripping formatting from IRC messages. 
Its primary purpose is for use with Python based IRC bots.

[![cicd badge](https://github.com/impredicative/ircstyle/workflows/cicd/badge.svg?branch=master)](https://github.com/impredicative/ircstyle/actions?query=workflow%3Acicd+branch%3Amaster)

## Links
* Code: https://github.com/impredicative/ircstyle/
* Release: https://pypi.org/project/ircstyle/
* Changelog: https://github.com/impredicative/ircstyle/releases

## Usage
This package provides two primary methods, **style** and **unstyle**.

### Style
This method is used to style text with IRC attribute and / or color codes.
```python
import ircstyle

ircstyle.style('Hi there', fg='blue', bg='white', bold=True, italics=True, underline=True, reset=True)
'\x0302,00\x02\x1d\x1fHi there\x0f'

ircstyle.style('Hello World!', fg='green', reset=False)
'\x0303Hello World!'

ircstyle.style('ATTENTION!', bold=True, underline=True)
'\x02\x1fATTENTION!\x0f'

ircstyle.style('Something', bg=ircstyle.colors.teal)
'\x0301,10Something\x0f'
```

### Unstyle
This method is used to strip all formatting control codes from IRC messages so that you can safely use the contents outside of IRC in a printable format.
```python
import ircstyle

ircstyle.unstyle('\x02message\x0f')
'message'

ircstyle.unstyle('message')
'message'
```
