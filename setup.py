from setuptools import setup, find_packages


setup(
    name='HMSFirepy',
    version='0.1',
    license='MIT',
    author="Joel",
    author_email='joel.chacon@cimat.mx',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/joelchaconcastillo/OSPO-HMS-Fire-publish-pypi',
    keywords='HMSFirepy project',
    install_requires=[
          'basemap',
          'pandas',
          'matplotlib',
          'request',
          'datetime',
      ],

)
