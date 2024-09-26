# Robowar
https://github.com/borgdog/MPF_Gemini/tree/main/config

https://missionpinball.org/latest/hardware/lisy/troubleshooting/

https://github.com/AmokSolderer/APC/blob/master/DOC/Software/MPF/Rollergames/config/config.yaml


17.6.1. Using lamp driver as coils ( LISY1 & LISY80 )
As Gottlieb was ‘running out’ on coil drivers in later games they used lamp drivers with an ‘extra
transistor’ to solve that problem. In MPF these ‘lamps’ need to be controlled in the same way as
coils. For LISY1 & LISY80 you can define a lamp as a coil by adding ‘100’ to the lamp number.
Example for ‘config.yaml’
coils:
 c_trough_release: # trough is a 'lamp' (L12), so we add 100 to the number
 number: 112
This is for Gottlieb Devils Dare, in this game the ball release coil is controlled by lamp driver #12. So
the ‘virtual’ coil ‘c_trough_release’ is defined with number 112 ( 100 + 12).


couleur rouge/orange ff1900


Regles :
	-
