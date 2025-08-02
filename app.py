import requests
import time

base_url = "https://supabaseflaskgoldshoot0720-production.up.railway.app"

tables = [
    "article",
    "bank",
    "cloud",
    "experience",
    "food",
    "host",
    "inventory",
    "mail",
    "member",
    "routine",
    "subscription",
    "video"
]

def fetch_and_print(url):
    print(f"Fetching {url} ...")
    try:
        resp = requests.get(url)
        print(f"Status code: {resp.status_code}")
        print(resp.text)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

def main():
    # 先抓首頁
    fetch_and_print(base_url)
    time.sleep(60)

    # 依序抓每個表的路由
    for table in tables:
        fetch_and_print(f"{base_url}/{table}")
        time.sleep(60)

    print("全部抓取完成！")

if __name__ == "__main__":
    main()
