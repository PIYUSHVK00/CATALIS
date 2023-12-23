import subprocess
import pyinotify

button_gpio_pin = 479
button_path = f"/sys/class/gpio/gpio{button_gpio_pin}/value"

try:
    with open("/sys/class/gpio/export", "w") as export_file:
        export_file.write(f"{button_gpio_pin}")
except IOError:
    pass

with open(f"/sys/class/gpio/gpio{button_gpio_pin}/direction", "w") as direction_file:
    direction_file.write("in")


class ButtonEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        button_state = subprocess.getoutput(f"cat {button_path}")

        if button_state == "1":
            data = {
                "key1": "Test1",
                "key2": "value2",
            }

            with open("test1.txt", "w") as file:
                for key, value in data.items():
                    file.write(f"{key}: {value}\n")


wm = pyinotify.WatchManager()
handler = ButtonEventHandler()
notifier = pyinotify.Notifier(wm, handler)
wm.add_watch(button_path, pyinotify.IN_MODIFY)

notifier.loop()
