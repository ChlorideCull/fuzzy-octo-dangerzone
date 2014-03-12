from bottle import Bottle, run, request
class FakeAPI (object):
    def __init__(self, callback_function):
        app = Bottle()

        @app.post("/xmlrpc.php")
        def _xmlrpcapi():
            print("post")
            for x in request.forms:
                print(x, end="")
                print(" = " + str(request.forms[x]))
            return 1

        @app.get("/xmlrpc.php")
        def _default():
            return "ey nigga get outta here"

        app.run(host="0.0.0.0", port=80)

if __name__ == "__main__":
    p = FakeAPI(None)
