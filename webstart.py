"""
URL routing & initialization for webapp
"""

from os.path import join
from main import app
from flask import send_from_directory, Blueprint, send_file


print "Starting webapp!"


from floorplan.views import floorplan
app.register_blueprint(floorplan, url_prefix='/floorplan')

#user
from user.views import user
app.register_blueprint(user, url_prefix='/user')

# splash
from splash.views import splash
app.register_blueprint(splash)


# modules manage their own static files. This serves them all up.
@app.route("/<blueprint_name>/static/<path:fn>")
def _return_static(blueprint_name, fn='index.html'):
    path = join(*app.blueprints[blueprint_name].import_name.split('.')[:-1]) 
    return send_file('%s/static/%s' % (path, fn)) 

if __name__ == '__main__':
    app.run(debug=True)