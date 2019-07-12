#!/usr/bin/env python2
# designed for use with boofuzz
#
# minimal example which act as a TLS server
# it will listen on localhost and fuzz the connecting TLS client

from boofuzz import *
import ssl

# create test certificate with
# openssl req -x509 -newkey rsa -keyout key.pem -out cert.pem -days 365 -nodes
ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ctx.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

session = Session(
    target=Target(
        connection=SocketConnection(
            host="127.0.0.1",
            port=443,
            proto='ssl',
            sslcontext=ctx,
            server=True,
            ),
    ),
)
s_initialize("A")
s_string("A")
session.connect(session.root, s_get("A"))
session.fuzz()
