# Requirments
You need python 3 installed, for centos run

```bash
yum install python3 -y
```

If you run the script with nrpe you will need to add the podman command to sudoers (as only root/admin is allowed to run the command)
```bash
cat <<EOF >> /etc/sudoers.d/icinga
icinga ALL=NOPASSWD: /usr/bin/podman stats --all --no-stream --format json
icinga ALL=NOPASSWD: /usr/bin/podman ps -a --format json --sort=names
icinga ALL=NOPASSWD: /usr/bin/podman inspect --format *

EOF
```
