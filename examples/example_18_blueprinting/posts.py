"""Part of the aplication displaying posts."""
from flask import Blueprint, render_template


posts = Blueprint("posts", __name__)

POSTS = [
    {"title": "My first post", "content": "This is my first post."},
    {"title": "Second posts", "content": "This is second post."},
    {
        "title": "Lipsum",
        "content": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas id ex pharetra, faucibus libero at, condimentum justo. 
        Proin hendrerit, elit nec facilisis mattis, mauris massa facilisis diam, vitae laoreet ex massa ut metus. 
        Vivamus congue, dolor eu sagittis tristique, tortor lectus fermentfffum enim, in tempor nisl risus a ex. 
        Duis aliquam turpis sed lectus egestas euismod quis vitae ligula. 
        Sed dictum enim feugiat consequat malesuada. 
        Morbi quis ullamcorper odio, in ultrices purus. 
        Integer vulputate quam non bibendum suscipit. 
        Vestibulum et leo laoreet diam bibendum eleifend.
        """
    }
]


# This will be available at <prefix>/, where prefix is chosen when registering
# the blueprint.
@posts.route("/all")
def all_posts():
    return render_template("posts.jinja2", posts=POSTS)
