from unityagents import UnityEnvironment
from ddpg_agent import Agent
import torch
import numpy as np
from ddpg_agent import Agent
from model import Actor

env = UnityEnvironment(file_name='Reacher.app')

# get the default brain
brain_name = env.brain_names[0]
brain = env.brains[brain_name]

# reset the environment
env_info = env.reset(train_mode=False)[brain_name]

# number of agents
num_agents = len(env_info.agents)
print('Number of agents:', num_agents)

# size of each action
action_size = brain.vector_action_space_size
print('Size of each action:', action_size)

# examine the state space
states = env_info.vector_observations
state_size = states.shape[1]
print('There are {} agents. Each observes a state with length: {}'.format(states.shape[0], state_size))
print('The state for the first agent looks like:', states[0])

random_seed = 1
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
scores = np.zeros(num_agents)

if torch.cuda.is_available():
    trained_model = torch.load('checkpoint_actor.pth')
else:
    trained_model = torch.load('checkpoint_actor.pth',map_location={'cuda:0': 'cpu'})

agent = Agent(state_size=state_size, action_size=action_size, random_seed=random_seed)
agent.actor_local = Actor(state_size, action_size, random_seed).to(device)
agent.actor_local.load_state_dict(trained_model)

env_info = env.reset(train_mode=False)[brain_name]     # reset the environment
states = env_info.vector_observations                  # get the current state (for each agent)

while True:
    action = agent.act(states, add_noise=False)
    env_info = env.step(action)[brain_name]
    states = env_info.vector_observations              # get next state (for each agent)
