#!/bin/bash

message=$1
if [[ -z "${message}" ]]; then
    echo "提交信息不能为空"
    exit 0
fi


git add *
git commit -m "更新榜单 - $message"
git pull
# git push