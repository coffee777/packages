%include /usr/share/spin-kickstarts/fedora-livecd-desktop.ks

repo --name=rpmfusion-free --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
repo --name=rpmfusion-free-updates --mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-updates-released-$releasever&arch=$basearch
repo --name=google-chrome --baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch

rootpw --iscrypted $6$Gy7TJjee52fs$zAES8PyxmHVqEnjBvNnEw5XWINhDRx.6PEXPLZ0ZVKxeKKYjpth8wfbQIN3LY7RwZyU87q6Z/tyUMmGqpMnuH0
authconfig --enableshadow --passalgo=sha512

%packages --instLangs=en_GB:th_TH
@thai-support
gstreamer-plugins-ugly
gstreamer-ffmpeg
gdouros-symbola-fonts
google-chrome-stable
-PackageKit-command-not-found
-PackageKit-gtk3-module
-gnome-games
-gnome-mplayer
-deja-dup
-aisleriot
-sound-juicer
-fedora-release-notes
-abrt*
-setroubleshoot*
-yelp
-firefox
-xulrunner
-evolution
%end
