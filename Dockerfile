FROM python:3.9.7-slim

RUN apt-get update \
    && apt-get install -y \
        wget \
        unzip \
        libgl1-mesa-glx \
        libglu1-mesa \
        libgomp1 \
        libglib2.0-0

COPY . neuromaps

RUN cd neuromaps \
    && python3 -m pip install '.[nulls]'

RUN while true; do \
        wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 --no-dns-cache -c \
            https://www.humanconnectome.org/storage/app/media/workbench/workbench-linux64-v1.5.0.zip \
        && unzip workbench-linux64-v1.5.0.zip -d "/" \
        && break; \
    done

ENV PATH="/workbench/bin_linux64:$PATH"

CMD python3
