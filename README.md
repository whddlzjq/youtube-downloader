# K-Tube Downloader (한국어 유튜브 다운로더) 🇰🇷

[Hitomi-Downloader](https://github.com/KurtBestor/Hitomi-Downloader)의 철학을 계승한, 한국 사용자를 위한 심플하고 강력한 유튜브 다운로더입니다.

## 🌟 주요 특징
- **완벽한 한국어 지원**: 직관적인 GUI 인터페이스가 모두 한국어로 구성되어 있습니다.
- **최고 화질 자동 선택**: `yt-dlp` 엔진을 사용하여 비디오와 오디오 중 최상의 품질을 자동으로 선택합니다.
- **멀티 쓰레딩 지원**: 다운로드 중에도 프로그램이 멈추지 않으며, 실시간으로 진행 상황을 확인할 수 있습니다.
- **경로 선택 기능**: 원하는 폴더를 자유롭게 지정하여 다운로드할 수 있습니다.
- **로그 시스템**: 진행 과정을 투명하게 확인할 수 있는 실시간 로그 창을 제공합니다.

## 🛠 기술 스택
- **Language**: Python 3.x
- **GUI Framework**: PyQt6
- **Core Engine**: [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## 🚀 시작하기

### 1. 필수 라이브러리 설치
프로그램 실행을 위해 아래 라이브러리가 필요합니다:
```bash
pip install yt-dlp PyQt6
```

> **참고**: 1080p 이상의 고화질 영상을 다운로드하려면 시스템에 [FFmpeg](https://ffmpeg.org/)가 설치되어 있어야 합니다.

### 2. 프로그램 실행
터미널 또는 명령 프롬프트에서 아래 명령어를 실행하세요:
```bash
python main.py
```

## 📂 프로젝트 구조
- `main.py`: 프로그램의 핵심 로직 및 GUI 코드
- `README.md`: 프로젝트 설명서

## 📝 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다.

---
**GitHub Repository**: [https://github.com/whddlzjq/youtube-downloader](https://github.com/whddlzjq/youtube-downloader)
