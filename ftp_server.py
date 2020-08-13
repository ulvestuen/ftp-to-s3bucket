from os import getcwd, getenv

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def setUpFtpServer():
    authorizer = DummyAuthorizer()
    authorizer.add_user(getenv("FTP_USERNAME"),
                        getenv("FTP_PASSWORD"),
                        getcwd() + "/files",
                        perm="ldfwT")

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 65535 + 1)

    server = FTPServer((getenv("FTP_IP_ADDRESS"), getenv("FTP_PORT")), handler)
    server.serve_forever()


setUpFtpServer()
