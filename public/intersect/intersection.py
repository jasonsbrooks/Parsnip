<<<<<<< HEAD
def intersection2c(p0, p1):
	[x0, y0, r0] = p0
	[x1, y1, r1] = p1
	dx = x1 - x0;
	dy = y1 - y0;
	d = ((x1 - x0)**2 + (y1 - y0)**2)**.5;
	if (d > (r0 + r1)):
		# no solution. circles do not intersect.
		return False

	if (d < abs(r0 - r1)):
		# no solution. one circle is contained in the other
		return False

	a = ((r0*r0) - (r1*r1) + (d*d)) / (2.0 * d) ;

	x2 = x0 + (dx * a/d);
	y2 = y0 + (dy * a/d);

	h = ((r0*r0) - (a*a))**.5;

	rx = -dy * (h/d);
	ry = dx * (h/d);

	xi = x2 + rx;
	xi_prime = x2 - rx;
	yi = y2 + ry;
	yi_prime = y2 - ry;

	return [[xi, yi], [xi_prime, yi_prime]];

def intersection3c(p0, p1, pf):
	res = intersection2c(p0, p1)
	if res:
		err0 = abs(((res[0][0] - pf[0])**2 + (res[0][1] - pf[1])**2)**.5 - pf[2]);
		err1 = abs(((res[1][0] - pf[0])**2 + (res[1][1] - pf[1])**2)**.5 - pf[2])
		if err0 < err1:
			return res[0]
		else:
			return res[1]
	else:
		return False

def intersection(ptdists):
	# Takes a list of [x,y,r] lists and returns the most likely [x,y] location of the user.
	for x in ptdists:
		try:
			if len(x) != 3:
				return False
		except:
			return False
	if len(ptdists) < 1:
		return False
	if len(ptdists) == 1:
		return ptdists[0][0:2]
	if len(ptdists) == 2:
		return intersection2c(ptdists[0], ptdists[1])[0]
	else:
		ptdists = sorted(ptdists, key=lambda x:x[2])[0:3]
		return intersection3c(ptdists[0], ptdists[1], ptdists[2])

## Bad usage
print intersection([2,0,8])

## Good usage
print intersection([[2,0,8]])
print intersection([[2,0,8],[10,0,5]])
print intersection([[2,0,8],[10,0,5],[5,5,5],[100,100,1000]])
