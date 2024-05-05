# 使用官方的 Python 3.9 slim 镜像
FROM python:3.9-slim AS base

# 设置工作目录
WORKDIR /app

# 安装系统依赖（并说明每个依赖的作用）
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libffi-dev \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# 更新 pip 到最新版
RUN pip install --upgrade pip

# 分段复制文件：先复制 requirements.txt
COPY requirements.txt /app/

# 使用升级后的pip安装依赖，锁定依赖版本
RUN pip install --no-cache-dir -r /app/requirements.txt

# 使用多阶段构建，创建一个新的阶段来复制应用代码
FROM base AS final

# 复制应用代码，而不是全部文件
COPY . /app/

# 暴露 Streamlit 默认端口
EXPOSE 8501

# 运行 Streamlit 应用
CMD ["streamlit", "run", "app.py"]