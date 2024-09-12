import os
from setuptools import setup, find_packages

# Read the contents of your README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Function to read the requirements from requirements.txt
def parse_requirements(filename):
    with open(filename, "r", encoding="utf-8") as req_file:
        return [line.strip() for line in req_file if line.strip()]

setup(
    name="your_project_name",  # Replace with your project name
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A project to handle file operations and MongoDB integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your/repo",  # Replace with your project's URL
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=parse_requirements("requirements.txt"),  # Install dependencies
    scripts=["mongo_setup.sh"],  # Include the MongoDB setup script
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "your_project_name=main:main",  # Replace with your main module function
        ],
    },
)
