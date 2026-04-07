from my_env.client import MyEnv, MyAction


def run_episode():
    env = MyEnv(base_url="http://localhost:8000")

    result = env.reset()
    print("Task:", result.observation)

    done = False
    total_reward = 0

    while not done:
        query = result.observation.lower()

        # Simple rule-based agent
        if "payment" in query or "charged" in query:
            action = "refund"
        elif "crash" in query:
            action = "troubleshoot"
        else:
            action = "help"

        result = env.step(MyAction(message=action))

        print("Action:", action)
        print("Response:", result.observation)

        total_reward += result.reward
        done = result.done

    print("Total Reward:", total_reward)


if __name__ == "__main__":
    run_episode()