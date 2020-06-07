# ircstyle
**ircstyle** is a Python 3.7+ package for applying and stripping formatting from IRC messages. 
Its primary purpose is for use with Python based IRC bots.

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

ircstyle.style(text, fg=None, bg=None, bold=False, italics=False, underline=False, reset=True)
```

Examples:
```python
ircstyle.style('Hello World!', fg='green')
```
```python
ircstyle.style('ATTENTION!', bold=True, underline=True)
```
```python
ircstyle.style('Some things', bg=ircstyle.colors.teal)
```

### Unstyle
This method is used to strip all formatting control codes from IRC messages so that you can safely display and log the contents outside of IRC in a printable format.
```python
import ircstyle

ircstyle.unstyle(text)
```
