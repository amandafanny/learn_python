import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    parser.print_help()
    return parser.parse_args()

if __name__ == '__main__':
    get_args()