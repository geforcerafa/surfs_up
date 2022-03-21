# Import dependenies
from flask import Flask

# create a new Flask instance called
app = Flask(__name__)

# define the starting point, also known as the root
@app.route('/')
def hello_world():
    return 'Hello world'