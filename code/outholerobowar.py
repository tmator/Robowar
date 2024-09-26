"""Outhole Support for Robowar"""

from mpf.core.custom_code import CustomCode


class OutholeRobowar(CustomCode):

    def on_load(self):

        self.auto_release_in_progress = False

        #si la bille est présente sur le switc outhole, on appelle eject_ball
        self.machine.switch_controller.add_switch_handler('s_outhole', self.eject_ball, ms=100)


    def eject_ball(self):

        #self.machine.coils['c_relay_s'].enable(pulse_ms=00)
        #self.machine.coils['c_3'].enable(=20)

        #self.machine.coils['c_3'].disable()
        #self.machine.coils['c_relay_s'].disable()

        self.machine.lights['l_4x'].on()