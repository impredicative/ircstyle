import re

from . import colors

# IRC Contextual controls
NORMAL = "\x0F"
BOLD = "\x02"
ITALICS = "\x1D"
UNDERLINE = "\x1F"
COLOR = "\x03"


def _color_code(color):
    """
    Returns a formatted color code.

    Args:
        color (str or int): Input can either be a string (the name of the color, e.g. red), or an int pulled
        from a color constant (e.g. ircstyle.colors.red)

    Raises:
        TypeError: Raised if the supplied color does not exist

    Returns:
        str: Formatted IRC color code with a leading zero
    """
    # Default to black if no color is provided
    if color is None:
        color = "black"

    if isinstance(color, str):
        try:
            color = getattr(colors, color)
        except AttributeError:
            raise TypeError("Unknown color: {c}".format(c=color))

    return str(color).zfill(2)


def style(text, fg=None, bg=None, bold=False, italics=False, underline=False, reset=True):
    """
    Styles text with IRC attribute and / or color codes and returns the new string.
    By default, the styling is self contained, which means that at the end of the string
    a reset ("normal") code is issued. This can be prevented by passing ``reset=False``.

    Examples:
        ircstyle.style('Hello World!', fg='green')
        ircstyle.style('ATTENTION!', bold=True, underline=True)
        ircstyle.style('Some things', bg=ircstyle.colors.teal)

    Supported color names:

    * ``white``
    * ``black``
    * ``blue``
    * ``green``
    * ``red``
    * ``brown``
    * ``purple``
    * ``orange``
    * ``yellow``
    * ``lime`` (light_green)
    * ``teal`` (cyan)
    * ``aqua`` (light_cyan)
    * ``royal`` (light_blue)
    * ``pink``
    * ``grey``
    * ``silver`` (light_grey)

    Args:
        text (str): The string to style with attribute / color codes
        fg (Optional[str, int or None]): The foreground color. This should be either the name of the color or the
            color code referenced from a constant in ircstyle.colors. Defaults to None.
        bg (Optional[str, int or None]): The background color. This should be either the name of the color or the
            color code referenced from a constant in ircstyle.colors. Defaults to None.
        bold (Optional[bool]): Enable bold formatting. Defaults to False.
        italics (Optional[bool]): Enable italic formatting. Defaults to False.
        underline (Optional[bool]): Enable underline formatting. Defaults to False.
        reset (Optional[bool]): By default a reset-all code is added at the end of the string, which means
            that styles do not carry over. This can be disabled to compose styles.

    Returns:
        str: The message with all formatting codes applied.
    """
    bits = []

    # Apply foreground / background colors
    if (fg is not None) or (bg is not None):
        fg = _color_code(fg)

        # Foreground and background or foreground only?
        if bg:
            bg = _color_code(bg)

            color_template = "{color_ctrl}{fg_code},{bg_code}"
            color_code = color_template.format(color_ctrl=COLOR, fg_code=fg, bg_code=bg)
            bits.append(color_code)
        else:
            color_template = "{color_ctrl}{fg_code}"
            color_code = color_template.format(color_ctrl=COLOR, fg_code=fg)
            bits.append(color_code)

    # Apply contextual formatting
    if bold:
        bits.append(BOLD)

    if italics:
        bits.append(ITALICS)

    if underline:
        bits.append(UNDERLINE)

    bits.append(text)

    if reset:
        bits.append(NORMAL)

    return "".join(bits)


def unstyle(text):
    """
    Removes color / attribute codes from an IRC message.

    Args:
        text (str): The text to remove style information from.

    Returns:
        str: The raw (unformatted) message.
    """
    # Strip attribute codes first
    for code in (NORMAL, BOLD, ITALICS, UNDERLINE):
        text = text.replace(code, "")

    text = re.sub(r"\x03(?P<fg>\d{2})(,(?P<bg>\d{2}))?", "", text)

    return text
