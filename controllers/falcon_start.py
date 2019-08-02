import falcon
from falcon import Request, Response

class HelloWorld():

    def on_get(self, req, resp):
        """Hello world
        ---
        description: Get a greeting to the world
        tags:
        - Test
        responses:
            200:
                description: Greeting to the world
                content:
                    application/json:
                        schema:
                            type: string
        """
        doc = {'message': 'Hello world'}
        resp.media = doc
        resp.status = falcon.HTTP_OK

class HelloUser():

    def on_get(self, req, resp, name):
        """Hello world
        ---
        description: Get a greeting to a user
        parameters:
        - name: name
          in: path
          description: name of user to greet
          schema:
            type: string
          required: true
        tags:
        - Test
        responses:
            200:
                description: Greeting to a user
                content:
                    application/json:
                        schema:
                            type: string
        """

        doc = {'message': 'Hello '+name}
        resp.media = doc
        resp.status = falcon.HTTP_OK

