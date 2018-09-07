from sys import argv
import re
import os
import string

def launch_clingo(input_files, output_file):
    input_args = ' '.join(input_files)
    command = "clingo 0 %s >%s" % (input_args, output_file)
    os.system(command)

def conversion(input, output):
    RE_ANSWER = re.compile('Answer:\s*(?P<answer>[0-9]+)')
    stop=False
    with open(input, 'r') as file:
        with open(output, 'w' )as output:
            answer = 0
            for line in file.readlines():
                new_answer = re.search(RE_ANSWER, line)
                if new_answer:
                    answer = new_answer.group('answer')
                elif 'SATISFIABLE' in line:
                    stop=True
                elif not stop:
                    line = re.sub('simName', 's(%s)' % answer, line)
                    line = re.sub('\s\s*', '.\n', line)
                    output.write("%s" % line)

def translation(input, output):
    RE_ANSWER = re.compile('Answer:\s*(?P<answer>[0-9]+)')
    stop=False
    with open(input, 'r') as file:
		with open(output, 'w')as output:
			answer = 0
			for line in file.readlines():

# Principle of Benefits Vs. Costs
# i(benCosts(s1,S,i1,I,t1,T,n1,N))
				if 'i(benCosts' in line: 
					newline = line.replace('i(benCosts','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					cw = re.search('n1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to the principle of Benefits Vs. Costs because its compared weight is negative"+cw.group(1)) 
# p(benCosts(s1,S,i1,I,t1,T,n1,N))
				elif 'p(benCosts' in line: 
					newline = line.replace('p(benCosts','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					cw = re.search('n1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to the principle of Benefits Vs. Costs because its compared weight is positive:"+cw.group(1)) 

# Act Utilitarianism 
# i(actUti(s1,S1,i1,I1,t1,T,n1,N1,i2,I2,n2,N2))
				elif 'i(actUti' in line: 
					newline = line.replace('i(actUti','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					aw = re.search('n1(.*)i2', newline)
					alternative = re.search('i2(.*)n2', newline)
					aaw = re.search('n2(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to Act Utilitarianism because it does not lead to the best possible outcome. Its best possible outcome has an added weight of"+aw.group(1))
					output.write ("\n The volition"+alternative.group(1))
					output.write ("leads to a better possible outcome, with an added weight of"+aaw.group(1))
# p(actUti(s1,S,i1,I,t1,T,n1,N))
				elif 'p(actUti' in line: 
					newline = line.replace('p(benCosts','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					aw = re.search('n1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to Act Utilitarianism because it can lead to the best possible outcome, whose added weight is:"+aw.group(1)) 

# Principle of Least Bad consequence
# i(leastBad(s1,S,i1,I,t1,T,n1,N))
				elif 'i(leastBad' in line: 
					newline = line.replace('i(leastBad','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					aw = re.search('n1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to the Principle of Least Bad consequence because its worst possible consequence, whose added weight is"+aw.group(1)+"is worse that the worst possible consequence of at least one of its viable alternatives.")
# p(leastBad(s1,S,i1,I,t1,T,n1,N))
				elif 'p(leastBad' in line: 
					newline = line.replace('p(leastBad','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					aw = re.search('n1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to the Principle of Least Bad consequence because its worst possible consequence, whose added weight is"+aw.group(1)+"is the best among the worst possible consequences of its viable alternatives.")

# Prohibiting Purely Bad Volitions 
# i(pureBad(s1,S,i1,I,t1,T))					
				elif 'i(pureBad' in line: 
					newline = line.replace('i(pureBad','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to the rule of Prohibiting Purely Bad volitions because it leads only to negative outcomes.") 
# p(pureBad(s1,S,i1,I,t1,T))										
				elif 'p(pureBad' in line: 
					newline = line.replace('p(pureBad','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to the rule of Prohibiting Purely Bad volitions because it does not lead only to negative outcomes.") 
						
					
# Rule Utilitarianism
# i(ruleUti(s1,S1,i1,I1,t1,T,n1,N1,r1,R1,i2,I2,n2,N2,r2,R2))
				elif 'i(ruleUti' in line: 
					newline = line.replace('i(ruleUti','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					rw1 = re.search('n1(.*)r1', newline)
					rule1 = re.search('r1(.*)i2', newline)
					alternative = re.search('i2(.*)n2', newline)
					rw2 = re.search('n2(.*)r2', newline)
					rule2 = re.search('r2(.*)', newline)					
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to Rule Utilitarianism because it is an instance of the rule"+rule1.group(1))
					output.write ("whose rule weight is"+rw1.group(1))
					output.write ("\n while there exists an alernative volition"+alternative.group(1))					
					output.write ("which belongs to a better rule"+rule2.group(1))
					output.write ("whose rule weight is"+rw2.group(1))
# p(ruleUti(s1,S,i1,I,t1,T,n1,N,r1,R)):-per(ruleUti,S,T,I),instance(I,R),ruleWeight(R,N).
				elif 'p(ruleUti' in line: 
					newline = line.replace('p(ruleUti','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					rw1 = re.search('n1(.*)r1', newline)
					rule1 = re.search('r1(.*)', newline)					
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to Rule Utilitarianism because it is an instance of the rule"+rule1.group(1))
					output.write ("whose rule weight is"+rw1.group(1))

# Codes of Conduct
# i(conduct(s1,S,i1,I,t1,T))
				elif 'i(conduct' in line: 
					newline = line.replace('i(conduct','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to the implemented Code of Conduct, because it infringes it.") 										
# p(conduct(s1,S,i1,I,t1,T)):-per(conduct,S,T,I).
				elif 'p(conduct' in line: 
					newline = line.replace('p(conduct','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to the implemented Code of Conduct, because it does not infringe it.")

# Kantian Ethics
# i(kant(s1,S,i1,I,t1,T,g1,G,e1,E1))
				elif 'i(kant' in line: 
					newline = line.replace('i(kant','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)g1', newline)
					agent = re.search('g1(.*)e1', newline)
					event = re.search('e1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to Kantian ethics because, without aiming for it, it causes event"+event.group(1)) 	
					output.write ("which impacts on agent(s)"+agent.group(1)) 	
# i(kant(s1,S,i1,I,t1,T,g1,G,e1,E,n1,N))
				elif 'i(kant' in line: 
					newline = line.replace('i(kant','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)g1', newline)
					agent = re.search('g1(.*)e1', newline)
					event = re.search('e1(.*)n1', newline)
					weight = re.search('n1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible according to Kantian ethics because it purposefully causes the bad event"+event.group(1)) 	
					output.write ("which impacts on agent(s)"+agent.group(1)) 	
					output.write ("and has a weight of"+weight.group(1)) 	
# p(kant(s1,S,a1,A,t1,T,g1,G,e1,E,n1,N)):-r(S,causes,A,T,E),impact(E,G,M,N),aim(A,E),weight(E,N),N>0,agent(G),action(A).
				elif 'p(kant' in line: 
					newline = line.replace('p(kant','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to the Kantian ethics, because ...!!!!") 	


# Doctrine of Double Effect
# 1. Nature of the Act Condition
# i(dde1(s1,S,i1,I,t1,T,m1,M))
				elif 'i(dde1' in line: 
					newline = line.replace('i(dde1','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')			
					sim = re.search('s1(.*)i1', newline)
					action = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)m1', newline)
					modality = re.search('m1(.*)', newline)
					output.write ("\n \n The action:"+action.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible because it is inherently wrong and violates the nature of the act condition of the dde.")
					output.write ("\n It infringes the modality"+modality.group(1))

# 2. Means-End Condition
# i(dde2_cbcg(s1,S,i1,I,e1,E1,e2,E2,t1,T1))
				elif 'i(dde2_cbcg' in line: 
					newline = line.replace('i(dde2_cbcg','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')					
					sim = re.search('s1(.*)i1', newline)
					action = re.search('i1(.*)e1', newline)
					event1 = re.search('e1(.*)e2', newline)
					event2 = re.search('e2(.*)t1', newline)		
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The action:"+action.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible because it violates the Means End condition of the DDE.") 
					output.write ("\n It causes an undesirable event which itself causes a desirable event.")
					output.write ("\n The caused undesirable event is:"+event1.group(1)) 
					output.write ("\n The caused desirable event is:"+event2.group(1))
				elif 'i(dde2_cbpb' in line: 
					newline = line.replace('i(dde2_cbpb','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					action = re.search('i1(.*)e1', newline)
					event1 = re.search('e1(.*)e2', newline)
					event2 = re.search('e2(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The action:"+action.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible because it violates the Means End condition of the DDE.") 
					output.write ("\n It causes an undesirable event which itself prevents another undesirable event.")
					output.write ("\n The caused undesirable event is:"+event1.group(1)) 
					output.write ("\n The prevented undesirable event is:"+event2.group(1))
				elif 'i(dde2_pgpb' in line: 
					newline = line.replace('i(dde2_pgpb','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					action = re.search('i1(.*)e1', newline)
					event1 = re.search('e1(.*)e2', newline)
					event2 = re.search('e2(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The action:"+action.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible because it violates the Means End condition of the DDE.") 
					output.write ("\n It prevents a desirable event, and as a consequence of this an undesirable event is prevented.")
					output.write ("\n The prevented desirable event is:"+event1.group(1)) 
					output.write ("\n The prevented undesirable event is:"+event2.group(1))			
				elif 'i(dde2_pgcg' in line: 
					newline = line.replace('i(dde2_pgcg','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					action = re.search('i1(.*)e1', newline)
					event1 = re.search('e1(.*)e2', newline)
					event2 = re.search('e2(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The action:"+action.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible because it violates the Means End condition of the DDE.") 
					output.write ("\n It prevents a desirable event, and as a consequence causes another desirable event.")
					output.write ("\n The prevented desirable event is:"+event1.group(1)) 
					output.write ("\n The caused desirable event is:"+event2.group(1))

# 3. Proportionality Condition
# i(dde3(s1,S,i1,I,t1,T))
				elif 'i(dde3' in line: 
					newline = line.replace('i(dde3','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					action = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)n1', newline)
					cw = re.search('n1(.*)', newline)
					output.write ("\n \n The action:"+action.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is impermissible because it violates the Proportionality condition of the DDE.") 
					output.write ("\n It prevents a desirable event, and as a consequence causes another desirable event.")
					output.write ("\n Its compared weight is"+cw.group(1)) 
# p(dde(s1,S,i1,I,t1,T))
				elif 'p(dde' in line: 
					newline = line.replace('p(dde','').replace(',',' ').replace('(',' ').replace(')',' ').replace('_',' ').replace('.',' ')						
					sim = re.search('s1(.*)i1', newline)
					volition = re.search('i1(.*)t1', newline)
					time = re.search('t1(.*)', newline)
					output.write ("\n \n The volition:"+volition.group(1))
					output.write ("\n which occurs in simulation"+sim.group(1))
					output.write ("at time"+time.group(1))
					output.write ("is permissible according to the Doctrine of Double Effect because it does not violate any of its conditions.") 

				

if __name__ == '__main__':
    # Lanches Clingo for the 1st time
    launch_clingo(input_files=['action.txt', 'collision.txt'], output_file='first_output.txt')

    # Transforms the result
    conversion('first_output.txt', 'first_converted.txt')

    # Lanches Clingo for the 2nd time
    launch_clingo(input_files=['first_converted.txt', 'causal.txt', 'good.txt', 'right.txt', 'show.txt'], output_file='second_output.txt')

    # Transforms the result
    conversion('second_output.txt', 'final_output.txt')

	# Translates the result
    translation('final_output.txt', 'english_output.txt')






