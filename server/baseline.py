import requests

BASE_URL = "http://localhost:8000"


def run_episode():
    total_reward = 0

    res = requests.post(f"{BASE_URL}/reset").json()
    observation = res["observation"]

    print("\nTask:", observation)

    done = False

    while not done:
        if "payment" in observation.lower() or "charged" in observation.lower():
            action = "refund"
        elif "crash" in observation.lower():
            action = "troubleshoot"
        else:
            action = "help"

        res = requests.post(
            f"{BASE_URL}/step",
            json={"message": action}
        ).json()

        print("Action:", action)
        print("Response:", res)

        total_reward += res["reward"]
        observation = res["observation"]
        done = res["done"]

    return total_reward


if __name__ == "__main__":
    episodes = 3
    scores = []

    for i in range(episodes):
        print(f"\n========== Episode {i+1} ==========")
        score = run_episode()
        scores.append(score)

    print("\nFinal Scores:", scores)
    print("Average Score:", sum(scores) / len(scores))