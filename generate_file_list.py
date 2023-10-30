import json
import urllib.parse

startIndex = 8


def generate_video_entry(url):
    # 从URL中解析文件名
    path = urllib.parse.unquote(urllib.parse.urlparse(url).query.split('=')[-1])
    title = path.split('/')[-1].replace('.mp4', '').replace('%20', ' ')

    # 根据url生成cover的链接
    cover_url = f"https://naruse.io/api/thumbnail/?path={urllib.parse.quote(path)}&size=medium"

    # 为了生成vidId，我们简单地取json list的长度+1
    # 在真实的场景下，您可能需要更复杂的逻辑或从数据库中获取ID
    vidId = f"vid-{startIndex + len(json_list) + 1:03d}"

    entry = {
        "vidId": vidId,
        "title": title,
        "url": url,
        "cover": cover_url
    }

    return entry


json_list = [
    # ... (您之前的json数据)
]

if __name__ == '__main__':
    url_list = """https://naruse.io/api/raw/?path=/%F0%9F%93%BA%20Bangumi/Platinum%20Disco%20-%20Nisemonogatari%20OP%203%20-%20%E7%99%BD%E9%87%91%E3%83%87%E3%82%A3%E3%82%B9%E3%82%B3%20-%20%E5%81%BD%E7%89%A9%E8%AA%9E%20%20(%20Lyrics%20Romaji%20).mp4
https://naruse.io/api/raw/?path=/%F0%9F%93%BA%20Bangumi/CHEESE%20CAKE%E3%80%80%E3%80%8E%E5%90%9B%E3%81%A8SOS%20(short%20ver.)%E3%80%8F.mp4
https://naruse.io/api/raw/?path=/%F0%9F%93%BA%20Bangumi/the%20peggies%E3%80%8C%E3%82%BB%E3%83%B3%E3%83%81%E3%83%A1%E3%83%BC%E3%83%88%E3%83%AB%E3%80%8DMusic%20Video.mp4
https://naruse.io/api/raw/?path=/%F0%9F%93%BA%20Bangumi/%E5%8C%96%E7%89%A9%E8%AA%9E%20ED%20%E5%90%9B%E3%81%AE%E7%9F%A5%E3%82%89%E3%81%AA%E3%81%84%E7%89%A9%E8%AA%9E%20nagi%201080P.mp4
https://naruse.io/api/raw/?path=/%F0%9F%93%BA%20Bangumi/%E5%8C%96%E7%89%A9%E8%AA%9Eop%20staple%20stable%20(%E9%99%84%E4%B8%AD%E6%97%A5%E5%AD%97%E5%B9%95).mp4
https://naruse.io/api/raw/?path=/%F0%9F%93%BA%20Bangumi/%E5%91%A8%E6%9D%B0%E5%80%AB%20Jay%20Chou%E3%80%90%E6%93%B1%E6%B7%BA%20Step%20Aside%E3%80%91-Official%20Music%20Video.mp4"""
    url_list = url_list.split('\n')
    for url in url_list:
        json_list.append(generate_video_entry(url))

    print(json.dumps(json_list, indent=4, ensure_ascii=False))
