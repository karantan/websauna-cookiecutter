from websauna.system.http import Request
from websauna.system.core.route import simple_route


# Configure view named home at path / using a template {{cookiecutter.pkg_name}}/home.html
@simple_route("/", route_name="home", renderer='{{cookiecutter.pkg_name}}/home.html')
def home(request: Request):
    """Render site homepage."""
    return {"project": "{{cookiecutter.pkg_name}}"}
