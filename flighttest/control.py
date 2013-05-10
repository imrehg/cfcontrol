
import cflib.crtp
import cflib.crazyflie
import time

cf = cflib.crtp.init_drivers()
available = cflib.crtp.scan_interfaces()
# for i in available:
#     print "Found Crazyflie on URI [%s] with comment [%s]" % (available[0], available[1])
print available

cf = cflib.crazyflie.Crazyflie()
cf.open_link("radio://0/9/250K")
cm = cflib.crazyflie.Commander(cf)


# print cm.send_setpoint(0, 0, 0, 30)
# time.sleep(1)
# print cm.send_setpoint(0, 0, 0, 0)

cf.close_link()
