%include /usr/share/spin-kickstarts/fedora-livecd-desktop.ks

keyboard uk
lang en_GB
timezone --utc Europe/London

repo --name=rpmfusion-free --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
repo --name=rpmfusion-free-updates --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-$releasever&arch=$basearch
repo --name=remix --baseurl=http://dl.dropbox.com/u/2682668/fedora-remix/$releasever/$basearch/


%packages

# Remix
discount
gnome-extra
nginx

# Fedora
fedora-packager
spin-kickstarts
livecd-tools
yum-plugin-fastestmirror

# RPM Fusion
gstreamer-plugins-ugly
gstreamer-ffmpeg

# Network Utilities
nmap
whois
wget
wol

# Command-line
lua
git
gitk
nano
file-libs
bash-completion
yajl
strace
valgrind
gcc
qemu
inotify-tools
man-pages
source-highlight
words
hunspell-en
xclip
httpd-tools
openssl-devel
GraphicsMagick
optipng
libjpeg-turbo-utils
advancecomp
pngnq

%end
