# Spiderweb + Django ORM

While playing around with [Spiderweb, my tiny web framework](https://github.com/itsthejoker/spiderweb), it seemed like a funny idea to try and run it using the Django ORM, which is my personal favorite and also kind of the best in the biz.

This repo is unmaintained, provided without support, and is just an example of what this integration might look like. To give it a try:

* Clone the repo in the way that works best for you
* run `poetry install`
* run `poetry shell`
* run `python main.py` to start the server.

If you make any changes to the models, you will need to run:

* `python manage.py makemigrations`
* `python manage.py migrate`

...and then start the server again.