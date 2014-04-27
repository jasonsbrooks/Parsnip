"""
URL routing & initialization for webapp
"""

from os.path import join
from main import app
from flask import send_from_directory, Blueprint, send_file


print "Starting webapp!"

# floorplan sub-app
from floorplan.views import floorplan
app.register_blueprint(floorplan, url_prefix='/floorplan')

# user sub-app
from user.views import user
app.register_blueprint(user, url_prefix='/user')

# beacon sub-app
from beacon.views import beacon
app.register_blueprint(beacon, url_prefix='/beacon')

# company sub-app
from company.views import company
app.register_blueprint(company, url_prefix='/company')

# advertisements sub-app
from advertisement.views import advertisement
app.register_blueprint(advertisement, url_prefix='/advertisement')

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