#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_domains/ tests/

black democritus_domains/ tests/

mypy democritus_domains/ tests/

pylint --fail-under 9 democritus_domains/*.py

flake8 democritus_domains/ tests/

bandit -r democritus_domains/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_domains/ tests/
