import memcache

mc = memcache.client( ['127.0.0.1:11211'], debug=1)

print( 'set', mc.set('mykey', '1') )
print( 'incr', mc.incr('mykey') )
print( 'get', mc.get('mykey') )
