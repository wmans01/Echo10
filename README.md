# Echo10
Echo10 is a 11 key macropad (10.57% of the keys of an actual keyboard, hence the name). It uses KMK firmware and maximizes functionality through three layers of toggleable keymaps.


## Features
- Two layer 3D printed case
- Minimalistic design to maximize productivity :))
- 8 degree tilt for ergonomic comfort
- 11 Keys
- Seeed Xiao RP2040 MCU
- Ground planes on both sides and stitched vias

## CAD Model:
Case assembled using 4 M3 bolts, screwed directly into plastic on the four corners of the case. 

![CAD Rendering of Echo10](/assets/Echo10WithSwitches.png)

The case also has an 8 degree incline for ergonomics

![CAD Rendering of Echo10](/assets/Echo10WithSwitchesBottom.png)

Made and rendered in Autodesk Inventor


## PCB
This is the PCB for the Echo10. It is a two layer PCB with ground planes on both sides and uses via stitching. <br>

![Schematic](/assets/Schematic.png)
![PCB Layout](/assets/PCB.png)
###### Designed with KiCAD.

I used MX_V2 for the keyswitch footprints. In retrospect, adding feedback through a display or LED might have been more effective. I also could have been more fancy with the designs on the silkscreen.


## Firmware
This macropad uses [KMK](https://github.com/KMKfw/kmk_firmware) firmware.<br>
The current firmware for this macropad allows for 27 different macros. This includes three layers of 9 macros each, accessible through the two switches at the top of the macropad. Currently, the macros are placeholders and just output text, but I will change them later.


## BOM
- 11x Cherry MX Switches
- 11x DSA Keycaps
- 4x M3x12mm SHCS Bolts
- 1x XIAO RP2040
- 1x Case (2 printed parts)
