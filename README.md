# Asynchronous Advantage Actor-Critic with Communication

The source-code used on the paper **Multi-Agent Reinforcement Deep Learning with Emergent Communication**, published on [IJCNN'19](https://www.ijcnn.org/). The paper describes the A3C2 algorithm, for multi-agent learning, with communication.

![5](https://user-images.githubusercontent.com/9117323/54480728-fdc34980-4823-11e9-9591-2fd32f0abf1f.png)

Contains 4 environments (Hidden Reward, Navigation, Pursuit, Traffic Intersection), and scripts to launch A3C2 and learn policies. Use the `requirements.txt` to install your dependencies and run the scripts.

![4](https://user-images.githubusercontent.com/9117323/54480699-90171d80-4823-11e9-8032-e5fed1059b2b.png)

Video is available [here](https://github.com/bluemoon93/A3C2/blob/master/A3C2.wmv).

Each agent is defined by 3 networks.

![1](https://user-images.githubusercontent.com/9117323/54480701-90171d80-4823-11e9-86b0-e6e2f254c6be.png)

The algorithm is distributed, and multiple workers update the networks.

![2](https://user-images.githubusercontent.com/9117323/54480700-90171d80-4823-11e9-8d86-5d37ebc0e7b9.png)

Gradients are pushed across multiple time-steps to optimize the communication network and enforce communication.

![3](https://user-images.githubusercontent.com/9117323/54480703-90afb400-4823-11e9-953a-2326a864fc4c.png)




