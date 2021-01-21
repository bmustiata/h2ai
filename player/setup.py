from setuptools import setup
from setuptools import find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

packages = find_packages()

setup(
    name="h2_player",
    version="1.0.0",
    description="h2_player",
    long_description=readme,
    author="Bogdan Mustiata",
    author_email="bogdan.mustiata@gmail.com",
    license="BSD",
    entry_points={
        "console_scripts": ["h2_player = h2_player.mainapp:main"]
    },
    install_requires=[],
    packages=packages,
    package_data={
        "": ["*.txt", "*.rst"],
        "h2_player": ["py.typed"],
    },
)
