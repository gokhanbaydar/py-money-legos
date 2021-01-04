import setuptools
import os


def get_files_in_dir(dirName):
    listOfFile = os.listdir(dirName)
    completeFileList = list()
    for file in listOfFile:
        completePath = os.path.join(dirName, file)
        if os.path.isdir(completePath):
            completeFileList = completeFileList + get_files_in_dir(completePath)
        else:
            completeFileList.append(completePath)
    return completeFileList


def find_json_files():
    json_files = []
    files = get_files_in_dir(".")
    for file in files:
        root, extension = os.path.splitext(file)
        if extension == ".json":
            json_files.append(file)
    return json_files


with open("MANIFEST.in", "w") as mfs:
    for file in find_json_files():
        mfs.write("include " + file + "\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="py-money-legos",
    version="0.1.1",
    author="Gokhan Baydar",
    author_email="gokhanbaydar@yahoo.com",
    description="money-legos for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gokhanbaydar/py-money-legos",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)