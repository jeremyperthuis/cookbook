from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='process',
      version='1.0',
      description='Python example package',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author='Perthuis Jeremy',
      author_email='jeremy',
      url='https://www.python.org/',
      packages=['process'],
     )
