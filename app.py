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

# Supabase Storage 圖片、PDF、影片 URL
supabase_files = [
    "https://lgztvgybalhvppkfpwdc.supabase.co/storage/v1/object/public/goldshoot0720/image/Screenshot%202025-07-06%20at%2016-40-13%20(Ministry%20of%20Examination%20R.O.C(Taiwan))FfD1M5Casnv7P5ErRDKIpHsACuhdB7.png",
    "https://lgztvgybalhvppkfpwdc.supabase.co/storage/v1/object/public/goldshoot0720/image/Screenshot%202025-07-06%20at%2019-30-50%20(Ministry%20of%20Examination%20R.O.C(Taiwan))t8oXnotAXWP5KGsPOB2CJLRbda885f.png",
    "https://lgztvgybalhvppkfpwdc.supabase.co/storage/v1/object/public/goldshoot0720/pdf/114080_02_202_2085_27720090%2011408049116215016157_ExamNotice.pdf",
    "https://lgztvgybalhvppkfpwdc.supabase.co/storage/v1/object/public/goldshoot0720/video/di-8jie-tai-bei-shi-chang-xuan-ju-hui-gu.mp4"
]

def fetch_and_print(url):
    print(f"\n🔎 Fetching: {url}")
    try:
        resp = requests.get(url)
        print(f"✅ Status code: {resp.status_code}")
        content_type = resp.headers.get('Content-Type', '')
        print(f"📄 Content-Type: {content_type}")
        print(f"📦 Size: {len(resp.content)} bytes")
        if 'application/json' in content_type or 'text' in content_type:
            print(resp.text[:500])  # 避免輸出過長，限制 500 字
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")

def main():
    # 抓首頁
    fetch_and_print(base_url)
    time.sleep(60)

    # 抓每個資料表
    for table in tables:
        fetch_and_print(f"{base_url}/{table}")
        time.sleep(60)

    # 抓 Supabase 儲存檔案（不儲存本地，只查看狀態）
    for url in supabase_files:
        fetch_and_print(url)
        time.sleep(60)

    print("\n🎉 全部抓取完成！")

if __name__ == "__main__":
    main()
