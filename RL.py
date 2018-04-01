#========================
#Reinforcement Learning
#========================

::Agent 
	:make observation, take action(in environment), receive rewards
	:goal - max expected long-term rewards (sparse and delayed)
	:policy - the algorithm to determine its action is called policy
		:stochastic policy
		:policy gradient - search in the gradients(high rewards dir) of the rewards regards to policy par.
	:picking action with prob. - exploring new actions and exploiting the action are known to work well

::Rewards
	:sparse and delayed
	:credit assignment - expected sum of discounted future rewards
		:sum - evaluate an action based on the sum of all rewards coming after items
		:discount - applying a discount rate r(0.95~0.99)  at each step
		:normalize - run many times get normalized action score

::Policy Gradients

::Markov Decision Processes(MDP)
	:optimal state value for s - sum of all discounted future rewards the agent can expect on average after reaches state s. assuming it acts optimally.
	:Bellman optimality equation - 


