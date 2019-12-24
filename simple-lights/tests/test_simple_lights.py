from simple_lights import start_lighting


def test_when_ran_then_pin_18_is_lit_up():
    time = FakeTime()
    gpio = FakeGPIO()

    start_lighting(time, gpio)




class FakeTime:
    def sleep(time):
        pass

class FakeGPIO:
    def setmode(mode):
        pass

    def setwarnings(show_warnings):
        pass

    def setup(pin, in_or_out):
        pass

    def output(pin, level):
        pass
    