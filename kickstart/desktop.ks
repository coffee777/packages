%include /usr/share/spin-kickstarts/fedora-live-desktop.ks

keyboard uk
lang en_GB
timezone --utc Europe/London

repo --name=rpmfusion-free --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
repo --name=rpmfusion-free-updates --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-$releasever&arch=$basearch
repo --name=remix --baseurl=http://dl.dropbox.com/u/2682668/fedora-remix/$releasever/$basearch/

%packages
-@office
-PackageKit-command-not-found
-gnome-games
-deja-dup
-aisleriot
-sound-juicer
-fedora-release-notes

gstreamer-plugins-ugly
gstreamer-ffmpeg

discount
xclip
inotify-tools
source-highlight
nginx
mpd
mpc

nano
hexedit
mutt
newsbeuter
ncmpc
weechat
htop

lua
git

strace
valgrind
gcc
qemu
man-pages

httpd-tools
GraphicsMagick
optipng
libjpeg-turbo-utils
advancecomp

%end
