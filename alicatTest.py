import asyncio
from alicat import FlowController

# Single serial port for all Alicat flow controllers
flowcontroller_port = "COM3"  # Adjust this for the actual port

# Flow controller addresses A, B, C, and D
flowcontroller_addresses = ["A", "B", "C", "D"]

async def get():
    """Initialize and read all flow controllers at their default settings, ensuring they are connected."""
    controllers = {}
    
    try:
        async with FlowController(flowcontroller_port) as MFC:
            for addr in flowcontroller_addresses:
                controllers[addr] = MFC
                print(f"Flow Controller {addr} connected on {flowcontroller_port}")
            
            readings = await MFC.get()
            print("Initial readings:", readings)
            return controllers
    except Exception as e:
        print(f"Error connecting to flow controllers: {e}")
        return None

async def set(controllers, settings):
    """Set the flow controllers based on provided settings from an external source."""
    if controllers is None:
        print("Failed to initialize flow controllers.")
        return
    
    for addr in flowcontroller_addresses:
        try:
            await controllers[addr].set_gas(settings[addr]["gas"])
            await controllers[addr].set_flow_rate(settings[addr]["setpoint"])
            print(f"Flow Controller {addr} set to {settings[addr]['setpoint']} {settings[addr]['unit']} of {settings[addr]['gas']}")
        except Exception as e:
            print(f"Error setting parameters for flow controller {addr}: {e}")

# Mock function to simulate getting values from a GUI
async def get_gui_settings():
    return {
        "A": {"gas": "C2H2", "setpoint": 6.0, "unit": "SLPM"},
        "B": {"gas": "H2", "setpoint": 12.0, "unit": "SLPM"},
        "C": {"gas": "O2", "setpoint": 8.5, "unit": "SLPM"},
        "D": {"gas": "N2", "setpoint": 10.0, "unit": "SLPM"}
    }

async def main():
    controllers = await get()
    settings = await get_gui_settings()
    await set(controllers, settings)

asyncio.run(main())
