import pytest

from simple_lights import start_lighting


@pytest.fixture()
def setup():

    time = FakeTime()
    gpio = FakeGPIO()

    return time, gpio


def test_when_ran_then_sleeps_for_one_second(time, gpio):
    start_lighting(time, gpio)

    assert time.time_slept == 1


def test_when_ran_then_sets_pin_18_as_high_output(time, gpio):
    start_lighting(time, gpio)

    assert 18 == gpio.output_calls[0]['pin']
    assert GPIO.HIGH == gpio.output_calls[0]['level']


def test_when_ran_then_sets_pin_18_as_low_output(time, gpio):
    start_lighting(time, gpio)

    assert 18 == gpio.output_calls[0]['pin']
    assert GPIO.LOW == gpio.output_calls[0]['level']


class FakeTime:
    def __init__(self):
        self.time_slept = 0

    def sleep(self, time):
        self.time_slept = time


class FakeGPIO:

    def __init__(self):
        self.output_calls = []
        self.setup_calls = []
        self.show_warnings = None
        self.mode = None

    def setmode(self, mode):
        self.mode = mode

    def setwarnings(self, show_warnings):
        self.show_warnings = show_warnings

    def setup(self, pin, in_or_out):
        self.setup_calls.append({'pin': pin, 'in_or_out': in_or_out})

    def output(self, pin, level):
        self.output_calls.append({'pin': pin, 'level': level})
