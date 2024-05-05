import streamlit as st
from cover_generator import create_cover, load_gradient
import io
import os
import streamlit as st

# 设置页面配置
st.set_page_config(page_title="封面制作工具", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto")

def main():
    page = st.sidebar.radio("菜单", ["封面制作工具", "关于作者：Chiloh"])

    if page == "封面制作工具":
        cover_creator()
    elif page == "关于作者：Chiloh":
        about_author()


def cover_creator():
    st.sidebar.title("封面制作工具")

    # 基础设置
    basic_settings = st.sidebar.expander("基础设置", expanded=True)
    platform = basic_settings.selectbox("选择平台", ["Bilibili", "抖音", "小红书", "微信公众号", "微信视频号"])
    bg_options = basic_settings.radio("背景选项", ["纯色", "渐变色", "上传图片"])

    if bg_options == "纯色":
        bg_color = basic_settings.color_picker("选择背景颜色", "#000000")
    elif bg_options == "渐变色":
        gradient = basic_settings.selectbox("选择渐变色", load_gradient(), format_func=lambda x: x[0])
    elif bg_options == "上传图片":
        bg_image = basic_settings.file_uploader("上传背景图片", type=["png", "jpg", "jpeg"])

    text = basic_settings.text_input("输入文字", "这里是封面文字")
    text_color = basic_settings.color_picker("选择文字颜色", "#FFFFFF")

    # 字体设置
    font_settings = st.sidebar.expander("字体设置")
    font_size = font_settings.slider("选择字体大小", min_value=10, max_value=160, value=80)
    font_choices = ["站酷快乐体", "站酷庆科黄油体", "站酷文艺体"]
    font_name = font_settings.selectbox("选择字体", font_choices)

    # 高级设置
    advanced_settings = st.sidebar.expander("高级设置")
    angle = advanced_settings.slider("设置文字旋转角度", min_value=0, max_value=180, value=0)
    stroke_width = advanced_settings.slider("设置文字描边宽度", min_value=0, max_value=10, value=2)
    stroke_color = advanced_settings.color_picker("选择描边颜色", "#F99706")

    sizes = {
        "Bilibili": (1200, 900),
        "抖音": (1080, 1920),
        "小红书": (1242, 1660),
        "微信公众号": (900, 500),
        "微信视频号": (1080, 1260)
    }
    size = sizes[platform]

    # 根据背景选项生成封面
    if bg_options == "纯色":
        image = create_cover(size, bg_options, bg_color, text, text_color, font_name, font_size, angle, stroke_width, stroke_color)
    elif bg_options == "渐变色":
        image = create_cover(size, bg_options, None, text, text_color, font_name, font_size, angle, stroke_width, stroke_color, gradient)
    elif bg_options == "上传图片":
        image = create_cover(size, bg_options, None, text, text_color, font_name, font_size, angle, stroke_width, stroke_color, None, bg_image)

    # 预览图和下载按钮
    if image:
        st.session_state['image'] = image
        if 'image' in st.session_state:
            file_path = save_image(st.session_state['image'], platform, size)
            with open(file_path, "rb") as file:
                st.download_button(
                    label="下载封面",
                    data=file,
                    file_name=f"{platform}-{size[0]}x{size[1]}.png",
                    mime="image/png",
                    key="download_button"
                )
            # 使用 use_column_width 自适应宽度，并设置合理的最大高度
            st.image(st.session_state['image'], caption='预览封面', use_column_width=True, output_format='PNG')

def save_image(img, platform, size):
    directory = "downloads"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, f"{platform}-{size[0]}x{size[1]}.png")
    img.save(file_path)
    return file_path

def about_author():
    st.title("关于作者")
    st.write("Chiloh 是一位软件产品经理，日常生活工作在西安。喜欢开源，也很喜欢折腾，对东西方哲学、人工智能、区块链等都比较感兴趣。")
    st.write("本项目由 ChatGPT 与我结对编程实现，查看项目源代码：[GitHub](https://github.com/chilohwei/cover_creator)")
    st.image("https://chilohdata.s3.bitiful.net/qrcode.jpg", caption="公众号：魏奇洛")


if __name__ == "__main__":
    main()