# installing python packages with pips-------------------------------

# pip install flask
# pip uninstall flask 
# pip install -r requirement.txt

#  pip install flask -U

#virtualenv ---------------------------------------------------------
# A virtual environment is simply a tool that separates the dependencies of different projects by creating 
# a separate isolated environment for each project.
# If you install two different versions of the same package into your global Python environment, 
# the second installation overwrites the first one. For the same reason, having a single virtual environment for 
# both clients won’t work either. You can’t have two different versions of the same package in a single Python environment.

# <!-- creating virtual environment -->
# pip install virtualenv
# virtualenv simple_django_project
# simple_django_project\Scripts\activate


# DJANGO-----------------------------------using virtualenv
from tkinter import PROJECTING
from venv import create
import django
import virtualenv


# pip install virtualenv --- download virtualenv
# mkdir django_project
# cd into it
# virtualenv simple_project_django
# get-ExecutionPolicy -- check if restricted or not
# Set-ExecutionPolicy Unrestricted -Scope Process
# django_project_env1\Scripts\activate --- while inside your created folder
#create repo same directory, same directory as virtualenv
# create django project (virtualenv) inside repo
# create django app   (virtualenv) same directory as project
# pip freeze > requirements.txt