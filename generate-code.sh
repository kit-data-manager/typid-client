# bash generate-code.sh generated this repository!
echo ${PWD}
docker run --rm -v ${PWD}:/local docker.io/openapitools/openapi-generator-cli:latest generate \
    -i https://typed-pid-maker.datamanager.kit.edu/preview/v3/api-docs \
    -g python \
    -o /local \
    --additional-properties=packageName=pytypid_generated_client,packageUrl=https://github.com/kit-data-manager/typid-client,packageVersion=0.2.0,disallowAdditionalPropertiesIfNotPresent=false