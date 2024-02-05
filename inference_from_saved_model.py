from stable_baselines3 import PPO, A2C, DQN
from train_model import CustomEnv
from stable_baselines3.common.env_util import make_vec_env

def main():
    model = PPO.load("ppo_numswap_5000_vec_env_v1")
    vec_env = make_vec_env(CustomEnv, seed=1, n_envs=1, env_kwargs=dict(numberline_len=10))
    obs = vec_env.reset()
    print("inf main")
    print(obs[0])
    print(obs[0].shape)
    n_steps = 1000
    reward = 0 # default starting reward
    for step in range(n_steps):
        action, _ = model.predict(obs)#, deterministic=True)
        print(f"Step {step + 1}")
        print("Action: ", action)
        obs, reward, done, info = vec_env.step(action)
        print("obs=", obs, "reward=", reward, "done=", done)
        vec_env.render()
        if done:
            # Note that the VecEnv resets automatically
            # when a done signal is encountered
            print("Goal reached!", "reward=", reward)
            break

if __name__== "__main__" :
    main()