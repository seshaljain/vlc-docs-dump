natalya.videolan.org:

{\| class="wikitable" -\| kvm-builder-1 \|\| none \|\| launches docker
containers for jenkins kvm-builder-2 \|\| none \|\| launches docker
containers for jenkins kvm-builder-3 \|\| none \|\| launches docker
containers for jenkins kvm-builder-4 \|\| none \|\| launches docker
containers for jenkins kvm-builder-5 \|\| none \|\| launches docker
containers for jenkins freebsd10-builder-1 \|\| none \|\| jenkins build
slave oddjob.videolan.org \|\| http://oddjob.videolan.org/~$username/,
ssh -l $username -p 20024 oddjob.videolan.org \|\| Developers
playground, Debian unstable, ask thresh for an account \|}

{\| class="wikitable" -\| docker-registry|\|
https://registry.videolan.org:5000/v2/_catalog \|\| stores docker images
for jenkins github-mirror \|\| none \|\| mirrors some repositories to
github jenkins-master \|\| https://jenkins.videolan.org/ \|\| jenkins
master libav-fate \|\| none \|\| libav fate slave nightlies-ftp \|\|
http://nightlies.videolan.org \|\| holds nightly binaries / contribs
proxy \|\| none \|\| holds a web proxy to selected kvm/lxc machines
rsync-status-check \|\| none \|\| ftp cron job checks streams \|\|
http://streams.videolan.org, ssh -4 -l videolan natalya.videolan.org -p
20025 \|\| holds samples, uploads \|}

[[Category:Roots]]
