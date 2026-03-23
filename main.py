import sys
import os
import threading
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QTextEdit, QLabel, QProgressBar, QFileDialog)
from PyQt6.QtCore import pyqtSignal, QObject
import yt_dlp

# UI 업데이트를 위한 시그널 클래스
class DownloadSignaler(QObject):
    progress = pyqtSignal(float)
    log = pyqtSignal(str)
    finished = pyqtSignal()

class KTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.signaler = DownloadSignaler()
        self.save_path = os.path.join(os.path.expanduser("~"), "Downloads")
        self.init_ui()

    def init_ui(self):
        # 레이아웃 설정
        layout = QVBoxLayout()

        # 제목 및 설명
        title = QLabel("🇰🇷 K-Tube 유튜브 다운로더")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        # URL 입력창
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("유튜브 링크(URL)를 입력하세요...")
        layout.addWidget(self.url_input)

        # 저장 경로 설정
        path_layout = QHBoxLayout()
        self.path_label = QLabel(f"저장 위치: {self.save_path}")
        path_btn = QPushButton("경로 변경")
        path_btn.clicked.connect(self.change_path)
        path_layout.addWidget(self.path_label)
        path_layout.addWidget(path_btn)
        layout.addLayout(path_layout)

        # 다운로드 버튼
        self.download_btn = QPushButton("다운로드 시작")
        self.download_btn.setStyleSheet("background-color: #e74c3c; color: white; height: 40px; font-weight: bold;")
        self.download_btn.clicked.connect(self.start_download_thread)
        layout.addWidget(self.download_btn)

        # 진행 바
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # 로그 출력창
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setPlaceholderText("작업 로그가 여기에 표시됩니다.")
        layout.addWidget(self.log_display)

        # 시그널 연결
        self.signaler.log.connect(self.append_log)
        self.signaler.progress.connect(self.update_progress)
        self.signaler.finished.connect(self.on_finished)

        self.setLayout(layout)
        self.setWindowTitle("K-Tube Downloader")
        self.resize(500, 400)

    def change_path(self):
        directory = QFileDialog.getExistingDirectory(self, "저장 폴더 선택")
        if directory:
            self.save_path = directory
            self.path_label.setText(f"저장 위치: {self.save_path}")

    def append_log(self, text):
        self.log_display.append(text)

    def update_progress(self, val):
        self.progress_bar.setValue(int(val))

    def on_finished(self):
        self.download_btn.setEnabled(True)
        self.download_btn.setText("다운로드 시작")
        self.append_log("✅ 모든 작업이 완료되었습니다.")

    def start_download_thread(self):
        url = self.url_input.text().strip()
        if not url:
            self.append_log("❌ 오류: URL을 입력해 주세요.")
            return

        self.download_btn.setEnabled(False)
        self.download_btn.setText("다운로드 중...")
        self.progress_bar.setValue(0)
        
        # 별도 쓰레드에서 다운로드 실행 (UI 프리징 방지)
        thread = threading.Thread(target=self.download_video, args=(url,), daemon=True)
        thread.start()

    def download_video(self, url):
        def progress_hook(d):
            if d['status'] == 'downloading':
                p = d.get('_percent_str', '0%').replace('%','')
                try:
                    self.signaler.progress.emit(float(p))
                except: pass
            elif d['status'] == 'finished':
                self.signaler.log.emit(f"파일 다운로드 완료: {d.get('filename', '알 수 없는 파일')}")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best', # 최상위 화질 자동 선택
            'outtmpl': f'{self.save_path}/%(title)s.%(ext)s', # 저장 파일명 형식
            'progress_hooks': [progress_hook],
            'noplaylist': True,
        }

        try:
            self.signaler.log.emit(f"정보 분석 중: {url}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.signaler.finished.emit()
        except Exception as e:
            self.signaler.log.emit(f"❌ 에러 발생: {str(e)}")
            self.signaler.finished.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KTubeDownloader()
    window.show()
    sys.exit(app.exec())
