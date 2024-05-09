import re

def main():
    print(parse(input('HTML: ')))

def parse(s):
    iframe_match = re.search(r'<iframe[^>]*></iframe>', s)
    if iframe_match:
        url_match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', iframe_match.group())
        if url_match:
            video_id = url_match.group(1)
            return 'https://youtu.be/' + video_id
    return None

if __name__ == '__main__':
    main()
