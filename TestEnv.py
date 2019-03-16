from simulator.GymTraffic import GymTraffic

env = GymTraffic()

for trial_number in range(3):
    obs = env.reset()
    #print(env.action_space.spaces)

    while True:
        print(obs[0])

        env.render()
        obs, reward, term, info = env.step(env.action_space.sample())     # take a random action

        if term:
            break

env.close()
