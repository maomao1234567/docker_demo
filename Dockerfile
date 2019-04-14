FROM python:3.6

COPY src/ /opt/app
WORKDIR /opt/app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sanic

EXPOSE 5000

CMD sleep 999999999