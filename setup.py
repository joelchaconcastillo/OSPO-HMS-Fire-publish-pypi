from setuptools import setup, find_packages


setup(
    name='example_publish_pypi',
    version='0.1',
    license='MIT',
    author="Giorgos Myrianthous",
    author_email='email@example.com',
    packages=find_packages('example_publish_pypi'),
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],
)
