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
    passive_ports = getenv("FTP_DATA_PORTS").split("-")
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(int(passive_ports[0]), int(passive_ports[1]) + 1)

    server = FTPServer((getenv("FTP_IP_ADDRESS"), getenv("FTP_CMD_PORT")), handler)
    server.serve_forever()


setUpFtpServer()
