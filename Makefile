# Makefile

# Build the Docker image
build:
	@echo "Building Docker image..."
	docker-compose build

# Start the containers
start:
	@echo "Starting containers..."
	docker-compose up -d

# Stop the containers
stop:
	@echo "Stopping containers..."
	docker-compose down

# View logs of running containers
logs:
	@echo "Fetching logs..."
	docker-compose logs -f

# Remove containers, networks, images, and volumes
clean:
	@echo "Cleaning up..."
	docker-compose down --rmi all -v

# Open a shell inside the container
shell:
	@echo "Opening shell..."
	docker-compose exec web /bin/bash

.PHONY: build start stop logs clean shell
