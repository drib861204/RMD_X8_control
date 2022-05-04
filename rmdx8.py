import can


class RmdX8:
    def __init__(self):
        self.RMD_X8_SPEED_LIMITED = 514
        self.SET_TORQUE_CMD = "ST"
        self.m_rmd_x8_position = 0
        self.m_motor_torque = 0

    def rmd_read(self, cmd, data):
        if cmd == self.SET_TORQUE_CMD:
            print("Set torque for motor run")
            self.m_motor_torque = data  # data = torque(Nm)
            data_out = [0xA1, 0x00, 0x00, 0x00, hex(data & 0xFF), hex(data >> 8), 0x00, 0x00]
            send_one(data_out)


def send_one(data=None):
    if data is None:
        data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    with can.interface.Bus() as bus:
        msg = can.Message(
            arbitration_id=0x141, data=data, is_extended_id=False
        )

        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")
