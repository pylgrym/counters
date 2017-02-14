import memcache
import sys

key='defkey'
if len(sys.argv) > 1:
	key = sys.argv[1]
#mc_addr = '127.0.0.1:11211'
#mc_addr = 'wd-lin-apache-prod2.valhalla.local:11211'
mc_addr = 'lmp-dev.valhalla.local:11211'
mc = memcache.Client( [mc_addr ], debug=1)

def incrsafe(key): # check if exists - create if it doesn't.
	if mc.get(key) == None:
		mc.set(key,'0')
	val = mc.incr(key)
	return val
	#print( 'incr mckey %s to %s' % (key, val) )

print('(will create key if missing)')
a=incrsafe(key)
print( 'incr mckey %s to %s' % (key, a) )
