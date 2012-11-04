%include include/desktop.ks

keyboard uk
lang en_GB
timezone --utc Europe/London

repo --name=remix --baseurl=http://dl.dropbox.com/u/2682668/fedora-remix/$releasever/$basearch/

%packages

# GNOME
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
gmpc

# Curses
nano
hexedit
mutt
ncmpc
weechat
htop
tig
nload

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
rlwrap
tree

# Services
nginx
privoxy
mpd

# Development
gcc
gdb
make
git
lua
man-pages
qemu
strace
valgrind

# Other
words

# Totem requires libzeitgeist/tracker, Brasero requires tracker
mplayer
-brasero*
-totem*
-tracker*
-zeitgeist*
-libzeitgeist*

%end
