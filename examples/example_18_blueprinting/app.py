"""Example 18: blueprinting."""
from flask import Flask
from examples.example_18_blueprinting.posts import posts
from examples.example_18_blueprinting.users import users

app = Flask(__name__)


# All endpoints from posts Blueprint will be prefixed with /posts
app.register_blueprint(posts, url_prefix="/posts")

# All endpoints from users Blueprint will be prefixed with users
app.register_blueprint(users, url_prefix="/users")

if __name__ == '__main__':
    app.run()
