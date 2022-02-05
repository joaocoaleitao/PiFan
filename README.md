# PiFan
A simple opensource project of an hat to cool you Raspberry.

Started this project because mostly all my Raspberrys end up overheating and then throttling.
So here it is!
The PiFan!
Simply put is a stackable HAT for raspberry, it can run a 100% all the time if you remove the jumper JP3 and that way you can also use the GPIO 17 for other things. Or you can keep the jumper and run the script in Python at boot and it will use the settings to control the speed through PWM.

My first tests suggest a maximum temperature of around 50C when using the fan while testing with "cpuburn-a53".

The HAT can slide down the existing GPIO pins and be tightened with a screw or you can solder a female connector (which can be the long pin version so you can stack another hat on top.)


