from numberswap import generateList, generateList, on_press_action, orderCheck, printList
#import gym
import gymnasium
#from gym import spaces
from gymnasium import spaces
from stable_baselines3.common.env_checker import check_env
import numpy as np

class CustomEnv(gymnasium.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, numberline_len=10, render_mode="console"):
        print('helper init')
        super(CustomEnv, self).__init__()
        self.render_mode = render_mode
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(2)

        self.numberline_len = numberline_len
       
        self.numberline = generateList(self.numberline_len)

        self.observation_space = spaces.Box(low=0, high=numberline_len,
                                            shape=(1,10), dtype=np.uint8)

        print("done helper init")

    def step(self, action):
        global reward 
        info = {}
        truncated = False
        done = False
        reward -= 1 # -1 reward per step
        numlist = on_press_action(action, self.numberline)
        if orderCheck(numlist):
            reward += 100
            done = True
        numlist = np.array(numlist)
        numlist = numlist[np.newaxis, :]
        numlist = numlist.astype('uint8')
        print(numlist)
        return numlist, reward, done,truncated, info

    def reset(self, seed=None, options=None):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        super().reset(seed=seed, options=options)
        # Initialize the agent at the right of the grid
        self.numberline = generateList(self.numberline_len)
        # here we convert to float32 to make it more general (in case we want to use continuous actions)
        return np.array([self.numberline]).astype(np.uint8), {}  # empty info dict
        #return observation  # reward, done, info can't be included

    def render(self, mode='console'):
        printList(self.numberline)

    def close (self):
        pass

def main():
    global reward
    reward = 0 # what should it be initialized to?
    env = CustomEnv()
    # If the environment don't follow the interface, an error will be thrown
    check_env(env, warn=True)

if __name__== "__main__" :
    main()