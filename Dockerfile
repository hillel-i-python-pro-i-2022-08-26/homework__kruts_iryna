FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./core core
COPY --chown=${USER} ./main.py main.py
COPY --chown=${USER} ./Makefile Makefile

USER ${USER}

ENTRYPOINT ["python", "main.py"]
