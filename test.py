import os
cmd = "python3 enhance.py --type=photo --model=repair --zoom=1 "
for i in range(2,58):
	file = str(i)+".jpg"
	os.system(cmd+file)
