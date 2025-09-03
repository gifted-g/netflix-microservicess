# Netflix-Scale Microservices Simulation (MVP)

A small microservices playground with auth, video, recommendation services and an API gateway.

## Services
- auth-service (Flask) -> /login (returns JWT stub)
- video-service (Flask) -> /stream (mock)
- recommendation-service (Flask) -> /recommend
- api-gateway (NGINX) -> reverse proxy to services

## Quick start (Docker Compose)
docker-compose up --build
