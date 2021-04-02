# Array of tests to run (in order)
# Each test contains
#   description -
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.)
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in
# that they are not ran in isolation but in the order shown and
tests = [ {'description': 'PINA: 0x00 => PORTC: 0x04',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 1 } ],
    'expected': [('PORTC',0x04)],
    },
    {'description': 'PINA: 0x03 => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x03)], 'iterations': 1 } ],
    'expected': [('PORTC',0x02)],
    },
    {'description': 'PINA: 0x05 => PORTC: 0x02',
    'steps': [ {'inputs': [('PINA',0x05)], 'iterations': 1 } ],
    'expected': [('PORTC',0x02)],
    },
    {'description': 'PINA: 0x08 => PORTC: 0x03',
    'steps': [ {'inputs': [('PINA',0x08)], 'iterations': 1 } ],
    'expected': [('PORTC',0x03)],
    },
    {'description': 'PINA: 0x0F => PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0x0F)], 'iterations': 1 } ],
    'expected': [('PORTC',0x80)],
    },
    {'description': 'PINA: 0x0E => PORTC: 0x01',
    'steps': [ {'inputs': [('PINA',0x0E)], 'iterations': 1 } ],
    'expected': [('PORTC',0x01)],
    },
    {'description': 'PINA: 0xFF => PORTC: 0x00',
    'steps': [ {'inputs': [('PINA',0xFF)], 'iterations': 1 } ],
    'expected': [('PORTC',0x80)],
    },
    ]
watch = ['main::count', 'main::A0', 'main::A1','main::A2', 'main::A3']  # PORTC optimized out? 
