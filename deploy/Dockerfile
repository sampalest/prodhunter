FROM centos/python-38-centos7
USER root

# Volumes for:
#   - configuration
VOLUME ["/app/config"]

# Install pipenv
RUN pip install pipenv
WORKDIR /app
COPY Pipfile* VERSION ./
RUN pipenv install --system

COPY deploy/start.sh /
COPY src/ app/
