%include desktop.ks

keyboard uk
lang en_GB.UTF-8
timezone --utc Europe/London

repo --name=remix --baseurl=http://dl.dropbox.com/u/2682668/fedora-remix/$releasever/$basearch/

%packages --instLangs=en_GB:th_TH

@thai-support

# GUI
vim-X11
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
webkitgtk3-doc
meld
gmpc

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
