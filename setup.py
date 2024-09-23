from setuptools import setup, find_packages

from my_garage.settings import PROJECT_NAME, PROJECT_DESCRIPTION, PROJECT_VERSION

setup(name=PROJECT_NAME,
      description=PROJECT_DESCRIPTION,
      long_description=PROJECT_DESCRIPTION,
      packages=find_packages(exclude=["*tests*"]),
      package_data={'': ['*.yaml']},
      version=PROJECT_VERSION,
      install_requires=[
          'gevent==21.12.0',
          'gunicorn==20.1.0',
          'django==4.1.13',
          'django-filter==22.1',
          'djangorestframework==3.13.1',
          'django-environ==0.9.0',
          'django-extensions==3.2.0',
          'django-choices==1.7.2',
          'django-cors-headers==3.13.0',
          'psycopg2==2.9.3',
          'drf-yasg==1.21.3',
          'whitenoise==6.2.0',
          'requests==2.28.1',
      ],
      extras_require={
          'dev': [
              'pycodestyle==2.9.1',
              'flake8==5.0.4',
          ],
      }
      )
