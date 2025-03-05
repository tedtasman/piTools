from pymavlink import mavutil
import sys

# Create the connection
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for the heartbeat msg to find the system ID
print('Waiting for heartbeat')
master.wait_heartbeat()
print('Heartbeat from system (system %u component %u)' % (master.target_system, master.target_component))

# Request data
master.mav.request_data_stream_send(
    master.target_system, master.target_component,
    mavutil.mavlink.MAV_DATA_STREAM_ALL, 1, 1)

# Get some information !
while True:
    try:
        msg = master.recv_match()
    except Exception as e:
        print(e)
        continue

    if not msg:
        continue

    if msg.get_type() == 'BAD_DATA':
        if mavutil.all_printable(msg.data):
            sys.stdout.write(msg.data)
            sys.stdout.flush()
    else:
        print(msg)

