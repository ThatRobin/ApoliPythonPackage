import shutil
import os
from git import Repo
from git import rmtree
from generate_types import generate_types

def update_wiki():
    rmtree('../wiki/')
    Repo.clone_from("https://github.com/apace100/origins-docs.git", "../wiki/")
    generate_types()
