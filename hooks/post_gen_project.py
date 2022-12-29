#!/usr/bin/env python

"""
Post generation hooks (delete unneeded files)
"""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    """Removes a file from the project directory"""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_folder(filepath):
    """Removes a folder from the project directory"""
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    if '{{ cookiecutter.project_type }}' != 'application':
        remove_folder('docker')
