import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from data.data_source import get_data, get_performance_ai_answer

app = FastAPI()

# Allow frontend to communicate with FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change to specific domains in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

user_tasks: dict[str, dict] = {}

# 📌 Data Retrieval Function
async def retrieve_data(user_id: str, user_input: str):
    return await get_data(user_id, user_input)

# 📌 Streaming Insights Generator
async def generate_insights(user_id: str):
    if user_id not in user_tasks or "data" not in user_tasks[user_id]:
        yield "data: Waiting for data...\n\n"
        return
    
    data = user_tasks[user_id]["data"]
    user_input = user_tasks[user_id]["query"]

    # 📌 Get AI performance response BEFORE streaming
    performance = await get_performance_ai_answer(user_id, user_input, data)

    # 📌 Stream response token by token (like ChatGPT)
    print("Streaming insights in real-time...")
    for token in performance.split(" "):  # Simulating tokenized output
        yield f"{token + ' '}\n\n"
        await asyncio.sleep(0.02)  # Small delay to simulate real-time effect
    
    # 📌 Final message to indicate the stream is finished
    yield f"data: [END OF STREAM]\n\n"
    print(f"Streaming finished for user_id: {user_id}")
    user_tasks.pop(user_id, None)  # Remove user task from memory


# 📌 HTTP Endpoint: Process Queries & Store Data
@app.post("/query")
async def query(user_id: str, user_input: str):
    user_tasks[user_id] = {"status": "processing", "query": user_input}

    # Retrieve data
    retrieved_data = await retrieve_data(user_id, user_input)

    # Store data in memory
    user_tasks[user_id]["data"] = retrieved_data
    user_tasks[user_id]["status"] = "completed"

    return {
        "user_id": user_id,
        "status": "completed",
        "data": retrieved_data
    }

# 📌 SSE Streaming Endpoint
@app.get("/stream/{user_id}")
async def sse_stream(user_id: str):
    if user_id not in user_tasks:
        return StreamingResponse(
            (f"data: Invalid user_id {user_id}\n\n" for _ in range(1)),
            media_type="text/event-stream"
        )

    # Streaming response (real-time token generation)
    async def event_stream():
        print(f"Streaming insights for user_id: {user_id}")
        async for insight in generate_insights(user_id):
            yield insight
    
    return StreamingResponse(event_stream(), media_type="text/event-stream")