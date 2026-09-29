from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="UniBoard PoC", version="1.0")

class PostCreate(BaseModel):
    content: str = Field(min_length=1, max_length=5000)
    audience_type: str
    community_id: str | None = None

class Post(PostCreate):
    id: str
    author_id: str
    created_at: str

posts: list[Post] = []

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/posts", response_model=Post, status_code=201)
def create_post(request: PostCreate):
    if request.audience_type not in {"UNIVERSITY", "COMMUNITY"}:
        raise HTTPException(status_code=400, detail="Invalid audience_type")
    if request.audience_type == "COMMUNITY" and not request.community_id:
        raise HTTPException(status_code=400, detail="community_id is required for community posts")
    post = Post(id=f"p_{len(posts)+1:03d}", author_id="u_demo",
                created_at=datetime.now(timezone.utc).isoformat(), **request.model_dump())
    posts.append(post)
    return post

@app.get("/posts", response_model=list[Post])
def list_posts():
    return posts