import falcon.testing as testing

from controllers.falcon_start import *


def test_hello():

    app = falcon.API()
    app.add_route('/hello', HelloWorld())
    client = testing.TestClient(app)

    response = client.simulate_request(path='/hello', method='GET')
    assert response.status == falcon.HTTP_200
    assert response.json == {'message': 'Hello world'}

def test_hello_user():

    app = falcon.API()
    app.add_route('/hello/{name}', HelloUser())
    client = testing.TestClient(app)
# this is a test comment
    response = client.simulate_request(path='/hello/world', method='GET')
    assert response.status == falcon.HTTP_200
    assert response.json == {'message': 'Hello worldd'}
