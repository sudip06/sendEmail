try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
name='SendEmail',
version='0.1.dev0',
packages=['SendEmail'],
#packages=['smtplib','string','email','getpass','validate_email'],
license='Common License',
install_requires=[
"smtplib",
"email",
"getpass",
"sys",
"os",
],
long_description="",
)

