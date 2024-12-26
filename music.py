# 파이튜브를 이용한 유튜브 음악 자동 다운로드 프로그램

import yt_dlp
import os

def download_audio(youtube_url, output_path=os.getcwd()):
    # yt-dlp 옵션 설정
    ydl_opts = {
        'format': 'bestaudio/best',  # 가장 좋은 품질의 오디오 선택
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # 오디오만 추출
            'preferredcodec': 'mp3',     # mp3로 변환
            'preferredquality': '192',  # 비트레이트 설정
        }],
        'ffmpeg_location' : 'C:\\Users\\User\\scoop\\shims', 
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # 저장 경로와 파일명 템플릿
        'quiet': True,  # 진행 상황 출력
    }

    # yt-dlp 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def get_playlist_urls(playlist_url):
    # 옵션 설정
    ydl_opts = {
        'quiet': True,  # 진행 상황 출력 억제
        'extract_flat': True,  # 상세 정보를 가져오지 않고 URL만 가져오기
        'skip_download': True,  # 다운로드 생략
    }

    # yt-dlp 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)  # 정보만 가져옴
        if 'entries' in info_dict:  # 재생목록일 경우
            video_urls = [entry['url'] for entry in info_dict['entries']]
            return video_urls
        else:
            print("재생목록이 아닙니다.")
            return []

def dl_list():
    # 유튜브 URL 입력
    youtube_url = input("재생목록 유튜브 URL을 입력하세요: ")
    dir = input("저장할 dir을 입력하세요: ")

    # 다운로드 실행
    dl_list = get_playlist_urls(youtube_url)

    print(len(dl_list), "개의 음악 발견")
    for i, v in enumerate(dl_list):
        print(i, v)

    fail = []
    for i in dl_list:
        print('*************', i, '***************')
        try:
            download_audio(i, os.path.join(os.getcwd(), dir))
            print("success")
        except:
            print("fail")
            fail.append(i)
    
    print(len(dl_list), '개의 동영상', len(dl_list)-len(fail), '개 성공')
    for i, v in enumerate(fail):
        print(i, v)


def dl_one():
    youtube_url = input("유튜브 URL을 입력하세요: ")
    try:
        download_audio(youtube_url, os.getcwd())
        print("success")
    except:
        print("fail")
        
dl_one()