import argparse

from .gen import render


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--services", nargs="+", required=False)
    args = parser.parse_args()
    render(args.services)
