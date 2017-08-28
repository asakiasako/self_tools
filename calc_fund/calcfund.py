
def calcfund(a,b,c,d,e,f,g,h,i,j):
	p_sz50 = float(a)
	p_cyb = float(b)
	p_mg = float(c)
	p_zqa = float(d)
	p_zqb = float(e)
	sz50 = float(f)
	cyb = float(g)
	mg = float(h)
	zqa = float(i)
	zqb = float(j)
	
	total = sz50 + cyb + mg + zqa + zqb + 400*4
	per = [p_sz50, p_cyb, p_mg, p_zqa, p_zqb]
	fund = [sz50, cyb, mg, zqa, zqb]
	fund_zip = zip(per, fund)
	rtn = []
	for x, y in fund_zip:
		foo = (x*total - y)/4
		foo = round(foo*1000)/1000
		rtn.append(foo)
	return rtn

if __name__ == "__main__":
	(a,b,c,d,e) = (0.14,0.14,0.14,0.27,0.31)
	print("Insert: sz50, cyb, nsdc100, bp500, bp100, zqa, zqb")
	var = input("> ")
	var = var.split()
	var0 = []
	for i in var:
		var0.append(float(i))
	var = var0
	sz50 = var[0]
	cyb = var[1]
	mg = var[2]+var[3]+var[4]
	zqa = var[5]
	zqb = var[6]
	print(calcfund(a,b,c,d,e,sz50, cyb, mg, zqa, zqb))
	