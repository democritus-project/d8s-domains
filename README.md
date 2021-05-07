# Democritus Domains

[![PyPI](https://img.shields.io/pypi/v/d8s-domains.svg)](https://pypi.python.org/pypi/d8s-domains)
[![CI](https://github.com/democritus-project/d8s-domains/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-domains/actions)
[![Lint](https://github.com/democritus-project/d8s-domains/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-domains/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-domains/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-domains)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with domains.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` (pronounced "dee-eights") as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Functions

  - ```python
    def is_domain(possible_domain: str) -> bool:
        """Check if the given string is a domain."""
    ```
  - ```python
    def domain_examples(n: int = 10) -> List[str]:
        """Create n domain names."""
    ```
  - ```python
    def domains_find(text: str, **kwargs: bool) -> List[str]:
        """Parse domain names from the given text."""
    ```
  - ```python
    def domain_dns(domain: str) -> str:
        """Get the DNS results for the given domain."""
    ```
  - ```python
    def domain_certificate_peers(domain: str) -> List[str]:
        """Return a list of all domains sharing a certificate with the given domain."""
    ```
  - ```python
    def domain_whois(domain: str) -> Optional[Dict[str, Any]]:
        """."""
    ```
  - ```python
    def domain_subdomains(domain_name: str) -> str:
        """Get the subdomains for the given domain name."""
    ```
  - ```python
    def domain_second_level_name(domain_name: str) -> str:
        """Get the second level name for the given domain name (e.g. google from https://google.co.uk)."""
    ```
  - ```python
    def domain_tld(domain_name: str) -> str:
        """Get the top level domain for the given domain name."""
    ```
  - ```python
    def domain_rank(domain_name: str) -> int:
        """."""
    ```
  - ```python
    def domain_is_member(domain_to_check: str, domain_base: str) -> bool:
        """Given two domains, check if the first domain is a member of the second domain.
    A member means it is either the domain itself, or a subdomain of the domain."""
    ```
  - ```python
    def domain_as_punycode(domain_name: str) -> str:
        """Convert the given domain name to Punycode (https://en.wikipedia.org/wiki/Punycode)."""
    ```
  - ```python
    def domain_as_unicode(domain_name: str) -> str:
        """Convert a given domain name to Unicode (https://en.wikipedia.org/wiki/Unicode)."""
    ```
  - ```python
    def tlds() -> List[str]:
        """Get the top level domains from https://iana.org/."""
    ```
  - ```python
    def is_tld(possible_tld: str) -> bool:
        """Return whether or not the possible_tld is a valid tld."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-
