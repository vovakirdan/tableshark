from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='tableshark',
      version='0.0.3',
      description='A simple table management tool',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author_email='vladimir.kirdan@bk.ru',
      author='vladimirkirdan',
      install_requires=['pandas>=2.0.2', 'openpyxl>=3.0.7'],
      packages=find_packages(),
      python_requires='>=3.7'
)
