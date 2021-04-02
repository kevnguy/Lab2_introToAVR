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
tests = [ {'description': 'PINA: 0x00, PINB: 0x00, PINC: 0x00 => PORTD: 0x00',
    'steps': [ {'inputs': [('PINA',0x00), ('PINB',0x00), ('PINC', 0x00)], 'iterations': 1 } ],
    'expected': [('PORTD',0x00)],
    },
    {'description': 'PINA: 0x2D, PINB: 0x2D, PINC: 0x2D => PORTD: 0x84',
    'steps': [ {'inputs': [('PINA',0x2D), ('PINB',0x2D), ('PINC', 0x2D)], 'iterations': 1 } ],
    'expected': [('PORTD',0x84)],
    },
    {'description': 'PINA: 0x40, PINB: 0x40, PINC: 0x40 => PORTD: 0xC1',
    'steps': [ {'inputs': [('PINA',0x40), ('PINB',0x40), ('PINC', 0x40)], 'iterations': 1 } ],
    'expected': [('PORTD',0xC1)],
    },
    {'description': 'PINA: 0x80, PINB: 0x0F, PINC: 0x04 => PORTD: 0x93',
    'steps': [ {'inputs': [('PINA',0x80), ('PINB',0x0F), ('PINC', 0x04)], 'iterations': 1 } ],
    'expected': [('PORTD',0x93)],
    },
    {'description': 'PINA: 0x51, PINB: 0x64, PINC: 0x79 => PORTD: 0x79',
    'steps': [ {'inputs': [('PINA',0x1F), ('PINB',0x64), ('PINC', 0x79)], 'iterations': 1 } ],
    'expected': [('PORTD',0xFF)],
    },
    {'description': 'PINA: 0x54, PINB: 0x54, PINC: 0x54 => PORTD: 0xFD',
    'steps': [ {'inputs': [('PINA',0x54), ('PINB',0x54), ('PINC', 0x54)], 'iterations': 1 } ],
    'expected': [('PORTD',0xFD)],
    },
    {'description': 'PINA: 0x55, PINB: 0x00, PINC: 0x00 => PORTD: 0x56',
    'steps': [ {'inputs': [('PINA',0x55), ('PINB',0x00), ('PINC', 0x00)], 'iterations': 1 } ],
    'expected': [('PORTD',0x56)],
    },
    ]
watch = ['main::weightA', 'main::weightB', 'main::weightC','main::weightT',]  # PORTC optimized out? 
