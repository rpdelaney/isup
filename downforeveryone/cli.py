"""Define a command-line interface for the isup module.

Call parse_args() to return an argument parser namespace
"""
import argparse


def parse_args() -> argparse.Namespace:
    """Define an argument parser and return the parsed arguments."""
    parser = argparse.ArgumentParser(
        prog="isup",
        description="checks if a site is down for everyone or just you",
    )
    parser.add_argument("url", help="url to test")

    return parser.parse_args()
