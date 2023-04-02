import asyncio
from mavsdk import System


async def run():

    
    
    drone = System(mavsdk_server_address='127.0.0.1')
    await drone.connect()
    
    status_text_task = asyncio.ensure_future(print_status_text(drone))
    
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Arming")
    await drone.action.arm()
    print('armed')

async def print_status_text(drone):
    
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return



if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())