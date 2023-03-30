#!/bin/bash

###########################################################
#            Script for pushing docker images             # 
###########################################################

log_sh() {
    echo "[$(date)][INFO] $@"
}

error_sh() {
    echo "[$(date)][ERROR] $@"
}

# values
tag="polo150199"


while getopts i:v:t flag
do
    case "${flag}" in
        i) images=${OPTARG};;
        v) version=${OPTARG};;
        t) tag=${OPTARG}
    esac
done

# image push to docker hub
docker tag ${image} ${tag}/${image}:${version}
docker push ${tag}/${image}:${version}
