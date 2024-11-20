import os
import shutil

# 다운로드 폴더 경로
download_folder = r"c:\Users\student\Downloads"

# 파일 이동 대상 폴더 경로 설정
folders = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 폴더 생성 및 파일 이동 함수
def organize_files():
    for folder_name, extensions in folders.items():
        # 대상 폴더 생성
        target_folder = os.path.join(download_folder, folder_name)
        os.makedirs(target_folder, exist_ok=True)

        # 해당 확장자를 가진 파일 검색 및 이동
        for extension in extensions:
            for file in [f for f in os.listdir(download_folder) if f.lower().endswith(extension.split("*")[1])]:
                source_path = os.path.join(download_folder, file)
                destination_path = os.path.join(target_folder, file)
                shutil.move(source_path, destination_path)
                print(f"Moved: {file} to {target_folder}")

if __name__ == "__main__":
    organize_files()
