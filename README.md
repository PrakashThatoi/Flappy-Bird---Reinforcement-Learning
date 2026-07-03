# 🐦 Flappy Bird AI: Reinforcement Learning

An artificial intelligence agent that learns to play the classic game **Flappy Bird** from scratch using Reinforcement Learning. 

Instead of hardcoding rules or logic, the AI interacts with the game environment, observes the consequences of its actions, and progressively optimizes its gameplay to achieve superhuman performance.

> **[Insert GIF here]** 
> *(Tip: Add a GIF here showing your AI successfully navigating the pipes!)*

---

## 🧠 How the AI Learns (The RL Setup)

This project models the game as a Markov Decision Process (MDP). The agent uses **Deep-Q-Learning (DQN)** to maximize its score based on the following architecture:

*   **State Space:** The agent observes the environment to make decisions. The state inputs include:
  * the last pipe's horizontal position
  * the last top pipe's vertical position
  * the last bottom pipe's vertical position
  * the next pipe's horizontal position
  * the next top pipe's vertical position
  * the next bottom pipe's vertical position
  * the next next pipe's horizontal position
  * the next next top pipe's vertical position
  * the next next bottom pipe's vertical position
  * player's vertical position
  * player's vertical velocity
  * player's rotation
*   **Action Space:** The agent has only two possible discrete actions at any given frame:
    *   `0`: Do nothing
    *   `1`: Flap (jump)
*   **Reward System:**
    *   **+1** for successfully passing through a set of pipes.
    *   **+0.1** for every frame it stays alive .
    *   **-1.0** for colliding with a pipe or the ground.
    *   **−0.5**  touch the top of the screen

---

## ✨ Features

*   **Trainable Agent:** Run the training script to watch the agent learn from trial and error in real-time.
*   **Save & Load Models:** Save the best-performing neural network weights and load them later to watch the fully trained agent play.

---

## 🛠️ Tech Stack

*   **Language:** Python
*   **Game Environment:** Gymnasium
*   **Machine Learning:** Pytorch

---
