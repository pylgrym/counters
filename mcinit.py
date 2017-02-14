import memcache
import sys

key='defkey'
if len(sys.argv) > 1:
	key = sys.argv[1]
#mc_addr = '127.0.0.1:11211'
#mc_addr = 'wd-lin-apache-prod2.valhalla.local:11211'
mc_addr = 'lmp-dev.valhalla.local:11211'
mc = memcache.Client( [mc_addr ], debug=1)

print('initing mckey: %s to 0' % key)
print( 'set',  mc.set(key, '0') )
