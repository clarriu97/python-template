# Contributing to {{cookiecutter.project_slug}}

Contributions are welcome! You can make this project better by:

* Proposing and implementing new features
* Reporting and fixing bugs
* Discussing the current state of the code

Please read the following sections carefully to discover how you can contribute to this project.

## Proposing Features

To propose new features, please [submit a feature request issue]({{ cookiecutter.project_url }}/-/issues/new?issuable_template=Feature). Take your time to fill this issue carefully and provide enough detail so we can be sure we're building the right thing. We recommend you:

* Search [existing issues]({{ cookiecutter.project_url }}/-/issues?scope=all&&state=all&label_name[]=feature) to see if this feature or a similar one has already been requested or implemented
* If the feature has already been requested but not implemented, you can leave a comment indicating that you are interested on it. If you're acting on behalf of a customer (e.g. customer success or sales representative) please try to explain the business opportunity in detail so we can prioritize it appropriately.

## Reporting Bugs

If you find any bug on this software, please [submit a bug issue]({{ cookiecutter.project_url }}/-/issues/new?issuable_template=Bug). When filling a bug report:

* Search [existing issues]({{ cookiecutter.project_url }}/-/issues?scope=all&&state=all&label_name[]=bug) to make sure the bug has not been already reported
* Gather as much information as possible: steps to reproduce, relevant logs/screenshots, versions affected, configuration, etc. The more details you can provide the better
* If the bug is related to third-party software we're using, search on the Internet (GitHub, StackOverflow, etc.) to see if it is a known bug and there is any available solution or workaround you can use

## Working on Issues

You can browse the list of [open issues]({{ cookiecutter.project_url }}/-/issues?scope=all&state=opened) to find things to work on in this project. Please consider:

* Make sure no one is working on a particular issue already. If the issue is not assigned or not labeled with the `doing` tag, it's safe to assume you can pick it up.
* Take a look at the project's backlog and favor high-priority issues. If you have any questions, You can reach out to the team manager or product owner to get assurances.
* Assign the issue to yourself and add the label `doing` when you're about to start doing work.
* Create a branch and a draft pull request (PR).

## Getting Started

Ready to contribute? Here's how to set up {{cookiecutter.project_slug}} for local development. Before you start you will need the following software installed on your machine:

* [Python](https://www.python.org/): {% for python_version in cookiecutter.python_versions %}{{python_version}}{% if not loop.last %},{% endif %}{% endfor %}
* Python-dev: {% for python_version in cookiecutter.python_versions %}[{{python_version}}-dev](https://packages.ubuntu.com/search?keywords=python{{python_version}}-dev){% if not loop.last %},{% endif %}{% endfor %}
* [pip](https://pip.pypa.io/en/stable/): 19.3+
* [tox](https://pypi.org/project/tox/): 3.14+
* [virtualenv](https://pypi.org/project/virtualenv/): 16.7+
* [git](https://git-scm.com/)
* [GNU make](https://www.gnu.org/software/make/): 4.1+
* [Docker](https://www.docker.com/): 19.3+

Please take a look at the documentation of your OS or distribution on how to install these software dependencies.

Once you have everything ready, you can start contributing to the project. Before doing do, please make sure you understand what code style you should follow, conventions, branching strategy, pull request requirements, etc. In case of doubt, contact any of the maintainers of the project (i.e. {{cookiecutter.author}}) or a member of the appropriate team. You can use the following basic workflow:

1. (First time) Clone this repository on your development machine and `cd` into the newly created folder.
1. Fetch all remote branches: `git fetch origin`
1. Checkout your issue branch: `git checkout -b "<branch name>" "origin/<branch name>"` If you've created a Pull request too (recommended), you can get the full instructions to do this on the PR page.
1. Create a development virtual environment: `make env-create`
1. Activate the environment: `source ./.tox/{{cookiecutter.project_slug}}/bin/activate`
1. (Optional) Add the required dependencies for production (`requirements.in`) and/or development (`requirements-dev.in`) and compile them: `make env-compile` (run `make env-create` afterwards to regenerate the environment)
1. Make your changes!
1. Make sure the code complies with code style conventions (PEP8) and looks correct (pylint): `make code-style` and `make lint`.
1. Make sure the files you add are not ignored by `.gitignore`.
1. Write tests and ensure they follow conventions: `make lint-tests`
1. Run the tests: `make test`
1. Check the code for security vulnerabilities: `make security` and `make check-dependencies`
1. Inspect the code metrics to assess that there is no unneeded complexity (refactor): `make code-metrics`
1. Update the documentation and generate it with: `make docs`
1. Update the `CHANGELOG.md`. Please follow the [Keep a Changelog](https://keepachangelog.com/en/1.0.0) conventions and add the changes to the `Unreleased` section (see [effort](https://keepachangelog.com/en/1.0.0/#effort) for more details)
1. Push your changes!
1. Check that the CI pipeline runs all steps successfully

While working on your changes, please keep in mind:

1. Try to use short-lived branches (ideally they shouldn't last more than 1 day) and rebase/merge frequently to master (see [Continuous Integration](https://www.martinfowler.com/articles/continuousIntegration.html)).
1. You can split big features or changes into smaller sub-tasks (with corresponding issues, branches and/or pull requests) to ensure the PRs are of a manageable size and you can integrate your work continuously to `master` (avoid merge hell).
1. Make sure the pipeline stays green at all times. If it fails, fix it before adding new code.
1. Make sure you're adding tests for the new code and the coverage metric is not getting degraded.
1. If your team supports it, favor [Trunk Based Development](https://trunkbaseddevelopment.com/) over branching to gain velocity.

For a more comprehensive list of scripted operations, please take a look at the [Using the `Makefile`](#using-the-makefile) section.

## Submitting a Pull Request (PR)

Once you've made the needed changes to the project on your own branch, you can submit a Pull Request (PR) to bring those changes to the main integration branch (typically `master`). Please follow the next steps:

1. If you haven't done so, [create a PR]({{ cookiecutter.project_url }}/-/pull_requests/new) and link it to the proper issue.
1. Make sure the pipeline passes
1. Mark the PR as ready
1. Assign one or more reviewers to the PR. Ideally these should be people with experience on the project that can understand the code and provide useful insights on how to improve it
1. Review the comments and make the needed changes. Make sure the pipeline stays green as you refactor the code
1. If a particular comment can't be addressed at the moment, create a follow-up issue
1. If the code review is done, merge your changes or ask a maintainer to do it for you!

## Releasing

If a new version of the software is ready to be released. Please follow the next procedure:

1. Create a new section (titled with the version and release date) on the `CHANGELOG.md` and move everything under the `Unreleased` section to this new section. Commit and push your changes.
1. Bump the version number with: `make version-bump-tag PART=minor` (where `PART` can be `major`, `minor` or `patch`). If you do it manually, please follow [Semantic Versioning](https://semver.org/)
1. If you've bumped the version number manually, create a git tag: `git tag -a v<x.y.z> -m "Add tag v<x.y.z>"` where `<x.y.z>` is the new version
1. Push the tag to Github: `git push --tags`
1. Let the pipeline package and publish the new version for you!

## Using the `Makefile`

Almost all the needed operations required to develop this project are scripted in the `Makefile` for your convenience. It is recommended that you familiarize yourself with this file and the features it provides. Below is a complete list of the available targets (operations):

| Target                    | Parameters                                                               | Description                                                                                                                                                                                              |
|---------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `help`                    |                                                                          | Prints all the available targets with a brief explanation of each of them                                                                                                                                |
| `env-create`              |                                                                          | Creates a development virtual environment using `tox` (the name is the same as the project slug)                                                                                                         |
| `env-compile`             |                                                                          | Compiles the `requirements.txt` and `requirements-dev.txt` files by pinning the dependencies found on `requirements.in`/`requirements-dev.in`                                                            |
| `env-add-package`         | `PACKAGE`: for example `requests`                                        | Adds a new package to `requirements.in`                                                                                                                                                                  |
| `env-add-dev-package`     | `PACKAGE`: for example `responses`                                       | Adds a new development package to `requirements-dev.in`                                                                                                                                                  |
| `env-upgrade-package`     | `PACKAGE`: for example `requests`                                        | Upgrades a package in `requirements.in`                                                                                                                                                                  |
| `env-upgrade-dev-package` | `PACKAGE`: for example `responses`                                       | Upgrades a development package in `requirements-dev.in`                                                                                                                                                  |
| `env-upgrade-all`         |                                                                          | Upgrades all packages in `requirements.in`/`requirements-dev.in`                                                                                                                                         |
| `install`                 |                                                                          | Installs this package using `pip` (not really required during development)                                                                                                                               |
| `uninstall`               |                                                                          | Uninstalls this package using `pip`                                                                                                                                                                      |
| `develop`                 |                                                                          | Installs this package in development mode (not really required during development)                                                                                                                       |
| `fmt`                     |                                                                          | Formats the code according to the [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/) using [black](https://pypi.org/project/black/)                                                            |
| `lint`                    |                                                                          | Lints the code using [pylint](https://www.pylint.org/)                                                                                                                                                   |
| `lint-tests`              |                                                                          | Lints the tests using [pylint](https://www.pylint.org/)                                                                                                                                                  |
| `code-style`              |                                                                          | Checks code style against [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/) using [pycodestyle](https://pypi.org/project/pycodestyle/)                                                        |
| `code-maintainability`    |                                                                          | Calculates a maintainability index using [radon](https://pypi.org/project/radon/)                                                                                                                        |
| `code-locs`               |                                                                          | Display metrics (LOCs, number of comments, etc.)                                                                                                                                                         |
| `code-complexity`         |                                                                          | Check cyclomatic complexity using [radon](https://pypi.org/project/radon/)                                                                                                                               |
| `code-metrics`            |                                                                          | Check cyclomatic complexity, print LOCs and calculate maintainability index using [radon](https://pypi.org/project/radon/)                                                                               |
| `test`                    | `REPORT_NAME`: (default `pytest`)                                        | Runs the tests and calculates code coverage. This task generates HTML and XML Junit test reports on `docs/_build/test-reports/<REPORT_NAME>` and coverage report on `docs/_build/coverage/<REPORT_NAME>` |
| `security`                | `REPORT_FORMAT`: If present, a report with this format will be generated | Runs a static security analysis on the code using [bandit](https://pypi.org/project/bandit/) and generates an HTML report (at `docs/_build/security`)                                                    |
| `check-dependencies`      |                                                                          | Checks dependencies for vulnerabilities using [safety](https://pypi.org/project/safety/)                                                                                                                 |
| `docs`                    |                                                                          | Generates package documentation using [sphinx](https://www.sphinx-doc.org/en/master/) (saved at `docs/_build/sphinx`)                                                                                    |
| `version`                 |                                                                          | Gets the current package version (found on the `__version__` variable at `{{cookiecutter.project_slug}}/_meta.py`)                                                                                       |
| `version-bump`            | `PART`: `major`, `minor` or `patch`                                      | Bumps the version part using [bump2version](https://pypi.org/project/bump2version/)                                                                                                                      |
| `version-bump-tag`        | `PART`: `major`, `minor` or `patch`                                      | Bumps and tags the version part using [bump2version](https://pypi.org/project/bump2version/)                                                                                                             |
| `version-set`             | `VERSION`: semantic version number                                       | Sets the package version to the one provided in the `VERSION` parameter                                                                                                                                  |
| `version-set-tag`         | `VERSION`: semantic version number                                       | Sets the package version to the one provided in the `VERSION` parameter and creates a tag                                                                                                                |
| `dist`                    |                                                                          | Builds a binary distribution (wheel) compiled with [cython](https://cython.org/)                                                                                                                         |
| `dist-dev`                |                                                                          | Builds a non-compiled binary distribution (wheel)                                                                                                                                                        |
| `sdist`                   |                                                                          | Builds a source code distribution                                                                                                                                                                        |
| `publish`                 |                                                                          | Publishes all wheels found on the `dist` folder to our private PyPi repository (Artifactory)                                                                                                             |
| `docker-run`              | `TARGET`: make target to run inside Docker                               | Runs the specified `TARGET` inside a Docker container (configured on `docker/dev/docker-compose.yml`). Useful if the package requires system-level dependencies.                                         |
| `docker-shell`            |                                                                          | Runs a shell inside the Docker container configured on `docker/dev/docker-compose.yml`                                                                                                                   |{%- if cookiecutter.project_type == 'application' %}
| `docker-lint`             |                                                                          | Lints the `Dockerfile` at `docker/prod` using [hadolint](https://github.com/hadolint/hadolint)                                                                                                           |
| `docker-build`            | `REVISION` (optional): current commit SHA (will be added as a `LABEL`)   | Builds the production docker image (the name will be the project slug)                                                                                                                                   |
| `docker-pull`             |                                                                          | Pulls the production docker image                                                                                                                                                                        |
| `docker-push`             |                                                                          | Pushes the production docker image                                                                                                                                                                       |
| `docker-security`         |                                                                          | Scans the production docker image for security vulnerabilities using [trivy](https://github.com/aquasecurity/trivy)                                                                                      |
| `docker-package`          |                                                                          | Packages the production docker image as a .tar archive                                                                                                                                                   |{%- endif %}
| `ci-all`                  |                                                                          | Simulate the complete CI pipeline by running all the `ci-*` targets                                                                                                                                      |
| `ci-prepare`              |                                                                          | Creates the virtual environment for every support Python version using `tox` (used on CI).                                                                                                               |
| `ci-lint`                 |                                                                          | Lints code and tests (used on CI)                                                                                                                                                                        |
| `ci-code-style`           |                                                                          | Checks code style against [PEP8 guidelines](https://www.python.org/dev/peps/pep-0008/) (used on CI). Equivalent to `make code-style`                                                                     |
| `ci-code-metrics`         |                                                                          | Check cyclomatic complexity, print LOCs and calculate maintainability index using [radon](https://pypi.org/project/radon/) (used on CI)                                                                  |
| `ci-security`             |                                                                          | Runs a static security analysis on the code using [bandit](https://pypi.org/project/bandit/) (used on CI). Equivalent to `make security-report`                                                          |
| `ci-check-dependencies`   |                                                                          | Checks dependencies for vulnerabilities using [safety](https://pypi.org/project/safety/) (used on CI)                                                                                                    |
| `ci-test`                 |                                                                          | Runs tests on every supported Python version. Equivalent to `make test-report` (used on CI). Reports are saved on `docs/_build/test_reports/py<version_number>`                                          |
| `ci-docs`                 |                                                                          | Generates package documentation using [sphinx](https://www.sphinx-doc.org/en/master/) (used on CI). Equivalent to `make docs`                                                                            |
| `ci-version-set`          | `VERSION`: semantic version number                                       | Sets the package version to the one provided in the `VERSION` parameter (used on CI)                                                                                                                     |
| `ci-dist`                 |                                                                          | Builds binary distributions (wheel) for each supported Python version (used on CI). Equivalent to `make dist`.                                                                                           |
| `ci-dist-dev`             |                                                                          | Builds development (non-binary) distributions (wheel) for each supported Python version (used on CI). Equivalent to `make dist-dev`.                                                                     |
| `ci-publish`              |                                                                          | Publishes all wheels found on the `dist` folder to our private PyPi repository (used on CI). Equivalent to `make publish`                                                                                |
| `ci-release`              |                                                                          | Builds and publishes binary distributions (wheel) for each supported Python version (used on CI). Equivalent to `make dist`.                                                                             |
| `ci-release-dev`          |                                                                          | Builds and publishes development (non-binary) distributions (wheel) for each supported Python version (used on CI). Equivalent to `make dist-dev`.                                                       |{%- if cookiecutter.project_type == 'application' %}
| `ci-release-docker`       |                                                                          | Lints, builds, publishes and scans the production docker image (used on CI)                                                                                                                              |{%- endif %}
| `clean`                   |                                                                          | Removes build, test coverage and Python artifacts                                                                                                                                                        |
| `clean-all`               |                                                                          | Removes everything (artifacts, environments and docker)                                                                                                                                                  |
| `clean-docs`              |                                                                          | Removes built documentation (`docs/_build)`)                                                                                                                                                             |
| `clean-build`             |                                                                          | Removes build artifacts                                                                                                                                                                                  |
| `clean-dist`              |                                                                          | Removes package builds found on `dist/`                                                                                                                                                                  |
| `clean-pyc`               |                                                                          | Removes python cache artifacts                                                                                                                                                                           |
| `clean-test`              |                                                                          | Removes pytest and coverage artifacts                                                                                                                                                                    |
| `clean-env`               |                                                                          | Removes tox virtual environments (`.tox`)                                                                                                                                                                |{%- if cookiecutter.project_type == 'application' %}
| `clean-docker`            |                                                                          | Removes docker containers, networks, etc.                                                                                                                                                                |{%- endif %}