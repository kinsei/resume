try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config =[
    'description': 'My Resume',
    'author': 'David Johnson',
    'url' : 'https://github.com/kinsei/resume',
    'download_url' : 'https://github.com/kinsei/resume',
    'author_email' : 'johnson.david3411@yahoo.com',
    'version' : '0.1',
    'install_requiers' : ['nose', 'termcolor'],
    'packages' : ['resume'],
    'scripts' : [],
    'name' ; 'resume'
]

setup(**config)
