from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Malibu-lambda-1",
    version="0.1",
    author="Monica Bustamante",
    author_email="mbustamante@monicadatascience.com",
    description="Incomedata package for lambda school Ds Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/Moly-malibu/lambdata-inclass-first",
    keywords="Income",
    packages=find_packages() # ["my_lambdate"]
)