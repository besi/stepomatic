# Stepomatic

Wifi-enabled 28BYJ-48 stepper motor driver.

![](stepomatic.png)


## Pinout

| Function   | Pin    |
|:-----------|-------:|
| Motor 1    | 13     |
| Motor 2    | 12     |
| Motor 3    | 14     |
| Motor 4    | 15     |
| SDA        | 4      |
| SCL        | 5      |
| Mode       | 0      |
| Neopixel   | 16     |
| Enable IR  | 2      |
| Distance   | ADC(0) |

The IR diode can be enabled by pulling `IO2` to `0`.

The SDA and SCL need to be pulled high in software.


## Flashing

The used ESP-07 chip uses 1MB of flash so make sure to flash it with the [1MB flash image](https://micropython.org/download/ESP8266_GENERIC/).


## JLC Componennts

    # Put this in your ~/.zshrc or ~/.bashrc
    alias jlc='JLC2KiCadLib -dir lib'
    
    # Now the following will download kicad symbols, footprints and 3d models
    jlc C82227

## Acknowledgments

- Special thanks to Valentyna M. for designing the pcb artwork.
- The free font [Dexotick](https://www.behance.net/dhanstudio) was used for the pcb artwork.
- [JLC2KiCadLib](https://pypi.org/project/JLC2KiCadLib) was used for downloading the footprints for the LCSC footprints

## Known issues

The Neopixel on Pin 16 does not work since that Pin has some limitations and neither supports PWM or I2C.
