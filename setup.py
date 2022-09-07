from setuptools import setup, find_packages

setup(name='my_garage',
      description='My Garage',
      long_description='My Garage Car Sales',
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version='1.0.0',
      install_requires=[
          'gevent==21.12.0',
          'gunicorn==20.1.0',
          'django==4.1.1',
          'django-filter==22.1',
          'djangorestframework==3.13.1',
          'django-environ==0.9.0',
          'django-extensions==3.2.0',
          'django-choices==1.7.2',
          'django-cors-headers==3.13.0',
      ],
      extras_require={
          'dev': [
              'pycodestyle==2.9.1',
              'flake8==5.0.4',
          ],
      }
      )
