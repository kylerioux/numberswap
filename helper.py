from numberswap import *
import gym
from gym import spaces

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, numberline_len=10, render_mode="console"):
        super(CustomEnv, self).__init__()
        self.render_mode = render_mode
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(3)
       
        self.numberline = numberswap.generateList(numberline_len)

        self.observation_space = spaces.Box(low=0, high=self.numberline_len,
                                            shape=(1,), dtype=np.uint8)

        print("Done Initialization")

    def step(self, action):
        return observation, reward, done, info

    def reset(self, seed=None, options=None):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        super().reset(seed=seed, options=options)
        # Initialize the agent at the right of the grid
        self.numberline = numberswap.generateList(numberline_len)
        # here we convert to float32 to make it more general (in case we want to use continuous actions)
        return np.array([self.numberline]).astype(np.float32), {}  # empty info dict
        #return observation  # reward, done, info can't be included

    def render(self, mode='console'):
        printList(self.numberline)

    def close (self):
        pass