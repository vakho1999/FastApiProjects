.PHONY: test build deploy

image = registry.gitlab.com/nelbakidze/transaction_module
tag = development.v1

build:
	docker build --pull -t "$(image):$(tag)" .
    docker push $(image):$(tag)

test:
    echo "RUNNING UNIT TESTS"
	cd app/tests
    pytest --junitxml=test-results.xml

deploy:
#    'not implemented'
