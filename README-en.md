<div align="center">
<h1 align="center">Cover Creation Tool: Creative Covers Generated with a Single Click</h1>

<p align="center">
  <a href="https://github.com/chiloh/cover_creator/stargazers"><img src="https://img.shields.io/github/stars/chilohwei/cover_creator.svg?style=for-the-badge" alt="Stargazers"></a>
  <a href="https://github.com/chilohwei/cover_creator/issues"><img src="https://img.shields.io/github/issues/chilohwei/cover_creator.svg?style=for-the-badge" alt="Issues"></a>
  <a href="https://github.com/chilohwei/cover_creator/network/members"><img src="https://img.shields.io/github/forks/chilohwei/cover_creator.svg?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/chilohwei/cover_creator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/chilohwei/cover_creator.svg?style=for-the-badge" alt="License"></a>
</p>
<h3>English | <a href="README.md">Simplified Chinese</a></h3>
<br>
</div>

## Overview
This project is a cover creation tool based on Streamlit, designed to help users quickly generate personalized covers suitable for various social media platforms. Users can easily create eye-catching covers through simple interface operations, customizing backgrounds, text, font styles, and more.

## Features
- **Multi-platform Support**: One-click adaptation for popular social media platform sizes such as Bilibili, TikTok, Xiaohongshu, WeChat Official Accounts, WeChat Video Account, etc.
- **Diverse Backgrounds**: Support for solid colors, gradients, and custom uploaded images as backgrounds.
- **Text and Font Customization**: Freely input text content, choose font styles and sizes, and adjust text colors and stroke effects.
- **Advanced Settings**: Adjust the text rotation angle, control the stroke width and color to meet personalized needs.
- **Instant Preview and Download**: Real-time preview of cover effects, one-click download of high-quality PNG format cover images.

## Quick Start
### Environment Requirements
Ensure the following dependencies are installed:
- Python 3.9+
- Streamlit
- Pillow

### Installation Guide
#### Local Deployment
1. Clone this repository locally:
```bash
    git clone https://github.com/chilohwei/cover_creator.git
```

2. Enter the project directory and install dependencies:
```bash
    cd cover_creator
    pip install -r requirements.txt
```

3. In the project root directory, execute the following command to start the application:
```bash
   streamlit run app.py
```
Then visit the displayed URL in your browser to start using the cover creation tool.

#### Docker Deployment
Execute the following command, and then open `http://localhost:8501` to access it.

```bash
docker run -d -p 8501:8501 chiloh/cover_creator:latest
```

## About the Author
Chiloh, a software developer who loves to explore graphic design and user experience. For more projects and information, please visit my [GitHub](https://github.com/chilohwei).

## Contributions
Contributions of any form are welcome, including but not limited to reporting issues, making suggestions, or submitting code. Let's work together to make this tool better!

## Acknowledgements
Thanks to the support of the open-source community, especially the Streamlit team for providing a powerful tool that makes it possible to quickly build beautiful web applications.

## Note
Please ensure that you comply with the provisions of the `LICENSE` file within the project when using this project. If deploying to a production environment, consider security and performance optimization measures.