IMAGE_NAME = front-builder

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) . -f Dockerfile.openshift

.PHONY: test
test:
	docker build -t $(IMAGE_NAME)-candidate . -f Dockerfile.openshift
	IMAGE_NAME=$(IMAGE_NAME)-candidate test/run
