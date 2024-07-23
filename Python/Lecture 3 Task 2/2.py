from pynotifier import Notification
import psutil

battery = psutil.sensors_battery()
Notification(
    title="battery percentage",
    description=str(battery.percent) + "%Percent",
    duration=10
).send()
