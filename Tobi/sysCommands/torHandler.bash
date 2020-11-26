#!/bin/bash

echo "owner /{dev,run}/shm/org.mozzila.*.* rw,"  >> /etc/apparmor.d/local/torbrowser.Browser.firefox && sudo systemctl restart apparmor 


