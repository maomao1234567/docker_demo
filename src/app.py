from sanic import Sanic
from sanic.response import html

app = Sanic()

@app.route("/")
async def test(request):
    return html("<h1>Hello Sanic!</h1>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
