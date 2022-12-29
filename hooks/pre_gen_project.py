"""
This runs before baking the project. Here we enforce certain validations on input data
and set additional cookiecutter variables (by modifying the Jinja context).

See: https://github.com/samj1912/cookiecutter-advanced-demo/blob/master/hooks/pre_gen_project.py
for more details.

The python target version is always the last supported version (they must be ordered).
The python target environment is constructed by prefixing 'py' to the target version
after stripping the version dot ("."). For example, if `python_target_version = 3.7`
then `python_target_env = py37`:

{{ cookiecutter.update({"python_target_version":  cookiecutter.python_versions[-1] }) }}
{{ cookiecutter.update({"python_target_env": 'py' + cookiecutter.python_versions[-1].replace('.','') }) }}
"""

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    #Exit to cancel project
    sys.exit(1)
