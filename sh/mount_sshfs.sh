#!/bin/sh
umount -f mount_point
sshfs eisuke@192.168.0.82:/home/eisuke mount_point
