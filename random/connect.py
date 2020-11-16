from dns import resolver
from simple_chalk import chalk
from urllib import request, parse
import socket


class ldap_connection_report:

    def generate_connection_report(self, ldap_url='ldap://ldap.forumsys.com'):
        final_report = {
            "dns": {
                "addr": [],
                "rdns": [],
            },
            "tcp": {
                "port_reachable_mapping": []
            }
        }

        r = parse.urlparse(ldap_url)
        ldap_port = 389 if r.scheme == 'ldap' else 636
        print(r)
        print("------------------------")
        print(chalk.green.bold(f"Host name: {r.netloc}"))
        print(chalk.green.bold(f"Protocol: {ldap_port}"))
        print("------------------------")

        # A	    IP Address record. Using a hostname to get an IPv4 adress.
        # AAAA	IP Address record. Using a hostname to get an IPv6 adress.
        # PTR	reverse DNS lookup. Using IP address to get hostname.
        # NS	Nameserver record responsible for the domain asked about.
        # MX	Mail Exchanger record. server responsible for handling email for the given domain.
        # SOA	Start of Authorities record describes some key data about the zone as defined by the zone administrator.
        # CNAME	Canonical Name or Alias, this allows providing an alternate name for a resource.
        # TXT	A generic Text record that provides descriptive data about domain.

        # using -  A	IP Address record. Using a hostname to get an IPv4 adress.

        k = resolver.resolve(r.netloc, 'A')
        ldns_resolved = [ipval.to_text() for ipval in list(k)]
        # save dns report
        final_report["dns"]["addr"] = ldns_resolved
        # perform reverse dns lookup using the socket module.
        # Doing a reverse DNS lookup finds the domain name associated with a given IP address. For example, doing a reverse DNS lookup for 127.0.0.1 results in localhost.
        r_dns = [socket.gethostbyaddr(ip)[0] for ip in ldns_resolved]
        final_report["dns"]["rdns"] = r_dns

        # Check if port is reachable
        # Create a socket object by calling socket.socket(family, type) with family set to socket.AF_INET and type set to socket.SOCK_STREAM. socket.AF_INET specifies the IP address family for IPv4 and socket.
        # SOCK_STREAM specifies the socket type for TCP.
        # To check if a network port is open, call socket.connect_ex(location) with socket as the socket object and location as a tuple containing the IP address and desired port number.
        # If the port is open, socket.connect_ex() returns 0. After checking the port, close the socket by calling socket.close() with socket as the socket object.

        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_port_check = [a_socket.connect_ex(
            (item, ldap_port)) for item in ldns_resolved]

        if 0 not in result_of_port_check:
            result_of_port_check = ["Port not reachable"]
        else:
            result_of_port_check = ["Port is reachable"]
        # print("a_socket", 1 in result_of_port_check)

        final_report["tcp"]["port_reachable_mapping"] = result_of_port_check
        print("Final report: ", final_report)
        return final_report


if __name__ == "__main__":
    r = ldap_connection_report()
    print(chalk.blue.bold(r.generate_connection_report()))
