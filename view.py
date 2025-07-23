import requests
import threading

TOOL_API_URL = "https://buf-view-tiktok-ayacte.vercel.app/tiktokview"

def send_single_request(tiktok_url, index):
    try:
        response = requests.get(TOOL_API_URL, params={'video': tiktok_url}, timeout=30)
        if response.status_code == 200:
            data = response.json()
            print(f"[Thread {index}] Thành công: {data.get('sent_success', 0)} | Thất bại: {data.get('sent_fail', 0)}")
        else:
            print(f"[Thread {index}] Lỗi HTTP {response.status_code}")
    except Exception as e:
        print(f"[Thread {index}] Lỗi: {e}")

def buff_view_multi_threads(tiktok_url, num_threads=100):
    print(f"\nĐang gửi {num_threads} request song song đến: {tiktok_url}")
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=send_single_request, args=(tiktok_url, i + 1))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Đã hoàn tất {num_threads} request.")

def main():
    while True:
        link = input("\nNhập link TikTok (hoặc để trống để thoát): ").strip()
        if not link:
            print("Thoát tool.")
            break

        try:
            threads = int(input("Nhập số lượng request song song (mặc định 100): ") or 100)
        except:
            print("Giá trị không hợp lệ. Dùng mặc định 100.")
            threads = 100

        buff_view_multi_threads(link, threads)

if __name__ == "__main__":
    main()