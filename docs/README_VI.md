# pyVideoTrans - Hướng dẫn Tiếng Việt

## Tổng quan

`pyVideoTrans` là ứng dụng dịch video, tạo phụ đề, chuyển giọng nói thành văn bản và lồng tiếng AI. Dự án hỗ trợ cả giao diện đồ họa và dòng lệnh, phù hợp cho nhu cầu xử lý video đơn lẻ hoặc theo lô.

## Cấu hình máy để cài và sử dụng

### Cấu hình tối thiểu

- Hệ điều hành: Windows 10/11 64-bit
- CPU: 4 nhân trở lên
- RAM: 8 GB
- Ổ cứng trống: 20 GB trở lên
- GPU: không bắt buộc, có thể chạy bằng CPU nhưng sẽ chậm
- Phần mềm cần có khi chạy từ mã nguồn: Python `3.10` đến `3.12`, `FFmpeg`, `uv`

### Cấu hình khuyến nghị

- Hệ điều hành: Windows 10/11 64-bit
- CPU: 6 đến 8 nhân trở lên
- RAM: 16 GB trở lên
- Ổ cứng trống: 50 GB trở lên nếu tải nhiều model
- GPU: NVIDIA 6 GB VRAM trở lên để tăng tốc ASR/TTS, khuyến nghị 8 GB VRAM trở lên
- Nếu dùng GPU NVIDIA theo hướng dẫn của dự án: nên có `CUDA 12.8` và `cuDNN 9.11`

### Khi nào cần máy mạnh hơn

- Xử lý video dài hoặc xử lý hàng loạt nhiều video
- Dùng các model nhận dạng giọng nói lớn
- Dùng voice cloning hoặc các mô hình TTS cục bộ
- Vừa dịch, vừa lồng tiếng, vừa ghép video trên cùng một máy

### Ghi chú

- Nếu chỉ cần cài và dùng bản `.exe`, bạn không cần cài Python.
- Nếu không có GPU NVIDIA, app vẫn dùng được nhưng thời gian xử lý sẽ lâu hơn đáng kể.
- Dung lượng đĩa có thể tăng nhanh khi tải model, sinh file tạm và xuất video kết quả.

## Cách cài đặt nhanh

### Cách 1: Dùng bản đóng gói Windows

1. Tải bản mới nhất từ `Releases`.
2. Giải nén vào một thư mục ngắn, không dấu và không có khoảng trắng nếu có thể. Ví dụ: `D:\pyVideoTrans`
3. Chạy `sp.exe`.

Lưu ý:

- Không chạy trực tiếp bên trong file `.zip`.
- Nếu muốn dùng GPU NVIDIA, cần cài `CUDA 12.8` và `cuDNN 9.11`.

### Cách 2: Chạy từ mã nguồn

Yêu cầu:

- Python `3.10` đến `3.12`
- `FFmpeg` có sẵn trong `PATH`, hoặc đặt `ffmpeg.exe` và `ffprobe.exe` vào thư mục dự án
- Khuyến nghị dùng `uv`

Lệnh cài đặt:

```bash
git clone https://github.com/jianchang512/pyvideotrans.git
cd pyvideotrans
uv sync
```

Khởi động giao diện:

```bash
uv run sp.py
```

Khởi động dòng lệnh:

```bash
uv run cli.py --help
```

## Cách dùng cơ bản trên giao diện

1. Bấm `Select audio & video` để chọn video hoặc audio cần xử lý.
2. Bấm `Save to..` để chọn thư mục lưu kết quả.
3. Chọn `Speech language` là ngôn ngữ gốc của video.
4. Chọn `Target lang` là ngôn ngữ đích.
5. Chọn `Translate channel` nếu bạn muốn dịch phụ đề.
6. Chọn `Dubbing channel` và `Dubbing role` nếu bạn muốn lồng tiếng.
7. Bấm `Start` để bắt đầu.

Một số chế độ hay dùng:

- Dịch video tự động: chọn video, đặt ngôn ngữ nguồn/đích, chọn kênh dịch và TTS nếu cần.
- Tạo phụ đề: chọn audio/video, chọn nhận dạng giọng nói, xuất ra SRT.
- Dịch file SRT: dùng nhóm công cụ hoặc CLI để dịch hàng loạt.
- Gộp video và phụ đề: dùng menu `Tools/Options`.

## Vị trí cần cấu hình thêm

- API dịch: menu `Trans Settings`
- API TTS: menu `TTS Settings`
- API nhận dạng giọng nói: menu `ASR Settings`
- Tinh chỉnh nâng cao: `Options`

## Ví dụ CLI

### Dịch video

```bash
uv run cli.py --task vtv --name "./video.mp4" --source_language_code zh --target_language_code en
```

### Chuyển audio thành phụ đề

```bash
uv run cli.py --task stt --name "./audio.wav" --model_name large-v3
```

## Lời khuyên khi dùng

- Nếu mới bắt đầu, hãy chạy bằng giao diện trước.
- Nếu chỉ cần phụ đề, không nhất thiết phải bật TTS.
- Nếu dùng API online, hãy kiểm tra proxy, key và quota trước.
- Nếu gặp lỗi mô hình, thử xem mục `Solution to model download failure`.

## Tệp quan trọng trong repo

- `sp.py`: điểm vào giao diện chính
- `cli.py`: điểm vào dòng lệnh
- `videotrans/language/vi.json`: gói ngôn ngữ Tiếng Việt
- `README.md`: giới thiệu tổng quan
