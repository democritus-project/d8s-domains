# -*- coding: utf-8 -*-

import os
import sys
from typing import Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import decorators
from typings import ListOfStrs, DictStrKeyAnyVal


def is_domain(possible_domain: str) -> bool:
    """Check if the given string is a domain."""
    domains = domains_find(possible_domain)
    if len(domains) == 1 and domains[0] == possible_domain:
        return True

    return False


# TODO: this function will sometimes create/return duplicates... probably need to have some option to prevent duplicates
def domain_examples(n: int = 10) -> ListOfStrs:
    """Create n domain names."""
    from hypothesis.provisional import domains

    from hypothesis_data import hypothesis_get_strategy_results

    results = hypothesis_get_strategy_results(domains, n=n)

    return results


def domains_find(text: str, **kwargs: bool) -> ListOfStrs:
    """Parse domain names from the given text."""
    from ioc_finder import ioc_finder

    return ioc_finder.parse_domain_names(text, **kwargs)


@decorators.get_first_arg_url_domain
def domain_dns(domain: str) -> str:
    """Get the DNS results for the given domain."""
    import socket

    return socket.gethostbyname(domain)


@decorators.get_first_arg_url_domain
def domain_certificate_peers(domain: str) -> ListOfStrs:
    """Return a list of all domains sharing a certificate with the given domain."""
    import socket
    import ssl

    ctx = ssl.create_default_context()
    s = ctx.wrap_socket(socket.socket(), server_hostname=domain)
    s.connect((domain, 443))
    cert = s.getpeercert()
    return [domain_name[1] for domain_name in cert['subjectAltName']]


@decorators.get_first_arg_url_domain
def domain_whois(domain: str) -> Optional[DictStrKeyAnyVal]:
    """."""
    import whois

    whois_data = whois.query(domain)
    if whois_data:
        return whois_data.__dict__
    else:
        return None


@decorators.get_first_arg_url_domain
def domain_subdomains(domain_name: str) -> str:
    """Get the subdomains for the given domain name."""
    import tldextract

    return tldextract.extract(domain_name).subdomain


@decorators.get_first_arg_url_domain
def domain_second_level_name(domain_name: str) -> str:
    """Get the second level name for the given domain name (e.g. google from https://google.co.uk)."""
    import tldextract

    return tldextract.extract(domain_name).domain


@decorators.get_first_arg_url_domain
def domain_tld(domain_name: str) -> str:
    """Get the top level domain for the given domain name."""
    import tldextract

    return tldextract.extract(domain_name).suffix


@decorators.get_first_arg_url_domain
def domain_rank(domain_name: str) -> int:
    """."""
    from networking import get

    onemillion_api_url = f'http://onemillion.hightower.space/onemillion/{domain_name}'
    return get(onemillion_api_url)


@decorators.get_first_arg_url_domain
def domain_as_punycode(domain_name: str) -> str:
    """Convert the given domain name to Punycode (https://en.wikipedia.org/wiki/Punycode)."""
    return domain_name.encode('idna').decode('utf-8')


@decorators.get_first_arg_url_domain
def domain_as_unicode(domain_name: str) -> str:
    """Convert a given domain name to Unicode (https://en.wikipedia.org/wiki/Unicode)."""
    return domain_name.encode('utf-8').decode('idna')


# TODO: cache this data
def tlds() -> ListOfStrs:
    """Get the top level domains from https://iana.org/."""
    from networking import get
    from strings import lowercase

    top_level_domains = get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt').split('\n')[1:-1]
    return lowercase(top_level_domains)


@decorators.map_first_arg
def is_tld(possible_tld: str) -> bool:
    """Return whether or not the possible_tld is a valid tld."""
    from strings import lowercase

    # remove any periods from the beginning (in case someone provides the TLD like `.com` rather than just `com`)
    possible_tld = possible_tld.lstrip('.')

    valid_tlds = tlds()
    tld_is_valid = lowercase(possible_tld) in lowercase(valid_tlds)
    return tld_is_valid
