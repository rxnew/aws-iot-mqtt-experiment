FROM ubuntu:18.04

ARG install_dir=/opt/app

RUN apt-get -y update \
    && apt-get -y install python3.7 python3.7-distutils curl iproute2 iputils-ping \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3.7 get-pip.py \
    && rm -rf get-pip.py \
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

ENTRYPOINT ["python3.7", "-m", "mqtt_test"]
