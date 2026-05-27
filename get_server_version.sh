#!/usr/bin/env bash

VERSION=$(\
    curl -s https://typed-pid-maker.datamanager.kit.edu/preview/actuator/info \
    | jq --raw-output '.build.version'\
)

echo "$VERSION"
