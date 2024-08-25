import sys


def keyboard_interrupt_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n\nKeyboardInterrupt: Program terminated by user.")
            sys.exit(1)

    return wrapper