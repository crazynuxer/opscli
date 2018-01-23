import argparse
from opscli.tools import describe_connectivity, describe_security_group
from opscli.configure import configure

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='1.0.0')

    subparser = parser.add_subparsers()

    configure_parser = subparser.add_parser('configure')
    configure_parser.set_defaults(func=configure)

    describe_connectivity_parser = subparser.add_parser('describe-connectivity')
    describe_connectivity_parser.add_argument('--ticket-id')
    describe_connectivity_parser.add_argument('--detailed', action='store_true', default=False)
    describe_connectivity_parser.set_defaults(func=describe_connectivity)

    describe_secgroup_parser = subparser.add_parser('describe-security-group')
    describe_secgroup_parser.add_argument('--group-id')
    describe_secgroup_parser.add_argument('--group-name')
    describe_secgroup_parser.add_argument('--detailed', action='store_true')
    describe_secgroup_parser.set_defaults(func=describe_security_group)

    return parser
