#!/usr/bin/python
# reversed napi 0.16.3.1
#
# by gim,krzynio,dosiu,hash 2oo8.
#
# 
#
# last modified: 6-I-2oo8
#
# 4pc0h f0rc3
#
# do dzialania potrzebny jest p7zip-full (tak sie nazywa paczka w debianie)
#
# POZDRAWIAMY NASZYCH FANOW!

import hashlib,sys,urllib.request,os

def f(z):
	idx = [ 0xe, 0x3,  0x6, 0x8, 0x2 ]
	mul = [   2,   2,    5,   4,   3 ]
	add = [   0, 0xd, 0x10, 0xb, 0x5 ]

	b = []
	for i in range(len(idx)):
		a = add[i]
		m = mul[i]
		i = idx[i]

		t = a + int(z[i], 16)
		v = int(z[t:t+2], 16)
		b.append( ("%x" % (v*m))[-1] )

	return ''.join(b)
proxy_url = "localhost:8888"
proxy_support = urllib.request.ProxyHandler({'http': proxy_url})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

d = hashlib.md5();
d.update(open(sys.argv[1],'rb').read(10485760))

str = "http://napiprojekt.pl/unit_napisy/dl.php?l=PL&f="+d.hexdigest()+"&t="+f(d.hexdigest())+"&v=other&kolejka=false&nick=&pass=&napios=posix"
print(str)
open("napisy.7z","w").write(urllib.request.urlopen(str).read())
