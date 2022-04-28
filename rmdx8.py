import can

class Rmdx8:
    def __init__(self):

        self.RMD_X8_SPEED_LIMITED = 514

        #self.SET_SPEED_CMD = "SP"
        self.CLOCKWISE_CMD = "TL"
        self.COUNTER_CLOCKWISE_CMD = "TR"
        self.READ_MULTI_TURN_ANGLE_CMD = "MT"

        self.READ_SPEED_CMD = "RP"
        self.READ_ENCODER_CMD = "RE"
        self.READ_TEMP_CMD = "RT"

        self.READ_ANGLE_KP_CMD = "AP"
        self.READ_ANGLE_KI_CMD = "AI"
        self.READ_SPEED_KP_CMD = "VP"
        self.READ_SPEED_KI_CMD = "VI"
        self.READ_TORQUE_KP_CMD = "TP"
        self.READ_TORQUE_KI_CMD = "TI"

        self.m_rmd_x8_position = 0
        #self.m_uart_data_receive = ""
        self.m_uart_cmd = ""
        self.m_uart_data = 0
        #self.m_uart_string_complete = False
        #self.m_float_data_value = 0
        self.m_motor_speed = 10

        self.m_get_angle_kp = False
        self.m_get_angle_ki = False
        self.m_get_speed_kp = False
        self.m_get_speed_ki = False
        self.m_get_torque_kp = False
        self.m_get_torque_ki = False

        self.m_get_speed = False
        self.m_get_encoder = False
        self.m_get_temp = False



    def rmd_read(self, cmd, data):
        #self.m_uart_cmd = cmd
        #self.m_uart_data = data

        if cmd == self.CLOCKWISE_CMD:
            print("Set motor run clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
        elif cmd == self.COUNTER_CLOCKWISE_CMD:
            print("Set motor run counter clockwise")
















