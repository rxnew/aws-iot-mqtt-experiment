FROM ubuntu:18.04

ARG install_dir=/opt/app

RUN apt-get -y update \
    && apt-get -y install python3-apt python3-pip iproute2 iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade pip \
    && pip3 install pipenv

WORKDIR /tmp/app

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

COPY Pipfile Pipfile.lock /tmp/app/
RUN pipenv install --system --deploy \
    && rm -rf /tmp/app

COPY mqtt_test ${install_dir}/mqtt_test

WORKDIR ${install_dir}

ENTRYPOINT ["python3", "-m", "mqtt_test"]
