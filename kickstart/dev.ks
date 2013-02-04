%include desktop.ks

keyboard uk
lang en_GB.UTF-8
timezone --utc Europe/London

repo --name=remix --baseurl=http://dl.dropbox.com/u/2682668/fedora-remix/$releasever/$basearch/

%packages --instLangs=en_GB:th_TH

@thai-support

# GUI
inkscape
gimp
blender
gedit-plugins
nautilus-open-terminal
dconf-editor
emerillon
devhelp
gtk3-devel-docs
webkitgtk3-doc
meld
gmpc
-brasero

# Curses
nano
vim-enhanced
hexedit
mutt
ncmpc
weechat
htop
tig
nload
pinfo

# Command-line
mpc
xclip
optipng
libjpeg-turbo-utils
advancecomp
GraphicsMagick
discount
source-highlight
inotify-tools
httpd-tools
android-tools
cclive
rlwrap
tree
units

# Services
nginx
privoxy
mpd

# Development
gcc
gdb
make
git
man-pages
qemu
strace
valgrind

# Lua
lua
luarocks
lua-filesystem
lua-socket
lua-lpeg
lua-lgi
lua-json
lua-copas
lua-wsapi
lua-posix

# Other
words

%end
