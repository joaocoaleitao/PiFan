This Python script controls the fan speed and temperature settings.
Copy the PythonPiFan folder to "/opt" folder and insert a line in crontab "@reboot cd /opt/PythonPiFan/ && python3 /opt/PythonPiFan/fan.py"
The file settings.ini in the PythonPiFan folder contains the following settings:

MinimumTemperature : Receives a number from where the temperature curve should start. 
Example: "MinimumTemperature = 25" if you want to start the fan climb at 25 Celsius degrees.

MaximumTemperature : Receives a number up to where the curve will grow. This effectively sets the 100% speed of the fan ceiling.
Example: "MaximumTemperature = 60" if you want the fan to hit 100% at 60 degrees

UpdateInterval : The interval at which the fan speed are updated based on current temperature.
Example: "UpdateInterval = 3" if you want to update the fan speed based on current temperature every 3 seconds.

MinimumFanSpeed : The minimum speed in percentage that the fan should rotate.
Example: "MinimumFanSpeed = 25" if you want the fan to never rotate a less than 25%

MaximumFanSpeed : The maximum speed in percentage that the fan should rotate.
Example: "MaximumFanSpeed = 90" to set the fan rotation speed at a maximum of 90%

Debug : If you want to print current settings and interval values.
Example: "Debug = 1" to print the values. set debug to zero if you want to turn them off