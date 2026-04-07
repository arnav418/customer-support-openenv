import random

class MyEnvEnvironment:

    def __init__(self):
        self.step_count = 0
        self.max_steps = 3

        self.tasks = [
            {
                "query": "My payment failed",
                "answer": "refund",
                "difficulty": "easy"
            },
            {
                "query": "App crashes after login on Android 13",
                "answer": "troubleshoot",
                "difficulty": "medium"
            },
            {
                "query": "Charged twice across different payment methods, need escalation",
                "answer": "refund",
                "difficulty": "hard"
            }
        ]

    async def reset(self):
        self.step_count = 0
        self.current_task = random.choice(self.tasks)

        return {
            "observation": self.current_task["query"],
            "reward": 0.0,
            "done": False
        }

    async def step(self, action):
        self.step_count += 1

        msg = action.get("message", "").lower()
        correct = self.current_task["answer"]

        if correct in msg:
            reward = 1.0
            response = "Correct solution"

        elif any(word in msg for word in ["help", "check", "support"]):
            reward = 0.5
            response = "Partial solution"

        elif "refund" in msg or "troubleshoot" in msg:
            reward = 0.2   

        else:
            reward = -0.2  
            response = "Wrong solution"

        done = reward == 1.0 or self.step_count >= self.max_steps

        return {
            "observation": response,
            "reward": reward,
            "done": done,
            "info": {
                "expected_answer": correct,
                "difficulty": self.current_task.get("difficulty"),
                "step_count": self.step_count,
                "max_steps": self.max_steps
            }
        }