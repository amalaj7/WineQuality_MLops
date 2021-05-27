# To create a template like cookiecutter

import os

# Creating Directories

dirs = [
    os.path.join("data", "raw"),       # to create raw inside data folder(join)
    os.path.join("data","processed"),  # to create processed inside data folder(join)
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)                       # if it exist replace it
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:   # since all dirs are empty we create .gitkeep in every dir for git push
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",                             # Ignore these files
    os.path.join("src","__init__.py")         # __init__.py - src as a python package
]

for file_ in files:
    with open(file_, "w") as f:
        pass