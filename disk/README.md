# sudoers.d
You want to add the following values to your sudoers to allow the smart check to be performed.

```
icinga ALL=NOPASSWD:  /usr/lib64/nagios/plugins/check_ide_smart -q -d *
icinga ALL=NOPASSWD: /home/icinga/bin/disk/check_smart.pl -q -i auto -d /dev/*
```


# check_smart.pl
Downloaded from [Napsty](https://github.com/Napsty/check_smart) 2021-07-16