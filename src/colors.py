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
	colors[0x0], colors[0x8] = (0x00, 0x00, 0x00), (0x80, 0x80, 0x80)
	colors[0x1], colors[0x9] = (0xc0, 0x00, 0x00), (0xff, 0x00, 0x00)
	colors[0x2], colors[0xa] = (0x00, 0xc0, 0x00), (0x00, 0xff, 0x00)
	colors[0x3], colors[0xb] = (0xc0, 0xa0, 0x00), (0xff, 0xff, 0x00)
	colors[0x4], colors[0xc] = (0x00, 0x00, 0xc0), (0x00, 0x00, 0xff)
	colors[0x5], colors[0xd] = (0xc0, 0x00, 0xc0), (0xff, 0x00, 0xff)
	colors[0x6], colors[0xe] = (0x00, 0xc0, 0xc0), (0x00, 0xff, 0xff)
	colors[0x7], colors[0xf] = (0xc0, 0xc0, 0xc0), (0xff, 0xff, 0xff)
	for n in range(216):
		x = sc(br, 1 / 5 * (n // 36))
		# x = sc(bb, 1 / 6 * (n % 6))
		y = sc(bg, 1 / 5 * ((n % 36) // 6))
		# z = sc(br, 1 / 6 * (n // 36))
		z = sc(bb, 1 / 5 * (n % 6))
		colors[16 + n] = mix(x, y, z)
	for n in range(24):
		colors[232 + n] = sc((255, 255, 255), n / 24)


def printcolordemo(c: tuple):
	assert isinstance(c, (tuple, list, int))
	if isinstance(c, int):
		assert c < 256 and c >= 0
		print('\x1b[48;5;{1}m{0}\x1b[0m'.format('  ', c), end='')
	else:
		print('\x1b[48;2;{1};{2};{3}m{0}\x1b[0m'.format('  ', *c), end='')


def minichart(builtin=False):
	if builtin:
		for n in range(16):
			printcolordemo(n)
			if n % 8 is 7:
				print()
		for n in range(16, 232):
			printcolordemo(n)
			if (n - 16) % 36 is 35:
				print()
		for n in range(232, 256):
			printcolordemo(n)
		print()
	else:
		for n in range(16):
			printcolordemo(colors[n])
			if n % 8 is 7:
				print()
		for n in range(16, 232):
			printcolordemo(colors[n])
			if (n - 16) % 36 is 35:
				print()
		for n in range(232, 256):
			printcolordemo(colors[n])
		print()


initColors()
