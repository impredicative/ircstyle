import unittest

import ircstyle


class AttributeTests(unittest.TestCase):
    """
    Basic attribute code tests
    """

    def test_bold_with_reset(self):
        message = ircstyle.style("Hello, world!", bold=True)
        self.assertEqual(message, "\x02Hello, world!\x0F")

    def test_bold_without_reset(self):
        message = ircstyle.style("Hello, world!", bold=True, reset=False)
        self.assertEqual(message, "\x02Hello, world!")

    def test_italics_with_reset(self):
        message = ircstyle.style("Hello, world!", italics=True)
        self.assertEqual(message, "\x1DHello, world!\x0F")

    def test_italics_without_reset(self):
        message = ircstyle.style("Hello, world!", italics=True, reset=False)
        self.assertEqual(message, "\x1DHello, world!")

    def test_underline_with_reset(self):
        message = ircstyle.style("Hello, world!", underline=True)
        self.assertEqual(message, "\x1FHello, world!\x0F")

    def test_underline_without_reset(self):
        message = ircstyle.style("Hello, world!", underline=True, reset=False)
        self.assertEqual(message, "\x1FHello, world!")

    def test_complex_attributes_with_reset(self):
        message = ircstyle.style("Hello, world!", bold=True, italics=True, underline=True)
        self.assertEqual(message, "\x02\x1d\x1fHello, world!\x0F")

    def test_complex_attributes_without_reset(self):
        message = ircstyle.style("Hello, world!", bold=True, italics=True, underline=True, reset=False)
        self.assertEqual(message, "\x02\x1d\x1fHello, world!")


class ColorTests(unittest.TestCase):
    """
    Color code tests
    """

    def test_fg_white(self):
        message = ircstyle.style("Hello, world!", fg="white")
        self.assertEqual(message, "\x0300Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.white)
        self.assertEqual(message, "\x0300Hello, world!\x0F")

    def test_fg_black(self):
        message = ircstyle.style("Hello, world!", fg="black")
        self.assertEqual(message, "\x0301Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.black)
        self.assertEqual(message, "\x0301Hello, world!\x0F")

    def test_fg_blue(self):
        message = ircstyle.style("Hello, world!", fg="blue")
        self.assertEqual(message, "\x0302Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.blue)
        self.assertEqual(message, "\x0302Hello, world!\x0F")

    def test_fg_green(self):
        message = ircstyle.style("Hello, world!", fg="green")
        self.assertEqual(message, "\x0303Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.green)
        self.assertEqual(message, "\x0303Hello, world!\x0F")

    def test_fg_red(self):
        message = ircstyle.style("Hello, world!", fg="red")
        self.assertEqual(message, "\x0304Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.red)
        self.assertEqual(message, "\x0304Hello, world!\x0F")

    def test_fg_brown(self):
        message = ircstyle.style("Hello, world!", fg="brown")
        self.assertEqual(message, "\x0305Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.brown)
        self.assertEqual(message, "\x0305Hello, world!\x0F")

    def test_fg_purple(self):
        message = ircstyle.style("Hello, world!", fg="purple")
        self.assertEqual(message, "\x0306Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.purple)
        self.assertEqual(message, "\x0306Hello, world!\x0F")

    def test_fg_orange(self):
        message = ircstyle.style("Hello, world!", fg="orange")
        self.assertEqual(message, "\x0307Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.orange)
        self.assertEqual(message, "\x0307Hello, world!\x0F")

    def test_fg_yellow(self):
        message = ircstyle.style("Hello, world!", fg="yellow")
        self.assertEqual(message, "\x0308Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.yellow)
        self.assertEqual(message, "\x0308Hello, world!\x0F")

    def test_fg_lime(self):
        message = ircstyle.style("Hello, world!", fg="lime")
        self.assertEqual(message, "\x0309Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.lime)
        self.assertEqual(message, "\x0309Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.light_green)
        self.assertEqual(message, "\x0309Hello, world!\x0F")

    def test_fg_teal(self):
        message = ircstyle.style("Hello, world!", fg="teal")
        self.assertEqual(message, "\x0310Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.teal)
        self.assertEqual(message, "\x0310Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.cyan)
        self.assertEqual(message, "\x0310Hello, world!\x0F")

    def test_fg_aqua(self):
        message = ircstyle.style("Hello, world!", fg="aqua")
        self.assertEqual(message, "\x0311Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.aqua)
        self.assertEqual(message, "\x0311Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.light_cyan)
        self.assertEqual(message, "\x0311Hello, world!\x0F")

    def test_fg_royal(self):
        message = ircstyle.style("Hello, world!", fg="royal")
        self.assertEqual(message, "\x0312Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.royal)
        self.assertEqual(message, "\x0312Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.light_blue)
        self.assertEqual(message, "\x0312Hello, world!\x0F")

    def test_fg_pink(self):
        message = ircstyle.style("Hello, world!", fg="pink")
        self.assertEqual(message, "\x0313Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.pink)
        self.assertEqual(message, "\x0313Hello, world!\x0F")

    def test_fg_grey(self):
        message = ircstyle.style("Hello, world!", fg="grey")
        self.assertEqual(message, "\x0314Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.grey)
        self.assertEqual(message, "\x0314Hello, world!\x0F")

    def test_fg_silver(self):
        message = ircstyle.style("Hello, world!", fg="silver")
        self.assertEqual(message, "\x0315Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.silver)
        self.assertEqual(message, "\x0315Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.light_grey)
        self.assertEqual(message, "\x0315Hello, world!\x0F")

    def test_bg(self):
        message = ircstyle.style("Hello, world!", bg="blue")
        self.assertEqual(message, "\x0301,02Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", bg=ircstyle.colors.blue)
        self.assertEqual(message, "\x0301,02Hello, world!\x0F")

    def test_fg_and_bg(self):
        message = ircstyle.style("Hello, world!", fg="yellow", bg="blue")
        self.assertEqual(message, "\x0308,02Hello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.yellow, bg=ircstyle.colors.blue)
        self.assertEqual(message, "\x0308,02Hello, world!\x0F")

    def test_fg_and_bg_no_reset(self):
        message = ircstyle.style("Hello, world!", fg="yellow", bg="blue", reset=False)
        self.assertEqual(message, "\x0308,02Hello, world!")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.yellow, bg=ircstyle.colors.blue, reset=False)
        self.assertEqual(message, "\x0308,02Hello, world!")

    def test_fg_and_bg_with_attributes(self):
        message = ircstyle.style("Hello, world!", fg="yellow", bg="blue", bold=True, underline=True)
        self.assertEqual(message, "\x0308,02\x02\x1fHello, world!\x0F")

        message = ircstyle.style("Hello, world!", fg=ircstyle.colors.yellow, bg=ircstyle.colors.blue, bold=True, underline=True)
        self.assertEqual(message, "\x0308,02\x02\x1fHello, world!\x0F")

    def test_bad_color(self):
        self.assertRaises(TypeError, ircstyle.style, "Hello, world!", "bad_color")


class UnstyleTests(unittest.TestCase):
    def test_unstyle_complex(self):
        message = "\x0308,02\x02\x1fHello, world!\x0F"
        self.assertEqual(ircstyle.unstyle(message), "Hello, world!")

    def test_unstyle_nothing(self):
        message = "Hello, world!"
        self.assertEqual(ircstyle.unstyle(message), message)
