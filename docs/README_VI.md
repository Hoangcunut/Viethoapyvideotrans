# pyVideoTrans - Hướng dẫn Tiếng Việt

## Tổng quan

`pyVideoTrans` là ứng dụng dịch video, tạo phụ đề, chuyển giọng nói thành văn bản và lồng tiếng AI. Dự án hỗ trợ cả giao diện đồ họa và dòng lệnh, phù hợp cho nhu cầu xử lý video đơn lẻ hoặc theo lô.

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
