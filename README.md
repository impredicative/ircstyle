# ircstyle
**ircstyle** is a Python package for applying and stripping formatting from IRC messages. Its primary purpose is for use with Python based IRC bots.

## Links
* Code: https://github.com/impredicative/ircstyle/
* Release: https://pypi.org/project/ircstyle/
* Changelog: https://github.com/impredicative/ircstyle/releases

## Usage
This package provides two primary methods, **style** and **unstyle**

### Style
```python
ircmessage.style(text, fg=None, bg=None, bold=False, italics=False, underline=False, reset=True):
```
This method is used to style text with IRC attribute and / or color codes.

Examples:
```python
ircmessage.style('Hello World!', fg='green')
```
```python
ircmessage.style('ATTENTION!', bold=True, underline=True)
```
```python
ircmessage.style('Some things', bg=ircmessage.colors.teal)
```

### Unstyle
```python
ircmessage.unstyle(text)
```
This method is used to strip all formatting control codes from IRC messages so that you can safely display and log the contents outside of IRC in a printable format.
