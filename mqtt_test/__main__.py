import argparse

from dotenv import load_dotenv

load_dotenv('.env')

parser = argparse.ArgumentParser(description='MQTT Test')
subparsers = parser.add_subparsers()


def publish(args):
    from .publisher import main
    main()


def subscribe(args):
    from .subscriber import main
    main()


parser_start = subparsers.add_parser('publish', help='publish')
parser_start.set_defaults(handler=publish)

parser_start = subparsers.add_parser('subscribe', help='subscribe')
parser_start.set_defaults(handler=subscribe)

args = parser.parse_args()

if not hasattr(args, 'handler'):
    parser.print_help()
    exit(1)

args.handler(args)
