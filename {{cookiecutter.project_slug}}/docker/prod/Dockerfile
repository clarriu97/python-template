{% set python_target_cp_version = 'cp' + cookiecutter.python_target_version.replace('.','') -%}
{% set python_apt_version = {"3.8": "3.8.15-1+focal3  ", "3.9": "3.9.13-1+focal3  "}[cookiecutter.python_target_version] | default("") -%}
# Build stage: install pip dependencies
FROM ubuntu:20.04 AS builder

ARG VERSION
ARG PIP_EXTRA_INDEX_URL

WORKDIR /home/python-dev

# Install pip for the desired python version
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
  python{{ cookiecutter.python_target_version }} get-pip.py && \
  python{{ cookiecutter.python_target_version }} -m pip install --upgrade pip==21.1.1

# Install dependencies and application
COPY requirements.txt .
COPY dist/{{ cookiecutter.project_slug }}-${VERSION}-{{ python_target_cp_version }}-{{ python_target_cp_version }}m-*.whl /home/python-dev
RUN python{{ cookiecutter.python_target_version }} -m pip --no-cache-dir install --user --upgrade --ignore-installed --extra-index-url "${PIP_EXTRA_INDEX_URL}" -r ./requirements.txt
RUN python{{ cookiecutter.python_target_version }} -m pip --no-cache-dir install --user --upgrade --ignore-installed --no-index --no-deps --find-links /home/python-dev {{ cookiecutter.project_slug }}==${VERSION}

# Final stage: install python and copy dependencies from build stage
FROM ubuntu:20.04

ARG BUILD_DATE
ARG VERSION
ARG REVISION

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install Python
WORKDIR /usr/local/bin
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common=0.99.9.8 && \
  add-apt-repository ppa:deadsnakes/ppa && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
  python{{ cookiecutter.python_target_version }}{% if python_apt_version != '' %}={{ python_apt_version }}{%endif%} && \
  apt-get clean && \
  update-alternatives --install /usr/bin/python3 python3 /usr/bin/python{{ cookiecutter.python_target_version }} 1 && \
  rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Get all the Python packages installed on the previous stage
COPY --from=builder /home/python-dev/.local/lib/python{{ cookiecutter.python_target_version }}/site-packages /usr/local/lib/python{{ cookiecutter.python_target_version }}/dist-packages
COPY --from=builder /home/python-dev/.local/bin/* /usr/local/bin/

# Create a non-root user to run the container. This step is optional, you can also use any existing user such as `www-data` for web servers (nginx for example)
RUN groupadd -g 1000 {{ cookiecutter.project_slug }} && useradd -ms /bin/bash -u 1000 -g 1000 {{ cookiecutter.project_slug }}

# Image labels (OCI spec)
LABEL org.opencontainers.image.created="${BUILD_DATE}" \
    org.opencontainers.image.authors='{{ cookiecutter.author }} <{{ cookiecutter.author_email }}>' \
    org.opencontainers.image.url='{{ cookiecutter.project_url }}' \
    org.opencontainers.image.documentation='{{ cookiecutter.project_url }}' \
    org.opencontainers.image.source='{{ cookiecutter.project_url }}' \
    org.opencontainers.image.version="${VERSION}" \
    org.opencontainers.image.revision="${REVISION}" \
    org.opencontainers.image.vendor='{{ cookiecutter.company_name }}' \
    org.opencontainers.image.title='{{ cookiecutter.project_slug }}' \
    org.opencontainers.image.description='{{ cookiecutter.project_short_description }}' \
    org.opencontainers.image.licenses="COPYRIGHT"

USER {{ cookiecutter.project_slug }}

# Add your code here! This is just an example:
CMD ["python3", "-c", "import {{ cookiecutter.project_slug }} as m ; print(f\"{m.__title__} (v{m.__version__})\")"]
