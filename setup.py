from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='ollamatui',
   version='0.0.1',
   description='A minimal front-end for Ollama.',
   author='wgelyjr',
   author_email='wgelyjr@gmail.com',
   packages=['ollamatui'],
   install_requires=['ollama'],
   long_description=long_description,
   entry_points={
        'console_scripts': [
            'ollamatui=ollamatui.main:main'
        ]
   }
)