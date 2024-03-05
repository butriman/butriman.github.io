import emoji
import markdown
import pdfkit

def replace_emojis_in_md(file_path):
    # Defining emoji to image mapping
    emoji_image_map = {
        "😀": "https://example.com/emoji_images/grinning.png",
        "👨‍💻": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f468-200d-1f4bb.svg",
        "🎓️": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f393.svg",
        "🚀": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f680.svg",
        "🇷🇺": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f1f7-1f1fa.svg",
        "🇺🇸": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f1fa-1f1f8.svg",
        "🌐": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f310.svg",
        "💻️": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f4bb.svg",
        "🏊‍♂️": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f3ca-200d-2642-fe0f.svg",
        "🏄‍♂️": "https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/1f3c4-200d-2642-fe0f.svg"
    }
    
    # Reading the Markdown content
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replacing emojis with image links
    def emoji_replacer(match):
        char = match.group(0)
        image_url = emoji_image_map.get(char, None)
        if image_url:
            return f"![{char}]({image_url})"
        return char

    updated_content = emoji.get_emoji_regexp().sub(emoji_replacer, content)
    print('updated_content: ', updated_content)

    # Convert Markdown to HTML
    html_content = markdown.markdown(updated_content)
    print('html_content: ', html_content)
    
    pdfkit.from_string(html_content, 'butriman_cv.pdf')
