from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Malibu-lambda-1",
    version="1.2",
    author="Monica Bustamante",
    author_email="mbustamante@monicadatascience.com",
    description="Incomedata",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/s2t2/game-utils-py",
    keywords="Income",
    packages=find_packages() # ["game_utils"]
)