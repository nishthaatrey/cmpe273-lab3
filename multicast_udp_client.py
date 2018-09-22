from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastPingClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:8005 - all listeners on the multicast address
        # (including us) will receive this message.
        msg="Client: Ping"
        self.transport.write(msg.encode("utf-8"), ("228.0.0.5", 8888))

    def datagramReceived(self, datagram, address):
        print ("Datagram %s received from %s" % (repr(datagram.decode("utf-8")), repr(address)))


reactor.listenMulticast(8888, MulticastPingClient(), listenMultiple=True)
reactor.run()