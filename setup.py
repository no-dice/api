from setuptools import setup, find_packages

version = '0.0.1'

setup(name='no-dice-api',
      version=version,
      description="API for accessing No-Dice.Net.",
      long_description=open("README.md", "r").read(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "License :: OSI Approved :: BSD License",
          ],
      keywords='',
      author='T. Scott Barnes',
      author_email='tsbarnes@no-dice.net',
      url='http://github.com/no-dice/api',
      license='BSD',
      packages=find_packages(),
      install_requires=[
          "requests",
          "requests-oauth2",
          ],
      include_package_data=True,
      zip_safe=False,
    )
