%include /usr/share/spin-kickstarts/fedora-live-desktop.ks

keyboard uk
lang en_GB
timezone --utc Europe/London

repo --name=rpmfusion-free --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
repo --name=rpmfusion-free-updates --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-$releasever&arch=$basearch
repo --name=remix --baseurl=http://dl.dropbox.com/u/2682668/fedora-remix/$releasever/$basearch/

%packages

# Junk
-@office
-PackageKit-command-not-found
-PackageKit-gtk3-module
-gnome-games
-deja-dup
-aisleriot
-sound-juicer
-fedora-release-notes

# GNOME
epiphany
epiphany-extensions
luakit
inkscape
gimp
blender
gedit-plugins
nautilus-open-terminal
dconf-editor
emerillon
devhelp
gtk3-devel-docs
meld
gstreamer-plugins-ugly
gstreamer-ffmpeg

# Curses
nano
hexedit
mutt
ncmpc
weechat
htop

# Command-line
mpc
xclip
optipng
libjpeg-turbo-utils
advancecomp
GraphicsMagick
discount
inotify-tools
source-highlight
httpd-tools
cclive

# Services
nginx
privoxy
mpd

# Development
lua
git
gcc
man-pages
qemu
strace
valgrind

%end
