#
# Regular cron jobs for the osvr-rendermanager package
#
0 4	* * *	root	[ -x /usr/bin/osvr-rendermanager_maintenance ] && /usr/bin/osvr-rendermanager_maintenance
