from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='ollama-tui',
   version='0.0.1',
   description='A minimal front-end for Ollama.',
   author='wgelyjr',
   author_email='wgelyjr@gmail.com',
   packages=['ollama-tui'],
   install_requires=['ollama'],
   long_description=long_description
)