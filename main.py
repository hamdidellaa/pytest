import falcon

from controllers import falcon_start as fa

print("della is here")
api = falcon.API()
api.add_route('/hello', fa.HelloWorld())
api.add_route('/hello/{name}', fa.HelloUser())