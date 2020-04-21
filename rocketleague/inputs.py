import keyboard
import time
from win32gui import GetWindowText, GetForegroundWindow
import config
import utils
from .enums import Controls

logger = utils.get_logger()

control_to_key_config = {
    Controls.DRIVE_FORWARD:   config.DRIVE_FORWARD,
    Controls.DRIVE_BACKWARDS: config.DRIVE_BACKWARDS,
    Controls.STEER_RIGHT:     config.STEER_RIGHT,
    Controls.STEER_LEFT:      config.STEER_LEFT,
    Controls.JUMP:            config.JUMP,
    Controls.BOOST:           config.BOOST,
    Controls.POWERSLIDE:      config.POWERSLIDE,
    Controls.AIRROLL:         config.AIRROLL,
    Controls.FOCUS_ON_BALL:   config.FOCUS_ON_BALL,
    Controls.REAR_VIEW:       config.REAR_VIEW,
    Controls.USE_ITEM:        config.USE_ITEM,
}

def do_control(control):
    if not rl_active():
        logger.warn("Rocket League is not active. Skipping.")
        return

    if control in control_to_key_config:
        configuration = control_to_key_config[control]
        key = configuration[0]
        duration = configuration[1]
        press(key, duration)
    else:
        logger.error("{} control is not supported".format(control.name))

def press(key, seconds=0):
    keyboard.press(key)
    time.sleep(seconds)
    keyboard.release(key)

def rl_active():
    if GetWindowText(GetForegroundWindow()) == "Rocket League (64-bit, DX11, Cooked)":
        return True
    return False
