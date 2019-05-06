import argparse

from .gen import render_service_clients

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--services', nargs='+', required=False)
    args = parser.parse_args()
    render_service_clients(args.services)
