from .config import IrcMessageTestCase
import ircmessage


class AttributeTests(IrcMessageTestCase):
    """
    Basic attribute code tests
    """
    def test_bold_with_reset(self):
        message = ircmessage.style('Hello, world!', bold=True)
        self.assertEqual(message, '\x02Hello, world!\x0F')

    def test_bold_without_reset(self):
        message = ircmessage.style('Hello, world!', bold=True, reset=False)
        self.assertEqual(message, '\x02Hello, world!')

    def test_italics_with_reset(self):
        message = ircmessage.style('Hello, world!', italics=True)
        self.assertEqual(message, '\x1DHello, world!\x0F')

    def test_italics_without_reset(self):
        message = ircmessage.style('Hello, world!', italics=True, reset=False)
        self.assertEqual(message, '\x1DHello, world!')

    def test_underline_with_reset(self):
        message = ircmessage.style('Hello, world!', underline=True)
        self.assertEqual(message, '\x1FHello, world!\x0F')

    def test_underline_without_reset(self):
        message = ircmessage.style('Hello, world!', underline=True, reset=False)
        self.assertEqual(message, '\x1FHello, world!')

    def test_complex_attributes_with_reset(self):
        message = ircmessage.style('Hello, world!', bold=True, italics=True, underline=True)
        self.assertEqual(message, '\x02\x1d\x1fHello, world!\x0F')

    def test_complex_attributes_without_reset(self):
        message = ircmessage.style('Hello, world!', bold=True, italics=True, underline=True, reset=False)
        self.assertEqual(message, '\x02\x1d\x1fHello, world!')


class ColorTests(IrcMessageTestCase):
    """
    Color code tests
    """
    def test_fg_white(self):
        message = ircmessage.style('Hello, world!', fg='white')
        self.assertEqual(message, '\x0300Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.white)
        self.assertEqual(message, '\x0300Hello, world!\x0F')

    def test_fg_black(self):
        message = ircmessage.style('Hello, world!', fg='black')
        self.assertEqual(message, '\x0301Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.black)
        self.assertEqual(message, '\x0301Hello, world!\x0F')

    def test_fg_blue(self):
        message = ircmessage.style('Hello, world!', fg='blue')
        self.assertEqual(message, '\x0302Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.blue)
        self.assertEqual(message, '\x0302Hello, world!\x0F')

    def test_fg_green(self):
        message = ircmessage.style('Hello, world!', fg='green')
        self.assertEqual(message, '\x0303Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.green)
        self.assertEqual(message, '\x0303Hello, world!\x0F')

    def test_fg_red(self):
        message = ircmessage.style('Hello, world!', fg='red')
        self.assertEqual(message, '\x0304Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.red)
        self.assertEqual(message, '\x0304Hello, world!\x0F')

    def test_fg_brown(self):
        message = ircmessage.style('Hello, world!', fg='brown')
        self.assertEqual(message, '\x0305Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.brown)
        self.assertEqual(message, '\x0305Hello, world!\x0F')

    def test_fg_purple(self):
        message = ircmessage.style('Hello, world!', fg='purple')
        self.assertEqual(message, '\x0306Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.purple)
        self.assertEqual(message, '\x0306Hello, world!\x0F')

    def test_fg_orange(self):
        message = ircmessage.style('Hello, world!', fg='orange')
        self.assertEqual(message, '\x0307Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.orange)
        self.assertEqual(message, '\x0307Hello, world!\x0F')

    def test_fg_yellow(self):
        message = ircmessage.style('Hello, world!', fg='yellow')
        self.assertEqual(message, '\x0308Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.yellow)
        self.assertEqual(message, '\x0308Hello, world!\x0F')

    def test_fg_lime(self):
        message = ircmessage.style('Hello, world!', fg='lime')
        self.assertEqual(message, '\x0309Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.lime)
        self.assertEqual(message, '\x0309Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.light_green)
        self.assertEqual(message, '\x0309Hello, world!\x0F')

    def test_fg_teal(self):
        message = ircmessage.style('Hello, world!', fg='teal')
        self.assertEqual(message, '\x0310Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.teal)
        self.assertEqual(message, '\x0310Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.cyan)
        self.assertEqual(message, '\x0310Hello, world!\x0F')

    def test_fg_aqua(self):
        message = ircmessage.style('Hello, world!', fg='aqua')
        self.assertEqual(message, '\x0311Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.aqua)
        self.assertEqual(message, '\x0311Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.light_cyan)
        self.assertEqual(message, '\x0311Hello, world!\x0F')

    def test_fg_royal(self):
        message = ircmessage.style('Hello, world!', fg='royal')
        self.assertEqual(message, '\x0312Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.royal)
        self.assertEqual(message, '\x0312Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.light_blue)
        self.assertEqual(message, '\x0312Hello, world!\x0F')

    def test_fg_pink(self):
        message = ircmessage.style('Hello, world!', fg='pink')
        self.assertEqual(message, '\x0313Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.pink)
        self.assertEqual(message, '\x0313Hello, world!\x0F')

    def test_fg_grey(self):
        message = ircmessage.style('Hello, world!', fg='grey')
        self.assertEqual(message, '\x0314Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.grey)
        self.assertEqual(message, '\x0314Hello, world!\x0F')

    def test_fg_silver(self):
        message = ircmessage.style('Hello, world!', fg='silver')
        self.assertEqual(message, '\x0315Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.silver)
        self.assertEqual(message, '\x0315Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.light_grey)
        self.assertEqual(message, '\x0315Hello, world!\x0F')

    def test_bg(self):
        message = ircmessage.style('Hello, world!', bg='blue')
        self.assertEqual(message, '\x0301,02Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', bg=ircmessage.colors.blue)
        self.assertEqual(message, '\x0301,02Hello, world!\x0F')

    def test_fg_and_bg(self):
        message = ircmessage.style('Hello, world!', fg='yellow', bg='blue')
        self.assertEqual(message, '\x0308,02Hello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.yellow, bg=ircmessage.colors.blue)
        self.assertEqual(message, '\x0308,02Hello, world!\x0F')

    def test_fg_and_bg_no_reset(self):
        message = ircmessage.style('Hello, world!', fg='yellow', bg='blue', reset=False)
        self.assertEqual(message, '\x0308,02Hello, world!')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.yellow, bg=ircmessage.colors.blue, reset=False)
        self.assertEqual(message, '\x0308,02Hello, world!')

    def test_fg_and_bg_with_attributes(self):
        message = ircmessage.style('Hello, world!', fg='yellow', bg='blue', bold=True, underline=True)
        self.assertEqual(message, '\x0308,02\x02\x1fHello, world!\x0F')

        message = ircmessage.style('Hello, world!', fg=ircmessage.colors.yellow, bg=ircmessage.colors.blue,
                                   bold=True, underline=True)
        self.assertEqual(message, '\x0308,02\x02\x1fHello, world!\x0F')

    def test_bad_color(self):
        self.assertRaises(TypeError, ircmessage.style, 'Hello, world!', 'bad_color')


class UnstyleTests(IrcMessageTestCase):

    def test_unstyle_complex(self):
        message = '\x0308,02\x02\x1fHello, world!\x0F'
        self.assertEqual(ircmessage.unstyle(message), 'Hello, world!')

    def test_unstyle_nothing(self):
        message = 'Hello, world!'
        self.assertEqual(ircmessage.unstyle(message), message)
