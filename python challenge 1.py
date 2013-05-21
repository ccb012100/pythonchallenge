def challenge_1():
	msg = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
	decmsg = ""
	for c in msg:
		if c == 'y':
			decmsg += 'a'
		elif c == 'z':
			decmsg += 'b'
		elif c != '.' and c!= "'" and c!= '.' and c!= ' ' and c != '(' and c!= ')':
			decmsg += chr(ord(c) + 2)
		else:
			decmsg += c
	print decmsg

intab = "yzabcdefghijklmnopqrstuvwx"
outtab = "abcdefghijklmnopqrstuvwxyz"
trantab = string.maketrans(intab, outtab)

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print str.translate(trantab);