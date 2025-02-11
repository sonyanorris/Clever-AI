from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

app = FastAPI(title="Clever AI API")

# Enable CORS for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REST Endpoint
@app.get("/status", tags=["REST"])
async def get_status():
    return {"status": "ok"}

# GraphQL Schema & Resolvers
type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello from Clever AI API!"

schema = make_executable_schema(type_defs, query)
app.mount("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
