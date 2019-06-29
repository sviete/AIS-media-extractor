# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='ais_media_extractor',
    version='0.3',
    description='A REST API server for getting the info for videos from different sites',
    long_description='A REST API server for getting the info for videos from different sites, powered by youtube-dl and youtube-dl-api-server',
    author='Andrzej Raczkowski',
    author_email='info@sviete.pl',
    url='https://github.com/sviete/AIS-media-extractor',
    packages=['ais_media_extractor'],
    entry_points={
        'console_scripts': [
            'ais-media-extractor = ais_media_extractor.server:main',
        ],
    },

    install_requires=[
        'Flask',
        'youtube_dl >= 2019.06.27',
    ],

    classifiers=[
        'Topic :: Multimedia :: Video',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
