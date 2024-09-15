import spiderweb
from spiderweb.response import HttpResponse
from spiderweb.decorators import csrf_exempt

from mydb.models import Item


app = spiderweb.SpiderwebRouter(
    middleware=[
        "spiderweb.middleware.sessions.SessionMiddleware",
        "spiderweb.middleware.csrf.CSRFMiddleware",
    ]
)


@app.route("/")
def index(request):
    item_count = Item.objects.count()

    resp = "This is an example of Spiderweb with the Django ORM!<br>"
    resp += "There are <b>{} items</b> in the database.<br>".format(item_count)
    resp += "<br><a href='/items'>View items</a>"
    resp += "<br><a href='/add_item'>Add item</a>"

    return HttpResponse(resp)

@app.route("/items")
def items(request):
    items = Item.objects.all()

    resp = "Items:<br><ul>"
    for item in items:
        resp += "<li>{}: ${}</li>".format(item.name, item.price)
    resp += "</ul>"
    resp += "<br><a href='/'>Back to index</a>"
    resp += "<br><a href='/add_item'>Add item</a>"

    return HttpResponse(resp)


@app.route("/add_item", allowed_methods=["GET", "POST"])
@csrf_exempt
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")

        Item.objects.create(name=name, price=price)

        return HttpResponse("Item added!<br><br><a href='/'>Back to index</a>")

    else:
        return HttpResponse(
            """
            <form method="post">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br>
                <label for="price">Price:</label><br>
                <input type="text" id="price" name="price"><br>
                <input type="submit" value="Submit">
            </form>
            """
        )


if __name__ == "__main__":
    app.start()
