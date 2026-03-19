# pyVideoTrans đã Việt hóa

`pyVideoTrans` là ứng dụng dịch video, tạo phụ đề, nhận dạng giọng nói và lồng tiếng AI. Repo này là bản mã nguồn đã được Việt hóa giao diện/tài liệu để thuận tiện cài đặt và sử dụng tại môi trường Việt Nam.

## Tính năng chính

- Dịch video từ ngôn ngữ nguồn sang ngôn ngữ đích.
- Tạo phụ đề từ audio/video.
- Dịch phụ đề SRT.
- Lồng tiếng AI với nhiều kênh TTS.
- Hỗ trợ cả giao diện đồ họa và dòng lệnh.
- Làm việc với nhiều nhà cung cấp ASR, dịch máy/LLM và TTS.

## Thành phần chính trong repo

- `sp.py`: điểm vào giao diện đồ họa.
- `cli.py`: điểm vào dòng lệnh.
- `videotrans/`: mã nguồn chính của ứng dụng.
- `docs/`: tài liệu bổ sung.
- `tests/`: một số test tích hợp/liên quan translator.
- `update_ffmpeg.bat`: script hỗ trợ cập nhật FFmpeg trên Windows.

## Yêu cầu môi trường

### Cấu hình máy

- Tối thiểu: Windows 10/11 64-bit, CPU 4 nhân, RAM 8 GB, trống 20 GB.
- Khuyến nghị: CPU 6 đến 8 nhân, RAM 16 GB+, GPU NVIDIA 6 đến 8 GB VRAM, trống 50 GB+.
- Nếu chạy tác vụ dài, batch nhiều video, voice clone hoặc model lớn thì nên dùng máy mạnh hơn.

### Phần mềm bắt buộc

- Python `3.10`.
- `FFmpeg` có trong `PATH`, hoặc đặt `ffmpeg.exe` và `ffprobe.exe` trong thư mục dự án.
- `uv` để đồng bộ môi trường nhanh và ổn định.

Lưu ý: `pyproject.toml` hiện ghim `requires-python = ">=3.10, <3.11"`, vì vậy nên dùng đúng Python 3.10 để tránh lệch dependency.

## Cài đặt nhanh

### Cách 1: dùng bản đóng gói Windows

1. Tải bản phát hành `.zip` hoặc `.7z` từ trang Releases của dự án.
2. Giải nén vào đường dẫn ngắn, không có dấu và hạn chế khoảng trắng.
3. Chạy `sp.exe`.

Phù hợp nếu bạn chỉ muốn dùng ứng dụng mà không cần môi trường Python.

### Cách 2: chạy từ mã nguồn

```bash
git clone https://github.com/Hoangcunut/Viethoapyvideotrans.git
cd Viethoapyvideotrans
uv sync
```

Khởi động giao diện:

```bash
uv run sp.py
```

Xem trợ giúp CLI:

```bash
uv run cli.py --help
```

## Cách dùng

### Giao diện đồ họa

Luồng dùng cơ bản:

1. Chọn file audio/video đầu vào.
2. Chọn thư mục lưu kết quả.
3. Chọn ngôn ngữ nguồn và ngôn ngữ đích.
4. Chọn kênh nhận dạng giọng nói, dịch và lồng tiếng nếu cần.
5. Bấm `Start` để chạy pipeline.

### Dòng lệnh

Ứng dụng hỗ trợ 4 nhóm tác vụ chính:

- `stt`: nhận dạng giọng nói thành văn bản/phụ đề.
- `tts`: tổng hợp giọng nói từ văn bản/phụ đề.
- `sts`: dịch phụ đề.
- `vtv`: dịch video trọn quy trình.

Ví dụ:

```bash
uv run cli.py --task stt --name "./audio.wav" --model_name large-v3
```

```bash
uv run cli.py --task vtv --name "./video.mp4" --source_language_code zh --target_language_code en
```

## Tài liệu liên quan

- `docs/README_VI.md`: bản hướng dẫn tiếng Việt cũ/dự phòng.
- `docs/README_CN.md`: README gốc theo tài liệu Trung văn.
- `docs/language.md`: hướng dẫn thêm/chỉnh language pack.
- `docs/googlecloud_tts.md`: ghi chú cấu hình Google Cloud TTS.
- `docs/whisper_net_setup.md`: ghi chú tăng tốc/cấu hình thêm cho một số môi trường.

## Ghi chú vận hành

- Nếu không có GPU, ứng dụng vẫn chạy được nhưng sẽ chậm hơn đáng kể.
- Một số kênh dịch/TTS/ASR cần API key hoặc cấu hình thêm trong giao diện cài đặt.
- Nên giữ đường dẫn dự án và đường dẫn file đầu vào ngắn, ít ký tự đặc biệt để giảm lỗi FFmpeg/model.
- Repo hiện là bản đã Việt hóa, nhưng lõi xử lý vẫn bám theo kiến trúc gốc của `pyVideoTrans`.

## Thông tin dự án

- Tên dự án: `pyVideoTrans`
- Phiên bản trong repo hiện tại: `v3.98`
- License: `GPL-3.0`
