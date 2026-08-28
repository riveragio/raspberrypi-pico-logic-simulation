# Raspberry Pi Pico Logic Gate Simulator

A simple hardware-based **Logic Gate Simulator** built using a Raspberry Pi Pico, push buttons, an LED, and a 0.96-inch OLED display.

The project demonstrates the behavior of common digital logic gates using two user-controlled binary inputs. The resulting logic output is represented by an LED, while the OLED displays the currently selected logic gate and input/output states.

## Features

* Two configurable binary inputs
* Push-button input controls
* Logic gate selection using a dedicated button
* LED logic output indicator
* OLED status display
* Supports multiple logic gates
* Simple educational tool for learning digital logic

## Supported Logic Gates

The simulator supports the following gates:

* AND
* OR
* XOR
* NAND
* NOR
* XNOR

The gate selection button cycles through the available gates:

```text
AND → OR → XOR → NAND → NOR → XNOR → AND
```

## Components

* Raspberry Pi Pico
* 3× Tactile Push Buttons
* 1× LED
* 1× 220Ω–330Ω Resistor
* 1× 0.96" I2C OLED Display (SSD1306)
* Breadboard
* Jumper Wires

## Pin Configuration

| Component             | Raspberry Pi Pico GPIO |
| --------------------- | ---------------------- |
| Input A Button        | GP14                   |
| Input B Button        | GP15                   |
| Gate Selection Button | GP16                   |
| Output LED            | GP17                   |
| OLED SDA              | GP4                    |
| OLED SCL              | GP5                    |
| OLED VCC              | 3V3                    |
| OLED GND              | GND                    |

The buttons use the Raspberry Pi Pico's internal pull-up resistors, so external resistors are not required for the button inputs.

A current-limiting resistor should be connected in series with the LED.

## Controls

### Input A Button

Pressing the Input A button toggles Input A between:

```text
0 → 1 → 0 → 1 ...
```

### Input B Button

Pressing the Input B button toggles Input B in the same way.

### Gate Selection Button

Pressing the Gate Selection button changes the currently active logic gate.

```text
AND
 ↓
OR
 ↓
XOR
 ↓
NAND
 ↓
NOR
 ↓
XNOR
 ↓
AND
```

## Output

The LED represents the result of the selected logic operation.

```text
LED OFF = Logic 0
LED ON  = Logic 1
```

For example, with the AND gate selected:

```text
A = 0
B = 0
OUT = 0
LED = OFF
```

After setting both inputs to `1`:

```text
A = 1
B = 1
OUT = 1
LED = ON
```

## OLED Display

The 0.96" OLED provides information about the current simulator state.

Example:

```text
LOGIC SIMULATOR

Gate: AND

A: 1    B: 0

OUT: 0
```

This allows the selected gate and logic states to be monitored without connecting the Pico to a computer.

## Circuit Connections

### Push Buttons

```text
GP14 ---- Input A Button ---- GND
GP15 ---- Input B Button ---- GND
GP16 ---- Gate Button ------- GND
```

The GPIO pins are configured using the Pico's internal pull-up resistors.

### LED

```text
GP17 ---- 220Ω/330Ω ---- LED ---- GND
```

### OLED

```text
Raspberry Pi Pico       OLED
--------------------------------
3V3 ------------------- VCC
GND ------------------- GND
GP4 ------------------- SDA
GP5 ------------------- SCL
```

## Software Requirements

The project uses:

* MicroPython
* SSD1306 MicroPython driver
* Thonny IDE or another MicroPython-compatible development environment

The Raspberry Pi Pico should be flashed with compatible MicroPython firmware.

## How It Works

The Raspberry Pi Pico monitors three push buttons.

The first two buttons represent binary inputs `A` and `B`. Pressing either button toggles its corresponding value between `0` and `1`.

The third button changes the active logic gate.

The Pico evaluates the two inputs according to the selected logic operation and produces either a `0` or `1` output.

The result is then:

* displayed on the OLED;
* represented physically by the LED.

This allows common digital logic operations to be demonstrated interactively using physical controls.

## Example

Suppose XOR is selected:

```text
A = 0
B = 0
OUT = 0
```

Press Input A:

```text
A = 1
B = 0
OUT = 1
```

Press Input B:

```text
A = 1
B = 1
OUT = 0
```

The LED automatically turns ON or OFF according to the resulting output.

## Educational Purpose

This project can be used as a simple introduction to:

* Digital logic
* Boolean operations
* Logic gates
* Binary inputs and outputs
* GPIO programming
* Push-button interfacing
* I2C communication
* OLED displays
* Raspberry Pi Pico development
* MicroPython programming

## Possible Improvements

Future versions of the project could include:

* Logic gate symbols displayed on the OLED
* Truth table display
* NOT gate support
* Additional input channels
* Automatic demonstration mode
* Logic gate animations
* Buzzer feedback
* Larger OLED display
* Menu-based interface
* PCB implementation
* Custom enclosure
