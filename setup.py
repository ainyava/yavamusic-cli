from distutils.core import setup

setup(
    name='ainmusic',
    packages=[
        'ainmusic',
        'ainmusic.commands',
        'ainmusic.configs'
    ],
    version='0.0.6',
    license='GNU General Public License v3 (GPLv3)',
    author='Hamed Mahmoudkhani',
    author_email='ainyava@gmail.com',
    url='https://github.com/ainyava/ainmusic',
    keywords=['Mojo Music', 'Music', 'Download'],
    description='A python module to download and manage music.',
    long_description='A python module to download and manage music.',
    scripts=['bin/ainmusic'],
    console=['bin/ainmusic'],
    install_requires=[
        'bs4',
        'progressbar',
        'selenium',
        'eyed3'
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
