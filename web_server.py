from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json
from research_server import mcp

app = FastAPI(title="MCP Research Server")

@app.get("/")
async def root():
    return {"message": "MCP Research Server is running"}

@app.post("/mcp")
async def mcp_endpoint(request: dict):
    # Handle MCP requests
    # This would need to be adapted for web transport
    return {"status": "MCP endpoint"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)