import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

encoder_handler.pin = ((board.GP1, board.GP2))

keyboard.col_pins = (board.GP29, board.GP6, board.GP7)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Will likely change these values later
keyboard.keymap = [
    [KC.ESC, KC.CLCK, KC.BSPC]
    [KC.SPC, KC.UP, KC.ENT]
    [KC.LEFT, KC.DOWN, KC.RIGHT]
]

encoder_handler.map = [((KC.VOLD, KC.VOLU),)]

rgb = RGB(
    pixel_pin=board.GP4,
    num_pixels=1,
    rgb_order=(1, 0, 2),
    animation_mode=AnimationModes.STATIC,
    hue=300,
    val=100,
)

if __name__ == '__main__':
    keyboard.go()