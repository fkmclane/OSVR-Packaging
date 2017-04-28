#!/bin/sh
get() {
	git clone "$2" "$1"

	ver="$((git -C "$1" describe 2>/dev/null || git -C "$1" describe --tags 2>/dev/null || echo "0.0-$(git -C "$1" log --oneline | wc -l)-$(git -C "$1" describe --always)") | sed -e 's/^v//')"

	for file in $(find "$1" -name ".git*"); do
		rm -rf "$file"
	done

	name="$1-$ver"

	mv "$1" "$name"

	tar czf "$name".tar.gz "$name"

	rm -rf "$name"
}

rm -f *.tar.gz

get libfunctionality https://github.com/OSVR/libfunctionality
get osvr-config https://github.com/OSVR/OSVR-Config
get osvr-core https://github.com/OSVR/OSVR-Core
get osvr-cpi https://github.com/ChristophHaag/OSVR-CPI
get osvr-display https://github.com/OSVR/OSVR-Display
get osvr-udev https://aur.archlinux.org/osvr-udev.git
get osvr-openhmd https://github.com/simlrh/OSVR-OpenHMD
get osvr-rendermanager https://github.com/sensics/OSVR-RenderManager
get osvr-tracker-viewer https://github.com/OSVR/OSVR-Tracker-Viewer
get osvr-leap-motion https://github.com/OSVR/OSVR-Leap-Motion
get osvr-oculus-rift https://github.com/OSVR/OSVR-Oculus-Rift
get osvr-steamvr https://github.com/OSVR/SteamVR-OSVR
get osvr-vive https://github.com/OSVR/OSVR-Vive
