import concurrent.futures
import requests
import os

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url} to {save_path}")

def main():
    # 图片链接列表
    image_urls = [
        'https://example.com/image1.jpg',
        'https://example.com/image2.jpg',
        'https://example.com/image3.jpg',
        # ... 可以添加更多图片链接
    ]

    # 创建保存图片的目录
    save_directory = 'downloaded_images'
    os.makedirs(save_directory, exist_ok=True)

    # 使用 ThreadPoolExecutor 创建线程池
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 提交下载任务
        future_to_url = {executor.submit(download_image, url, f"{save_directory}/image{i}.jpg"): url for i, url in enumerate(image_urls)}

        # 等待所有任务完成
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    main()
