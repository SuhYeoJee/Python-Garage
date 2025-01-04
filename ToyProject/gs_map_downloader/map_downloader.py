import requests
import os
import random
from PIL import Image
import time
from tqdm import tqdm
# -------------------------------------------------------------------------------------------
base_url = "https://act-webstatic.hoyoverse.com/map_manage/map/2/9e1c6c4d2bac013bc0cdd81c58733f47/"
save_folder = "downloaded_images"
os.makedirs(save_folder, exist_ok=True)
image_width,image_height = 256,256
# -------------------------------------------------------------------------------------------

# 이미지 다운로드 함수
def download_image(url, filename):
    try:
        # 이미지를 GET 방식으로 다운로드
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(filename, "wb") as file:
                file.write(response.content)
        else:
            print(f"이미지 다운로드 실패 (상태 코드: {response.status_code}): {url}")
    except Exception as e:
        print(f"에러 발생 ({e}): {url}")
# --------------------------
# 여러 이미지를 다운로드하는 함수
def download_images(start_front, end_front, start_back, end_back):
    total_images = (end_front - start_front + 1) * (end_back - start_back + 1)  
    with tqdm(total=total_images, desc="Downloading images", unit="image") as pbar:
        for front in range(start_front, end_front + 1):  # 범위 끝 값을 포함
            for back in range(start_back, end_back + 1):
                image_url = f"{base_url}{front}_{back}_P0.webp"
                filename = os.path.join(save_folder, f"{front}_{back}_P0.webp")
                if not os.path.exists(filename):
                    time.sleep(random.uniform(0.1, 1))  # 랜덤한 시간 동안 대기
                    download_image(image_url, filename)
                pbar.update(1) 
# --------------------------
# 저장 파일명 생성 함수 
def get_output_file_path(start_front, end_front, start_back, end_back)->str:
    file_name = f'map_{start_front}_{end_front}_{start_back}_{end_back}.png'
    return os.path.join(save_folder,file_name)
# --------------------------
# 구간에 해당하는 이미지 파일들을 찾아 이어붙이는 함수
def combine_images_in_range(start_front, end_front, start_back, end_back):
    total_width = (end_front - start_front + 1) * image_width
    total_height = (end_back - start_back + 1) * image_height 
    combined_image = Image.new('RGB', (total_width, total_height), (0, 0, 0))

    current_x,current_y = 0,0
    total_images = (end_front - start_front + 1) * (end_back - start_back + 1)  
    with tqdm(total=total_images, desc="combining images", unit="image") as pbar:
        for back in range(start_back, end_back + 1):
            for front in range(start_front, end_front + 1):
                image_filename = os.path.join(save_folder, f"{front}_{back}_P0.webp")
                try:
                    image = Image.open(image_filename)
                    combined_image.paste(image, (current_x, current_y))
                    pbar.update(1)
                except FileNotFoundError:
                    print(f"누락: {image_filename}")
                current_x += image_width
            current_x = 0
            current_y += image_height
        else:
            combined_image.save(get_output_file_path(start_front, end_front, start_back, end_back),format="PNG")
            print(f'저장 완료')

# ===========================================================================================

# 2x2 크기의 랜덤 이미지
def test_download_random_images(size:int=2):
    random_front = random.randint(10, 80)
    random_back = random.randint(20, 69)
    end_front = random_front + size - 1
    end_back = random_back + size - 1
    download_images(random_front,end_front,random_back,end_back)
    combine_images_in_range(random_front,end_front,random_back,end_back)


def download_total_images():
    start_front, end_front, start_back, end_back = 10,80,20,69
    download_images(start_front, end_front, start_back, end_back)
    combine_images_in_range(start_front, end_front, start_back, end_back)


if __name__=='__main__':
    test_download_random_images(6)
    # download_total_images()