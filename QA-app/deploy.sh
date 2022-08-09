#!/bin/zsh

aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 704325809072.dkr.ecr.ap-northeast-1.amazonaws.com


docker build -t sc900-qa-app .


docker tag sc900-qa-app:latest 704325809072.dkr.ecr.ap-northeast-1.amazonaws.com/sc900-qa-app:latest


docker push 704325809072.dkr.ecr.ap-northeast-1.amazonaws.com/sc900-qa-app:latest
