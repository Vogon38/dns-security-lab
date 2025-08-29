#!/usr/bin/env python3

# Dependencies:
# python3-dnspython

# Used Modules:
import dns.zone as dz
import dns.query as dq
import argparse

# List of found subdomains
Subdomains = []

# Define the AXFR Function
def AXFR(domain, nameserver):
    try:
        # Perform the zone transfer
        axfr = dz.from_xfr(dq.xfr(nameserver, domain))
        if axfr:
            print('[*] Successful Zone Transfer from {}'.format(nameserver))
            for record in axfr:
                Subdomains.append('{}.{}'.format(record.to_text(), domain))
    except Exception as error:
        print(f"Error with {nameserver}: {error}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="dns-axfr.py", epilog="DNS Zonetransfer Script",
                                     usage="dns-axfr.py [options] -d <DOMAIN>", prefix_chars='-')
    parser.add_argument('-d', metavar='Domain', type=str, help='Target Domain', required=True)
    parser.add_argument('-n', metavar='Nameserver', type=str, help='Nameservers separated by comma')
    parser.add_argument('-v', action='version', version='DNS-AXFR - v1.0')

    args = parser.parse_args()

    if not args.d:
        print('[!] You must specify target Domain.')
        parser.print_help()
        exit()

    if not args.n:
        print('[!] You must specify target nameservers.')
        parser.print_help()
        exit()

    Domain = args.d
    # Separar os nomes dos servidores em uma lista
    nameservers = [ns.strip() for ns in args.n.split(',')]

    # Para cada nameserver, tentar o AXFR passando o nome ou IP
    for ns in nameservers:
        print(f"Attempting zone transfer from {ns}...")
        AXFR(Domain, ns)

    # Mostrar resultados
    if Subdomains:
        print('-------- Found Subdomains:')
        for sub in set(Subdomains):  # usar set para remover duplicados
            print(sub)
    else:
        print('No subdomains found.')
