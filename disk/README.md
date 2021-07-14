# sudoers.d
You want to add the following values to your sudoers to allow the smart check to be performed.

```
icinga ALL=NOPASSWD:  /usr/lib64/nagios/plugins/check_ide_smart -q -d *
```