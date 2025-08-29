#!/usr/bin/env python3

# Dependencies:
# python3-dnspython

# Used Modules:
import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

# Initialize Resolver-Class from dns.resolver as "NS"
NS = dr.Resolver()

# List of found subdomains
Subdomains = []

# Define the AXFR Function
def AXFR(domain, nameserver):
    # Try zone transfer for given domain and nameserver
    try:
        # Perform the zone transfer
        axfr = dz.from_xfr(dq.xfr(nameserver, domain))
        # If zone transfer was successful
        if axfr:
            print('[*] Successful Zone Transfer from {}'.format(nameserver))
            # Add found subdomains to global 'Subdomains' list
            for record in axfr:
                Subdomains.append('{}.{}'.format(record.to_text(), domain))
    except Exception as error:
        print(error)
        pass

# Main
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Zone transfer script.')
    parser.add_argument('-target', '--domain', type=str, required=True, help='Target domain for zone transfer')

    args = parser.parse_args()
    Domain = args.domain

    # Set the nameservers that will be used
    NS.nameservers = ['ns1.inlanefreight.com', 'ns2.inlanefreight.com']

    # For each nameserver
    for nameserver in NS.nameservers:
        # Try AXFR
        AXFR(Domain, nameserver)

    # Print the results
    if Subdomains:
        print('-------- Found Subdomains:')
        for subdomain in Subdomains:
            print('{}'.format(subdomain))
    else:
        print('No subdomains found.')
        exit()