>>> def find(a,b,neighbours):             #βρησκω τους γειτονες..
	neighbours=[]
	if a!=0 and b!=0 and a!=9 and b!=9:
		neighbours.append(a+1,b)
		neighbours.append(a-1,b)
		neighbours.append(a,b+1)
		neighbours.append(a,b-1)
	elif a==0 and b==0:
		neighbours.append(a+1,b)
		neighbours.append(a,b+1)
	elif a==0 and b==9:
		neighbours.append(a+1,b)
		neighbours.append(a,b-1)
	elif a==9 and b==0:
		neighbours.append(a-1,b)
		neighbours.append(a,b+1)
	elif a==9 and b==9:
		neighbours.append(a-1,b)
		neighbours.append(a,b-1)
	elif a==0:
		neighbours.append(a+1,b)
		neighbours.append(a,b+1)
		neighbours.append(a,b-1)
	elif b==0:
		neighbours.append(a-1,b)
		neighbours.append(a+1,b)
		neighbours.append(a,b+1)
	elif a==9:
		neighbours.append(a-1,b)
		neighbours.append(a,b+1)
		neighbours.append(a,b-1)
	elif b==9:
		neighbours.append(a-1,b)
		neighbours.append(a+1,b)
		neighbours.append(a,b-1)
	return neighbours

>>> def make_maze(n,start_x,start_y,seed,output_file):
	output_file={}
	seed=[]
	seed[i,j]=start_x,start_y
	s=0
	while s>len(seed.neighbours()):              #Για καθε γειτονα ψαχνει αν εχει καταχωριθει στο γραφο και αν οχι τον εισαγει. 
		if output_file!=seed.neighbours(i):
			output[i]=neighbours[i]
		i=i+1
	if n==0:
		return output_file
	else:
		make_maze1=make_maze(n-1,i+1,j+1,seed,output_file) 
		
		
		# προσπαθησα να κανω μια αναδρομη,νομιζω δεν ειναι σωστο που αλλαζω τα i,j μεσα στην κληση,
		ομως δεν ηξερα πως αλλιως να το κανω να αλλαζει για να προχωραει στο γραφο...:(
