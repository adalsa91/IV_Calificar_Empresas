# -*- coding: utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Calificar Empresas',
    version='0.1',
    description='Aplicación para valorar empresas de prácticas.',

    url='https://github.com/adalsa91/IV_Calificar_Empresas',

    author='Adrián Álvarez Sáez',
    author_email='adalsa91@gmail.com',

    license='GNU GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django :: 1.8',

    ],
    install_requires=reqs,

    keywords='education companies students practice',
)
