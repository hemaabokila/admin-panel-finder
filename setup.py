from setuptools import setup, find_packages

setup(
    name="admin-panel-finder",
    version="1.0.0",
    author="Ibrahem abo kila",
    author_email="ibrahemabokila@gmail.com",
    description="A simple DDoS attack simulation tool.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hemaabokila/admin-panel-finder",
    packages=find_packages(),
    package_data={
        '': ['wordlists/wordlist.txt'], 
        },
    install_requires=[
	'requests',
        'colorama',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'adminp=admin.main:main', 
        ],
    },
)

