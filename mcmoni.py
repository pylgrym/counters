import memcache
import sys
import time

key='defkey'
if len(sys.argv) > 1:
	key = sys.argv[1]
#mc_addr = '127.0.0.1:11211'
#mc_addr = 'wd-lin-apache-prod2.valhalla.local:11211'
mc_addr = 'lmp-dev.valhalla.local:11211'
mc = memcache.Client( [mc_addr ], debug=1)

while 1:
  print( 'moni %s: %s' % (key, mc.get(key)) )
  time.sleep(1)
