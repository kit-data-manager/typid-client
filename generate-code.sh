# bash generate-code.sh generated this repository!
echo ${PWD}
podman run --rm -v ${PWD}:/local docker.io/openapitools/openapi-generator-cli:latest generate \
    -i https://typed-pid-maker.datamanager.kit.edu/preview/v3/api-docs \
    -g python \
    -o /local/src/typid_client/generated