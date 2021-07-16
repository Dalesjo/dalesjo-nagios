To make system/check_failed/logins work with nrpe you must add a sudo command for the user (username nrpe in Centos 7). Add the following _/etc/sudoers.d/nrpe_

```
icinga ALL=NOPASSWD: /usr/bin/journalctl -q -t sshd --since 24 hours ago
```

You can test it by running.

`sudo -u ìcinga /usr/lib64/nagios/plugins/custom/system/check_failed_logins -d 24 -w 100 -c 200`

If you want to check more than 24 hours back in time you need to change your sudoers file otherwise check_failed_logins will ask for nrpes password.
