<div align="center">

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[Contributing Guidelines](./CONTRIBUTING.md) · [Request a Feature]({{ cookiecutter.project_url }}/-/issues/new?issuable_template=Feature) · [Report a Bug]({{ cookiecutter.project_url }}/-/issues/new?issuable_template=Bug)

</div>

## Usage

{%- if cookiecutter.project_type == 'application' %}

You can install this package using [pip](https://pip.pypa.io/en/stable/):

```
$ pip install {{ cookiecutter.project_slug }}
```

You can now import this module on your Python project:

```python
import {{ cookiecutter.project_slug }}
```
{%- else %}

This application is released as a Docker image. You can run it with:

```
$ docker run -it registry.gitlab.com/{{ cookiecutter.project_url.lstrip("https://gitlab.com/") }}:{{ cookiecutter.version }}
```
{%- endif %}

## Development

To start developing this project, clone this repo and do:

```
$ make env-create
```

This will create a virtual environment with all the needed dependencies (using [tox](https://tox.readthedocs.io/en/latest/)). You can activate this environment with:

```
$ source ./.tox/{{cookiecutter.project_slug}}/bin/activate
```

Then, you can run `make help` to learn more about the different tasks you can perform on this project using [make](https://www.gnu.org/software/make/).

## License

[Copyright](./LICENSE)