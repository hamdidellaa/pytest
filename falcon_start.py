import falcon
from falcon import Request, Response



class HelloWorld():
    require_authentication = False

    def on_get(self, req: Request, resp: Response):
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
    require_authentication = False

    def on_get(self, req: Request, resp: Response, name: str):
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

        doc = {'message': f'Hello {name}'}
        resp.media = doc
        resp.status = falcon.HTTP_OK
