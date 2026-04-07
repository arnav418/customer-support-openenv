from fastapi import FastAPI
from server.my_env_environment import MyEnvEnvironment
from models import MyAction  

app = FastAPI()
env = MyEnvEnvironment()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/reset")
async def reset():
    return await env.reset()

@app.get("/state")
def state():
    if not hasattr(env, "current_task"):
        return {
            "message": "Call /reset first",
            "step_count": env.step_count,
            "done": False
        }

    return {
        "step_count": env.step_count,
        "current_task": env.current_task,
        "done": env.step_count >= env.max_steps
    }


@app.post("/step")
async def step(action: MyAction): 
    return await env.step(action.dict())  