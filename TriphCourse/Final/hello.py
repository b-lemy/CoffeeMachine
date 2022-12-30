from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/about/<name>')
def about(name):
    return f'Hello there {name}'

# Creating variable path and changing to a specified data type
@app.route('/setting/<path:sort>')
def setting(sort):
    return f'Hello there {sort}'


if __name__ == "__main__":
    # Run the debug mode into auto reload
    app.run(debug=True)
