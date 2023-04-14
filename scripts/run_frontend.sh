#!/bin/bash

# Allow run frontend in local env

ADIR="$(
    cd "$(dirname "$0")" >/dev/null 2>&1
    pwd -P
)"
FRONT_DIR="${ADIR}/../harcownik-frontend/"

log_info() {
    echo "$(date) [INFO]: $*"
}

#----------------------------------------------#
#                   MAIN                       #
#----------------------------------------------#

cd ${FRONT_DIR}
if [ -d "${FRONT_DIR}/node_modules" ]; then
    log_info "Packages are installed"
else
    log_info "Installing packages..."
    npm install
    log_info "Packages are installed"
fi

npm start