import numpy as np
import gymnasium

from numberswap import generateList, generateList, orderCheck, printList
from gymnasium import spaces
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import PPO, A2C, DQN
from stable_baselines3.common.env_util import make_vec_env

class CustomEnv(gymnasium.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}

    def __init__(self, numberline_len=10, render_mode="console"):
        super(CustomEnv, self).__init__()
        self.render_mode = render_mode
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(3)

        self.numberline_len = numberline_len
       
        self.numberline = generateList(self.numberline_len)

        self.observation_space = spaces.Box(low=0, high=numberline_len,
                                            shape=(1,10), dtype=np.uint8)

    def step(self, action):#, reward):
        global numberline

        info = {}
        truncated = False
        done = False
        reward = -1
        obs = self.on_press_action(action)
        if orderCheck(self.numberline):
            reward = 1000
            done = True
        #[0]
        #self.numberline = np.array([self.numberline]).astype(np.uint8)
        # print('step')
        # print(type(self.numberline))
        # print(self.numberline)
        return obs, reward, done, truncated, info

    def reset(self, seed=None, options=None):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        global numberline

        print('reset')

        super().reset(seed=seed, options=options) 

        #self.numberline = self.numberline[np.newaxis, :]

        self.numberline = generateList(self.numberline_len)
        
        obs = np.array([self.numberline]).astype(np.uint8)
        #self.numberline = self.numberline[np.newaxis, :]
        return obs, {}  # empty info dict

    def render(self, mode='console'):
        global numberline
        printList(self.numberline)

    def on_press_action(self, action):
        global numberline
        #print('onpress')
        #print(self.numberline)
        loc = self.numberline.copy()
        if action == 0:
            #print('onpress1')
            loc =  loc[1:]+[loc[0]]

        elif action == 1:
            #print('onpress2')
            loc = [loc[-1]] + loc[:-1]
             
        elif action == 2:
            #print('onpress3')
            loc[0], loc[1] = loc[1], loc[0]
            
        self.numberline = loc 
        return np.array([loc]).astype(np.uint8)

def main():
    global reward
    reward = 0 # what should it be initialized to?

    vec_env = make_vec_env(CustomEnv, seed=1, n_envs=1, env_kwargs=dict(numberline_len=10)) #seed=1 needed in windows

    model = PPO("MlpPolicy", vec_env, verbose=1).learn(50000)

    model.save("ppo_numswap_5000_vec_env_v1")
    
    # env = CustomEnv(numberline_len=10)
    # check_env(env, warn=True) # If the environment doesn't follow the interface, an error will be thrown

if __name__== "__main__" :
    main()