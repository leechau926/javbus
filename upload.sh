#!/bin/bash

for item in $(ls *.jpg)
do
    rclone copy $item wlyn:adult --log-file ./upload.log
    echo "${item} upload completed!"
done
