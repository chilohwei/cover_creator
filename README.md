<div align="center">
<h1 align="center">封面制作工具：创意封面一键生成</h1>

<p align="center">
  <a href="https://github.com/chiloh/cover_creator/stargazers"><img src="https://img.shields.io/github/stars/chilohwei/cover_creator.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/chilohwei/cover_creator/issues"><img src="https://img.shields.io/github/issues/chilohwei/cover_creator.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/chilohwei/cover_creator/network/members"><img src="https://img.shields.io/github/forks/chilohwei/cover_creator.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/chilohwei/cover_creator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/chilohwei/cover_creator.svg?style=for-the-badge" alt="License"></a>
</p>
<h3>简体中文 | <a href="README-en.md">English</a></h3>
<br>
</div>

## 项目简介
本项目是一个基于Streamlit的封面制作工具，旨在帮助用户快速生成适用于不同社交平台的个性化封面图。用户可以通过简单的界面操作，自定义背景、文字、字体样式等，轻松创作出吸引眼球的封面。

## 功能特性
- **多平台支持**：一键适配Bilibili、抖音、小红书、微信公众号、微信视频号等主流社交平台尺寸。
- **多样化背景**：支持纯色、渐变色以及自定义上传图片作为背景。
- **文字与字体定制**：自由输入文字内容，选择字体风格及大小，调节文字颜色与描边效果。
- **高级设置**：调整文字旋转角度，控制描边宽度与颜色，满足个性化需求。
- **即时预览与下载**：实时预览封面效果，一键下载高质量PNG格式封面图。

## 快速开始
### 环境要求
确保已安装以下依赖：
- Python 3.9+
- Streamlit
- Pillow

### 安装指南
#### 本地部署
1. 克隆本仓库到本地：
```bash
   git clone https://github.com/chilohwei/cover_creator.git
```

2. 进入项目目录并安装依赖：
```bash
   cd cover_creator
   pip install -r requirements.txt
```

3. 在项目根目录下，执行以下命令启动应用：
```bash
  streamlit run app.py
```
然后在浏览器中访问展示的URL即可开始使用封面制作工具。

#### Docker部署
执行下方命令，然后打开`http://localhost:8501`访问使用。

```bash
docker run -d -p 8501:8501 chiloh/cover_creator:latest
```

## 关于作者
Chiloh，一位热爱探索图形设计与用户体验的软件开发者。更多项目和信息，请访问我的[GitHub](https://github.com/chilohwei)。


## 贡献
欢迎任何形式的贡献，包括但不限于报告问题、提出建议或提交代码。让我们一起让这个工具更加完善！

## 致谢
感谢开源社区的支持，特别是Streamlit团队提供了强大的工具，使得快速构建美观的Web应用成为可能。

## 注意
请确保遵循项目内的`LICENSE`文件规定使用本项目。如需部署至生产环境，请考虑安全性与性能优化措施。