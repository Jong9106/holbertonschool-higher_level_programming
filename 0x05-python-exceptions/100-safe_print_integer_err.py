#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        int(value)
        print("{:d}".format(value))
        return True
        raise
    except ValueError as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return False
    except:
        print("Exception: {}".format(i), file=sys.stderr)
        return False
