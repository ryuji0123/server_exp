FROM ubuntu/nginx

# apt-get
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && \
    apt-get install -y curl dnsutils iputils-ping lsof net-tools python3-pip sudo tmux tree vim wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/apk/*

# python
COPY ./src/requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt