#!/usr/bin/env python3

import os
import sys
import platform

# For development purpose we need to use swmclient from the sources:
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from swmclient.api import SwmApi


def main() -> None:
    swm_api = SwmApi(
        url=f"https://{platform.node()}:8443",
        key_file="~/.swm/key.pem",
        cert_file="~/.swm/cert.pem",
        ca_file="/opt/swm/spool/secure/cluster/ca-chain-cert.pem",
    )
    nodes = swm_api.get_nodes()
    for node in nodes:
        print(f"Node: {node}")


if __name__ == "__main__":
    main()
