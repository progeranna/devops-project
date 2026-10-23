#!/bin/bash
VERSION=1.0
REGISTRY=localhost:5000

docker compose build

docker tag shop-backend $REGISTRY/shop-backend:$VERSION
docker tag shop-frontend $REGISTRY/shop-frontend:$VERSION

docker push $REGISTRY/shop-backend:$VERSION
docker push $REGISTRY/shop-frontend:$VERSION
