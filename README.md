# IRC Style
[![Build Status](https://travis-ci.org/FujiMakoto/IRC-Message.svg?branch=master)](https://travis-ci.org/FujiMakoto/IRC-Message)
[![Coverage Status](https://coveralls.io/repos/FujiMakoto/IRC-Message/badge.svg?branch=master&service=github)](https://coveralls.io/github/FujiMakoto/IRC-Message?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/8f58d6b6195f4a0f82d2e1c8fc6a209b)](https://www.codacy.com/app/makoto_2/IRC-Message)

IRC Message is a simple Python module for applying and stripping formatting from IRC messages. Its primary purpose is for use with Python based IRC bots.

The modules syntax was heavily inspired by [Click](http://click.pocoo.org/5/utils/#ansi-colors)'s own style and unstyle methods.

## Installation
You can install the IRC Message Formatter module via pip,

```pip install ircstyle```

This module provides two primary methods, **style** and **unstyle**

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
