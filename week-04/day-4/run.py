from server import server

from dashapp1 import app as app1
from dashapp2 import app as app2


if __name__ == '__main__':
    server.run(debug=True)