#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A aids_jiance.taskapp worker -l INFO
