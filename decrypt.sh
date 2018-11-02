#!/bin/sh

uid=$(cat /etc/machine-id)

device=/dev/mapper/cinder--volumes-miloud

key=$(curl -su 'admin' "http://keyserver_url:5000/getkey/$uid" | jq -r '.key')

echo $key | cryptsetup luksOpen $device encrypted

mount /dev/mapper/encrypted /mnt
