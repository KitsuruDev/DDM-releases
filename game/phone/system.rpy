init offset = -120

init python in phone.system:
    from renpy import store
    from store.phone.config import time_format
    from datetime import datetime, time

    CONNECTED, NO_INTERNET, NOT_CONNECTED, AIRPLANE_MODE, CELLULAR_DATA = 1, 2, 3, 4, 5

    renpy.const("phone.system.CONNECTED")
    renpy.const("phone.system.NO_INTERNET")
    renpy.const("phone.system.NOT_CONNECTED")
    renpy.const("phone.system.AIRPLANE_MODE")
    renpy.const("phone.system.CELLULAR_DATA")

    def get_internet_connection_state():
        if airplane_mode:              return AIRPLANE_MODE
        if not internet_connection:    return NO_INTERNET
        if wifi and not cellular_data: return CONNECTED
        if not wifi and cellular_data: return CELLULAR_DATA
        return NOT_CONNECTED

    def get_battery_level():
        return int(battery_level)

    def get_date():
        return datetime.now()

    def get_time():
        return time(hour=clock[0], minute=clock[1]).strftime(__(time_format))

# If any of these "If not `None`" values are `None`, they're taken from the player's device.
default phone.system.clock = (1, 1)
default phone.system.battery_level = 100

default phone.system.brightness = 1.0 # [phone.config.lowest_brightness, 1.0]

####################################### НАЖАТИЕ КНОПОК В ПОДМЕНЮШКЕ МОБИЛЬНИКА #######################################

default phone.system.internet_connection = True
default phone.system.cellular_data = False
default phone.system.wifi = False
default phone.system.airplane_mode = False
default phone.system.bluetooth = False
default phone.system.rotation_locked = False
default phone.system.at_list = [] # A transform or list of transforms applied to the phone screen (overlay screens excluded).
default phone.system.dark_mode = False
default phone.system.flashlight = False
default phone.system.volume = 1.0

####################################### ДОСТУП К КНОПКАМ В ИНТЕРАКТИВЕ #######################################

default phone.system.cellular_data_lock = True
default phone.system.wifi_lock = True
default phone.system.airplane_mode_lock = True
default phone.system.bluetooth_lock = True
default phone.system.flashlight_lock = True
default phone.system.volume_lock = True
