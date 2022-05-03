FROM python:3.9.7-slim

ENV RELEASE=https://api.github.com/repos/netneurolab/neuromaps/releases/latest

RUN apt-get update && apt-get install -y curl jq

RUN curl -L $( curl -Ls ${RELEASE} | jq -r '.tarball_url' ) > tmp.tar.gz \
    && tar xzvf tmp.tar.gz \
    && rm tmp.tar.gz \
    && cd $( find . -type d -name "netneurolab-neuromaps-*" ) \
    && python -m pip install .

ENTRYPOINT [ "python3" ]
