# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='Calificar Empresas',
    version='0.1',
    description='Aplicación para valorar empresas de prácticas.',
    url='https://github.com/adalsa91/IV_Calificar_Empresas',
    author='Adrián Álvarez Sáez',
    author_email='adalsa91@gmail.com',

    license='GNU GPLv3',

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Education',
        'Development Status :: 3 - Alpha',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',

    ],
    install_requires=[
        'Django==1.8.5',
        'sqlite3',
    ],

    keywords='education companies students practice',
)
