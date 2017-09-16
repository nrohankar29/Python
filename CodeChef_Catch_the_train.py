def Catch_the_train(Ve,Vy,L,T):
	t = L/Ve
    
	t_esc_walk = L/(Ve+Vy)
	
	p = (t-t_esc_walk)/T
	
	if p < 1.0:
	
		return p
		
	elif p >= 1.0:
	
		return 1.0
		


Tc = int(input().strip())

for i in range(Tc):

	Ve = int(input().strip())
	Vy = int(input().strip())
	L = int(input().strip())
	T = int(input().strip())
	
	print(Catch_the_train(Ve,Vy,L,T))