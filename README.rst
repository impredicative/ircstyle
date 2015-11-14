IRC Message
===========

|Build Status| |Coverage Status| |Codacy Badge|

IRC Message is a simple Python module for applying and stripping
formatting from IRC messages. Its primary purpose is for use with Python
based IRC bots.

The modules syntax was heavily inspired by
`Click <http://click.pocoo.org/5/utils/#ansi-colors>`__'s own style and
unstyle methods.

Installation
------------

You can install the IRC Message Formatter module via pip,

``pip install ircmessage``

This module provides two primary methods, **style** and **unstyle**

Style
~~~~~

.. code:: python

    ircmessage.style(text, fg=None, bg=None, bold=False, italics=False, underline=False, reset=True):

This method is used to style text with IRC attribute and / or color
codes.

Examples:

.. code:: python

    ircmessage.style('Hello World!', fg='green')

.. code:: python

    ircmessage.style('ATTENTION!', bold=True, underline=True)

.. code:: python

    ircmessage.style('Some things', bg=ircmessage.colors.teal)

Unstyle
~~~~~~~

.. code:: python

    ircmessage.unstyle(text)

This method is used to strip all formatting control codes from IRC
messages so that you can safely display and log the contents outside of
IRC in a printable format.

License
-------

::

    The MIT License (MIT)

    Copyright (c) 2015 Makoto Fujimoto

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

.. |Build Status| image:: https://travis-ci.org/FujiMakoto/IRC-Message.svg?branch=master
   :target: https://travis-ci.org/FujiMakoto/IRC-Message
.. |Coverage Status| image:: https://coveralls.io/repos/FujiMakoto/IRC-Message/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/FujiMakoto/IRC-Message?branch=master
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/grade/8f58d6b6195f4a0f82d2e1c8fc6a209b
   :target: https://www.codacy.com/app/makoto_2/IRC-Message
