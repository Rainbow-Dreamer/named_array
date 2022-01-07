from setuptools import setup, find_packages
from os import path

setup(
    name='named_array',
    py_modules=['named_array'],
    version='0.11',
    license='LGPLv2.1',
    description=
    'This is a python module that extends numpy array to be able to have column names to index with',
    author='Rainbow-Dreamer',
    author_email='1036889495@qq.com',
    install_requires=['py'],
    url='https://github.com/Rainbow-Dreamer/named_array',
    download_url=
    'https://github.com/Rainbow-Dreamer/named_array/archive/0.11.tar.gz',
    keywords=['python', 'hide warnings'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    include_package_data=True)
