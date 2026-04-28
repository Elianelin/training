from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

from database import engine, Base
from routers import materials, courses, exams, employees, certificates, auth

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="培训管理系统",
    description="支持教材上传、知识库生成、自动出题、考试评分、员工认证管理的培训系统",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 路由注册
app.include_router(auth.router)
app.include_router(materials.router)
app.include_router(courses.router)
app.include_router(exams.router)
app.include_router(employees.router)
app.include_router(certificates.router)


@app.get("/")
async def root():
    """返回前端管理后台页面"""
    index_path = os.path.join("static", "index.html")
    if os.path.exists(index_path):
        return FileResponse(
            index_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return {"message": "培训管理系统 API 服务运行中", "docs": "/docs"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
