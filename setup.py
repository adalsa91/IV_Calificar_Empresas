# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup
from pip.req import parse_requirements
from codecs import open

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

#here = os.path.abspath(os.path.dirname(__file__))

# with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Calificar Empresas',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Aplicación para valorar empresas de prácticas.',
    long_description=README.

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
    install_requires=reqs,

    keywords='education companies students practice',
)
