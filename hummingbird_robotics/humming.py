def on_button_pressed_a():
    global A_button, B_button
    A_button = 1
    B_button = 0
    if hummingbird.get_battery() > 5000:
        hummingbird.set_position_servo(FourPort.ONE, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global B_button, A_button
    B_button = 1
    A_button = 0
    if hummingbird.get_battery() > 5000:
        hummingbird.set_position_servo(FourPort.ONE, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

B_button = 0
A_button = 0
hummingbird.start_hummingbird()
music.play(music.string_playable("A G F E D C G A ", 120),
    music.PlaybackMode.UNTIL_DONE)
A_button = 0
B_button = 0

def on_forever():
    if A_button == 1:
        hummingbird.set_led(ThreePort.ONE, 0)
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_HEART)
    else:
        hummingbird.set_led(ThreePort.ONE, 50)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    hummingbird.set_tri_led(TwoPort.ONE,
        hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE),
        80,
        80)
basic.forever(on_forever)

