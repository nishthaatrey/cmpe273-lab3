from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedUDP(DatagramProtocol):

    def datagramReceived(self, data, host):
        print("received %r from %s" % (data, host))
        self.transport.write(data, host)

reactor.listenUDP(8888, ConnectedUDP())
reactor.run()