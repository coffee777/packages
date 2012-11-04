%include desktop.ks

keyboard us
lang th_TH.UTF-8
timezone --utc Asia/Bangkok

%packages --instLangs=th_TH:en_GB:en_US
@thai-support
hunspell-th
%end
