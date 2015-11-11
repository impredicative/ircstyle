from setuptools import setup, find_packages

setup(
    name='IRC Message Parser',
    version='0.1.0',
    description='IRC Message Parser',
    long_description='IRC Message Parser',
    author='Makoto Fujimoto',
    author_email='makoto@makoto.io',
    url='https://github.com/FujiMakoto/IRC-Message-Parser',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    entry_points={},
    install_requires=['six']
)