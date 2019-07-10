
import falcon
import falcon.testing as testing

import falcon_start as fa

#
# def test_hello():
#
#     app = falcon.API()
#     app.add_route('/hello', fa.HelloWorld())
#     client = testing.TestClient(app)
#
#     response = client.simulate_request(path='/hello', method='GET')
#     assert response.status == falcon.HTTP_200
#     assert response.json == {'message': 'Hello world'}
#
# def test_hello_user():
#
#     app = falcon.API()
#     app.add_route('/hello/{name}', fa.HelloUser())
#     client = testing.TestClient(app)
# # this is a test comment
#     response = client.simulate_request(path='/hello/sray', method='GET')
#     assert response.status == falcon.HTTP_200
#     assert response.json == {'message': 'Hello srayy'}