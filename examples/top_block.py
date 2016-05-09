#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun May  8 23:57:21 2016
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import llsr
import pmt
import sys

from distutils.version import StrictVersion
class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.llsr_llsr_mac_1 = llsr.llsr_mac(
              0,
              0.01,
              5,
              2.0,
              True,
              0.05,
              10.0,
              10,
              False,
              True)
          
        self.llsr_llsr_mac_0 = llsr.llsr_mac(
              1,
              0.01,
              5,
              2.0,
              True,
              0.05,
              10.0,
              10,
              False,
              False)
          
        self.blocks_random_pdu_0 = blocks.random_pdu(5, 5, chr(0xFF), 2)
        self.blocks_message_strobe_3 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_strobe_2 = blocks.message_strobe(pmt.intern("TEST"), 20000)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 10000)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.blocks_message_strobe_0, "strobe", self.llsr_llsr_mac_0, "ctrl_in")
        self.msg_connect(self.blocks_message_strobe_2, "strobe", self.blocks_random_pdu_0, "generate")
        self.msg_connect(self.blocks_message_strobe_3, "strobe", self.llsr_llsr_mac_1, "ctrl_in")
        self.msg_connect(self.blocks_random_pdu_0, "pdus", self.llsr_llsr_mac_0, "from_app_arq")
        self.msg_connect(self.llsr_llsr_mac_0, "to_radio", self.llsr_llsr_mac_1, "from_radio")
        self.msg_connect(self.llsr_llsr_mac_1, "to_app", self.blocks_message_debug_0, "print_pdu")
        self.msg_connect(self.llsr_llsr_mac_1, "to_radio", self.llsr_llsr_mac_0, "from_radio")

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
