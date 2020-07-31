'''Value Iteration Algorithm'''
import copy
N,M = raw_input().split()
M = int(M)
N = int(N)

reward = [[0 for j in range(M)] for i in range(N)]
reward_states =[]
for i in range(N):
	reward[i]=raw_input().split()
	reward[i]=map(float,reward[i])
	for j in range(M):
		if reward[i][j]==0:
			reward_states.append([i,j])


E,W = raw_input().split()
E = int(E)
W = int(W)

end_states = [[0 for j in range(2)] for i in range(E)]
for i in range(E):
	end_states[i]=raw_input().split()
	end_states[i]=map(int,end_states[i])

wall_states = [[0 for j in range(2)] for i in range(W)]
for i in range(W):
	wall_states[i]=raw_input().split()
	wall_states[i]=map(int,wall_states[i])

#append edges to wall_states
for i in range(0,N):
	wall_states.append([i,-1])
	wall_states.append([i,M])
for i in range(0,M):
	wall_states.append([-1,i])
	wall_states.append([N,i])

start_state=[0,0]
start_state=raw_input().split()
start_state=map(int,start_state)

unit_step_reward = raw_input()
unit_step_reward = float(unit_step_reward)


policy = [['-' for i in range(M)] for j in range(N)]
prev_utility = copy.deepcopy(reward)
curr_utility = copy.deepcopy(reward)
max_utility = -200000.00
r = 0.99
e = 0.01
delta = 0
ite = 0
print "\n"
#value iteration algorithm
while True:
	prev_utility = copy.deepcopy(curr_utility)
	curr_utility = copy.deepcopy(reward)
	delta = 0
	ite = ite + 1
	print "ITERATION ",
	print ite
	print "\n"
	for i in range(N):
		for j in range(M):
			if [i,j] not in end_states and [i,j] not in wall_states:
				max_utility = -200000.00
				a,b,c,d = 0,0,0,0
				if [i,j+1] in wall_states:
					a = 1
				if [i,j-1] in wall_states:
					b = 1
				if [i+1,j] in wall_states:
					c = 1
				if [i-1,j] in wall_states:
					d = 1

				#East
				u = 0
				if a==0:
					u += round(0.8 * prev_utility[i][j+1],3)
				else:
					u += round(0.8 * prev_utility[i][j],3)
				if d==0:
					u += round(0.1 * prev_utility[i-1][j],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if c==0:
					u += round(0.1 * prev_utility[i+1][j],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if u>max_utility:
					max_utility = round( u,3)
				
				#West
				u = 0
				if b==0:
					u += round(0.8 * prev_utility[i][j-1],3)
				else:
					u += round(0.8 * prev_utility[i][j],3)
				if d==0:
					u += round(0.1 * prev_utility[i-1][j],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if c==0:
					u += round(0.1 * prev_utility[i+1][j],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if u>max_utility:
					max_utility = round(u,3)

				#North
				u = 0
				if d==0:
					u +=round( 0.8 * prev_utility[i-1][j],3)
				else:
					u += round(0.8 * prev_utility[i][j],3)
				if a==0:
					u += round(0.1 * prev_utility[i][j+1],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if b==0:
					u += round(0.1 * prev_utility[i][j-1],3)
				else:
					u +=round( 0.1 * prev_utility[i][j],3)
				if u>max_utility:
					max_utility = round(u,3)

				#South
				u = 0
				if c==0:
					u += round(0.8 * prev_utility[i+1][j],3)
				else:
					u += round(0.8 * prev_utility[i][j],3)
				if a==0:
					u += round(0.1 * prev_utility[i][j+1],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if b==0:
					u += round(0.1 * prev_utility[i][j-1],3)
				else:
					u += round(0.1 * prev_utility[i][j],3)
				if u > max_utility:
					max_utility = round(u,3)
				curr_utility[i][j]= round(r*max_utility + unit_step_reward + reward[i][j],3)
				#print delta,
				#print curr_utility[i][j]-prev_utility[i][j]
				if delta < (curr_utility[i][j]-prev_utility[i][j]):
					delta = copy.deepcopy(curr_utility[i][j]-prev_utility[i][j])

			print curr_utility[i][j],
		print "\n"
	print "\n"
	if r!=1 and delta < e*(1-r)/r:
		break
	if r==1 and delta < 0.0001:
		break



p = '-'
prev_utility = copy.deepcopy(curr_utility)
print "POLICY:",
print "\n"
for i in range(N):
	for j in range(M):
		p = '-'
		if [i,j] not in end_states and [i,j] not in wall_states:
			max_utility = -200000.00
			a,b,c,d = 0,0,0,0
			if [i,j+1] in wall_states:
				a = 1
			if [i,j-1] in wall_states:
				b = 1
			if [i+1,j] in wall_states:
				c = 1
			if [i-1,j] in wall_states:
				d = 1

			#East
			u = 0
			if a==0:
				u += round(0.8 * prev_utility[i][j+1],3)
			else:
				u += round(0.8 * prev_utility[i][j],3)
			if d==0:
				u += round(0.1 * prev_utility[i-1][j],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if c==0:
				u += round(0.1 * prev_utility[i+1][j],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if u>max_utility:
				p = 'E'
				max_utility = round( u,3)
			
			#West
			u = 0
			if b==0:
				u += round(0.8 * prev_utility[i][j-1],3)
			else:
				u += round(0.8 * prev_utility[i][j],3)
			if d==0:
				u += round(0.1 * prev_utility[i-1][j],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if c==0:
				u += round(0.1 * prev_utility[i+1][j],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if u>max_utility:
				p = 'W'
				max_utility = round(u,3)

			#North
			u = 0
			if d==0:
				u +=round( 0.8 * prev_utility[i-1][j],3)
			else:
				u += round(0.8 * prev_utility[i][j],3)
			if a==0:
				u += round(0.1 * prev_utility[i][j+1],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if b==0:
				u += round(0.1 * prev_utility[i][j-1],3)
			else:
				u +=round( 0.1 * prev_utility[i][j],3)
			if u>max_utility:
				p = 'N'
				max_utility = round(u,3)

			#South
			u = 0
			if c==0:
				u += round(0.8 * prev_utility[i+1][j],3)
			else:
				u += round(0.8 * prev_utility[i][j],3)
			if a==0:
				u += round(0.1 * prev_utility[i][j+1],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if b==0:
				u += round(0.1 * prev_utility[i][j-1],3)
			else:
				u += round(0.1 * prev_utility[i][j],3)
			if u > max_utility:
				p = 'S'
				max_utility = round(u,3)
			policy[i][j]=p
		print policy[i][j],
	print "\n"
print "\n"