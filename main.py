import falcon

from controllers import falcon_start as fa

api = falcon.API()
api.add_route('/hello', fa.HelloWorld())
api.add_route('/hello/{name}', fa.HelloUser())