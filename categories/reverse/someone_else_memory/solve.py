a = 'C3 CF C4 C5 C2 D9 FB D3 B0 ED E5 EF EE C5 DF E5 EC A4 E5 DF F3 DF ED B2 ED EF F2 D9 DF B1 F3 DF F3 F7 E5 B2 F4 DF C0 F3 DF E8 CF EE B2 F9 FD'.split()
b = [int(i, 16) for i in a]
for i in b:
	print(chr(i-128), end='')