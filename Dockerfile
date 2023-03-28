FROM rabbitmq:3.9.10-management

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install rabbitmq-admin

ENTRYPOINT ["rabbitmqadmin"]
CMD ["--help"]
