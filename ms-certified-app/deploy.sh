#!/bin/zsh

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 704325809072.dkr.ecr.ap-northeast-1.amazonaws.com

docker build -t ms-certified-app .

docker tag ms-certified-app:latest 704325809072.dkr.ecr.ap-northeast-1.amazonaws.com/ms-certified-app:latest

docker push 704325809072.dkr.ecr.ap-northeast-1.amazonaws.com/ms-certified-app:latest
