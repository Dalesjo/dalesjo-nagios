
# check_backend_health
Checks if varnish believe the backend is healthy (good to use) or sick. Depends on you using the inbuilt probes function for your backend. Can return statistics to Nagios/OP5 how the last probes in the window have gone. Example below on how to test your backed named video.

> ./check_backend_health -b video -s

# check_hit_ration
Checks how many percentage of all requests that are hits against your cache. the example below returns critical error if 50% or your hits is not cached.

> ./check_hit_ration -w 80 -c 50 -s"

# check_storage_utilization
Checks how much of your storage is used for cache. Cache name depends on your startup variables in varnish. a malloc cache has the prefix SMA. a file cache has a prefix om SMF. The example below will return a critical error if more than 90% of the cache is used.

> ./check_storage_utilization -S SMF.play -w 80 -c 90 -s
