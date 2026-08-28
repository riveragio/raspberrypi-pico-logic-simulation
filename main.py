from machine import Pin, I2C
from time import sleep_ms
import ssd1306

# -------------------------
# Pin Configuration
# -------------------------

BUTTON_A_PIN = 14
BUTTON_B_PIN = 15
GATE_BUTTON_PIN = 16
LED_PIN = 17

OLED_SDA_PIN = 4
OLED_SCL_PIN = 5


# -------------------------
# GPIO Setup
# -------------------------

button_a = Pin(BUTTON_A_PIN, Pin.IN, Pin.PULL_UP)
button_b = Pin(BUTTON_B_PIN, Pin.IN, Pin.PULL_UP)
gate_button = Pin(GATE_BUTTON_PIN, Pin.IN, Pin.PULL_UP)

led = Pin(LED_PIN, Pin.OUT)


# -------------------------
# OLED Setup
# -------------------------

i2c = I2C(
    0,
    sda=Pin(OLED_SDA_PIN),
    scl=Pin(OLED_SCL_PIN),
    freq=400000
)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)


# -------------------------
# Logic Gate Configuration
# -------------------------

gates = [
    "AND",
    "OR",
    "XOR",
    "NAND",
    "NOR",
    "XNOR"
]

gate_index = 0

input_a = 0
input_b = 0


# -------------------------
# Logic Gate Function
# -------------------------

def calculate_gate(gate, a, b):

    if gate == "AND":
        return a & b

    elif gate == "OR":
        return a | b

    elif gate == "XOR":
        return a ^ b

    elif gate == "NAND":
        return int(not (a & b))

    elif gate == "NOR":
        return int(not (a | b))

    elif gate == "XNOR":
        return int(not (a ^ b))

    return 0


# -------------------------
# OLED Display
# -------------------------

def update_display():

    gate = gates[gate_index]

    output = calculate_gate(
        gate,
        input_a,
        input_b
    )

    led.value(output)

    oled.fill(0)

    oled.text("LOGIC SIMULATOR", 0, 0)

    oled.text(
        "Gate: " + gate,
        0,
        16
    )

    oled.text(
        "A: " + str(input_a),
        0,
        32
    )

    oled.text(
        "B: " + str(input_b),
        50,
        32
    )

    oled.text(
        "OUT: " + str(output),
        0,
        48
    )

    oled.show()


# -------------------------
# Initial Display
# -------------------------

update_display()


# -------------------------
# Main Loop
# -------------------------

last_a = 1
last_b = 1
last_gate = 1

while True:

    current_a = button_a.value()
    current_b = button_b.value()
    current_gate = gate_button.value()

    # ---------------------
    # Input A
    # ---------------------

    if last_a == 1 and current_a == 0:

        input_a = not input_a
        input_a = int(input_a)

        update_display()

        sleep_ms(200)


    # ---------------------
    # Input B
    # ---------------------

    if last_b == 1 and current_b == 0:

        input_b = not input_b
        input_b = int(input_b)

        update_display()

        sleep_ms(200)


    # ---------------------
    # Change Logic Gate
    # ---------------------

    if last_gate == 1 and current_gate == 0:

        gate_index += 1

        if gate_index >= len(gates):
            gate_index = 0

        update_display()

        sleep_ms(200)


    last_a = current_a
    last_b = current_b
    last_gate = current_gate

    sleep_ms(10)
