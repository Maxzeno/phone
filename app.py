from application import *
from application.models import *

app = create_app()

# flask_sqlalchemy wont work without this part.
app.app_context().push()


if __name__ == '__main__':
    app.run() #debug=True
