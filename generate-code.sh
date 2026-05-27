# bash generate-code.sh generated this repository!
echo ${PWD}

VERSION=${$1:?Version number required}

DOCKER_IMAGE=docker.io/openapitools/openapi-generator-cli:latest-release

docker image pull $DOCKER_IMAGE
docker run --rm -v ${PWD}:/local $DOCKER_IMAGE generate \
    -i https://typed-pid-maker.datamanager.kit.edu/preview/v3/api-docs \
    -g python \
    -o /local \
    --additional-properties=packageName=pytypid_generated_client,packageUrl=https://github.com/kit-data-manager/typid-client,packageVersion=${VERSION:?Version number required},disallowAdditionalPropertiesIfNotPresent=false
