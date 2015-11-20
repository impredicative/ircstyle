from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='ircmessage',
    version='0.1.1',
    description='A simple Python module for applying and stripping formatting from IRC messages.',
    long_description=readme(),
    author='Makoto Fujimoto',
    author_email='makoto@makoto.io',
    url='https://github.com/FujiMakoto/IRC-Message-Formatter',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Text Processing'
    ],
    packages=find_packages(exclude=['tests']),
    entry_points={},
    install_requires=['six>=1.10.0,<1.11'],

    keywords=['irc', 'internet relay chat'],
)
