
# check_backend_health
Checks if varnish believe the backend is healthy (good to use) or sick. Depends on you using the inbuilt probes function for your backend. Can return statistics to Nagios/OP5 how the last probes in the window have gone. Example below on how to test your backed named video.

> ./check_backend_health -b video -s
