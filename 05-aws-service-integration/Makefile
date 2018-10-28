.PHONY: help create delete info deploy

environment = "eu-west-1"

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

create: ## create env
	sceptre launch-env $(environment)

delete: ## delete env
	sceptre delete-env $(environment)

info: ## describe resources
	@sceptre describe-env-resources $(environment)

deploy: delete create info ## delete and create

describe: ## describe the stack outputs
	sceptre describe-stack-outputs $(environment) tour-of-heroes

merge-swagger: ## merged swagger with api gateway
	@aws-cfn-update \
		rest-api-body  \
		--resource RestAPI \
		--open-api-specification swagger/swagger.yaml \
		--api-gateway-extensions swagger/aws-extensions.yaml \
		--add-new-version \
		templates/api-gateway.yaml
