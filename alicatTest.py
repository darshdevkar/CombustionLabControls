import asyncio
from alicat import FlowController
import time

# Single serial port for all Alicat flow controllers
flowcontroller_port = "COM3"  # Adjust this for the actual port

# Flow controller addresses A, B, C, and D
flowcontroller_addresses = ["A", "B", "C"]

async def get():
    """Initialize and read all flow controllers at their default settings, ensuring they are connected."""
    try:
        for addr in flowcontroller_addresses:
          async with FlowController(address=flowcontroller_port, unit=addr) as MFC:
              print(f"Flow Controller {addr} connected on {flowcontroller_port}")
              print("Initial readings:", await MFC.get())
    except Exception as e:
        print(f"Error connecting to flow controllers: {e}")

async def set(settings):
    """Set the flow controllers based on provided settings from an external source."""
    try:
        for addr in flowcontroller_addresses:
          if addr == "B":
            async with FlowController(address=flowcontroller_port, unit="B") as MFC:
              if MFC is None:
                print("Error setting fowrate: controller not found")
              else:
                await MFC.set_flow_rate(settings["B"]["setpoint"])
                time.sleep(5)
                await MFC.set_flow_rate(0.0)
    except Exception as e:
        print(f"Error setting flowrate of 'B': {e}")
    '''
    for addr in flowcontroller_addresses:
        try:
            await controllers[addr].set_gas(settings[addr]["gas"])
            await controllers[addr].set_flow_rate(settings[addr]["setpoint"])
            print(f"Flow Controller {addr} set to {settings[addr]['setpoint']} {settings[addr]['unit']} of {settings[addr]['gas']}")
        except Exception as e:
            print(f"Error setting parameters for flow controller {addr}: {e}")
    '''
# Mock function to simulate getting values from a GUI
async def get_gui_settings():
    return {
        "A": {"gas": "H2", "setpoint": 0.0, "unit": "SLPM"},
        "B": {"gas": "N2", "setpoint": 1.0, "unit": "SLPM"},
        "C": {"gas": "O2", "setpoint": 0.0, "unit": "SLPM"}
    }

async def main():
    await get()
    settings = await get_gui_settings()
    time.sleep(3)
    print("setting...")
    await set(settings)
    input("Press Enter to close...")

asyncio.run(main())
