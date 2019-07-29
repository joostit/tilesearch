from bluepy.btle import Scanner, DefaultDelegate

import AudioIndicator

#import bluetooth
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            devName = dev.getValueText(0x09)


            #if "d6:76:fc:76:70:aa" in dev.addr:
            if "Tile" == devName:
                print("RX Tile: ", dev.addr, "   RSSi: ", dev.rssi, "dB ")
                #print("  rssi: ", dev.rssi)
                #print("  getValueText: ", dev.getValueText(0x09))
                #print("  getScanData: ", dev.getScanData())
                #print("")
           # else:
                #print("Discovered other device", dev.addr)
                #print("  rssi: ", dev.rssi)
                #print("  getValueText: ", dev.getValueText(0x09))

        #elif isNewData:
            #print("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
#devices = scanner.scan(10.0)

while True is True:
    scanner.clear()
    scanner.start()
    scanner.process(2)
    scanner.clear()
    scanner.stop()

