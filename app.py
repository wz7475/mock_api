from flask import Flask

import routes

app = Flask(__name__)


app.add_url_rule("/1", view_func=routes.hello_world)
app.add_url_rule("/json/<line_id>", view_func=routes.load_json)



if __name__ == '__main__':
    app.run(debug=True)