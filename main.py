import asyncio

from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import StreamingResponse

from data.data_source import get_data, get_performance_ai_answer

app = FastAPI()


user_tasks: dict[str, dict] = {}


# 📌 Simulated Data Retrieval Function
async def retrieve_data(user_id: str, user_input: str):
    return await get_data(user_id, user_input)


# # 📌 Mock function to generate insights dynamically
async def generate_insights(task_id: str):
    if task_id not in user_tasks or "data" not in user_tasks[task_id]:
        yield f"data: Waiting for data\n\n"
        return
    
    data = user_tasks[task_id]["data"]
    user_input = user_tasks[task_id]["query"]

    performance = get_performance_ai_answer(task_id, user_input, data)
    performance_list = performance.split(" ")
    print("Starting to generate insights...")
    for perf in performance_list:
        yield f"{perf} "
        await asyncio.sleep(0.1)


# 📌 HTTP Endpoint: Processes Queries & Stores Data for User
@app.post("/query")
async def query(user_id: str, user_input: str, background_tasks: BackgroundTasks):
    user_tasks[user_id] = {"status": "processing", "query": user_input}

    # Retrieve data
    retieved_data = await retrieve_data(user_id, user_input)

    # Store data
    user_tasks[user_id]["data"] = retieved_data
    user_tasks[user_id]["status"] = "completed"

    # Start generating insights in the background
    background_tasks.add_task(generate_insights, user_id)

    return {
        "user_id": user_id,
        "status": "completed",
        "data": retieved_data
    }


# 📌 SSE Streaming Endpoint: Streams Insights Using Retrieved Data
@app.get("/stream/{user_id}")
async def sse_stream(user_id: str):
    if user_id not in user_tasks:
        return StreamingResponse(
            (f"data: Invalid user_id {user_id}\n\n" for _ in range(1)),
            media_type="text/event-stream"
        )

    # Stream Insights
    async def event_stream():
        print(f"Streaming insights for user_id: {user_id}")
        async for insight in generate_insights(user_id):
            yield insight
    
    return StreamingResponse(event_stream(), media_type="text/event-stream")
