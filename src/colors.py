def icr(i: float):
	return [0, 255, round(i)][(i >= 0) + (i < 256)]

def cr(c: tuple):
	return tuple([icr(x) for x in c])


def mix(*args):
	assert all([isinstance(x, tuple) for x in args])
	assert len(args) >= 2
	assert all([len(x) is 3 for x in args])
	if len(args) > 2:
		return mix(mix(*args[:2]), *args[2:])
	elif len(args) is 2:
		return cr([x + y for x, y in zip(args[0], args[1])])
	else:
		return args


def sc(c: tuple, f: float):
	return cr([x * f for x in c])


def mult(c1: tuple, c2: tuple):
	return cr([x * y for x, y in zip(c1, c2)])


colors = [(0, 0, 0)] * 256
br = (255, 0, 0)
bg = (0, 255, 0)
bb = (0, 0, 255)


def initColors():
	#
	for n in range(216):
		x = sc(br, 1 / 6 * (n % 6))
		y = sc(bg, 1 / 6 * ((n % 36) // 6))
		z = sc(bb, 1 / 6 * (n // 36))
		colors[16 + n] = mix(x, y, z)


def printcolordemo(c: tuple):
	assert isinstance(c, (tuple, list))
	print('\x1b[48;2;{0};{1};{2}m{3}\x1b[0m'.format(*c, '  '), end='')


def minichart():
	#
	for n in range(16, 232):
		printcolordemo(colors[n])
		if (n - 16) % 36 is 35:
			print()


initColors()
