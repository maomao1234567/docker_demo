#  使用Docker 对python Sanic应用的自动化打包与部署



## Docker的介绍

Docker 是一个开源的应用容器引擎，基于 [Go 语言](http://www.runoob.com/go/go-tutorial.html) 并遵从Apache2.0协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

---

## Sanic的介绍

Sanic是一个类似Flask的Python 3.5+ Web服务器，它的写入速度非常快。除了Flask之外，Sanic还支持异步请求处理程序。这意味着你可以使用Python 3.5中新的闪亮的异步/等待语法，使你的代码非阻塞和快速。



## 先使用sanic编写代码

**这里这是一个简单的演示应用就只写一个简单处理函数返回"Hello Sanic"及可**

app.py

```python
from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "sanic"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

 manage.py

```python
from app import app


app.run(host="0.0.0.0", port=5000)

```

---



## 使用docker对项目进行打包与部署

**编写Dockerfile**

Dockerfile

```SAS
FROM Python:3.6

COPY src/ /opt/app
WORKDIR /opt/app

RUN curl -s http://ip-api.com | grep China > /dev/null && \
    pip install -i https://pypi.doubanio.com/simple --trusted-host pypi.doubanio.com sanic

EXPOSE 5000

CMD sleep 999999999
```



**使用Dockerfile构建这个项目的镜像**

```shell
docker build .
```

---

**使用刚才创建的镜像创建并运行容器**

```shell
docker run -p 5000:5000 image
```

---

**进入容器并运行sanic**

