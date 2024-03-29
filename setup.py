from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mexico_einvoice/__init__.py
from mexico_einvoice import __version__ as version

setup(
	name="mexico_einvoice",
	version=version,
	description="Mexico Einvoice",
	author="Beveren-Software-Inc",
	author_email="info@beverensoftware.ca",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
