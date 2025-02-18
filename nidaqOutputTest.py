import nidaqmx

ni9474_channel = "Dev1/port0/line0:6"

def initialize_ni9474():
    with nidaqmx.Task() as task:
        task.do_channels.add_do_chan(ni9474_channel)
        task.write([0,0,0,0,0,0,0])  # Set all outputs to False
        print("NI-9474 initialized. All outputs set to False.")

def test_sequence():
    with nidaqmx.Task() as task:
        task.do_channels.add_do_chan(ni9474_channel)
        task.write([0,1,1,0,0,0,0])
        print("Fuel injection complete")
        task.write([1,0,0,1,0,0,0])
        print("Driver injection complete")
        

