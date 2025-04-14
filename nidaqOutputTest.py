import time
import nidaqmx
from nidaqmx.constants import LineGrouping


ni9474_channel = "cDAQ9188-169338EMod1/port0/line0:7"

def zeroDigitalOutputs():
    with nidaqmx.Task() as task:
        task.do_channels.add_do_chan(ni9474_channel, line_grouping=LineGrouping.CHAN_PER_LINE)
        task.write([False]*8)  # Set all outputs to False
        print("NI-9474 initialized. All outputs set to False.")
        task.stop()

def test_sequence(digitalOuts):
    with nidaqmx.Task() as task:
        task.do_channels.add_do_chan(ni9474_channel, line_grouping=LineGrouping.CHAN_PER_LINE)
        input("Press enter to start...")
        task.write(digitalOuts)
        print("ON")
        time.sleep(3)
        task.write([False]*8)
        print("OFF")
        input("Press enter to close...")
        task.stop()
        
zeroDigitalOutputs()
test_sequence([True, False, False, False, False, False, False, False])
