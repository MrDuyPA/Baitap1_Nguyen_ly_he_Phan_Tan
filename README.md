# Baitap1_Nguyen_ly_he_Phan_Tan

Bài Tập 1 nộp môn Nguyên lý hệ phân tán.

# KVSS - Key Value Store Service (TCP Server/Client)

Dự án này triển khai hệ thống phân tán đơn giản với **TCP server** và **client** để lưu trữ key-value trong bộ nhớ, đồng thời cho phép quan sát các request/response bằng **Wireshark** hoặc `tshark`.

---

## 1. Yêu cầu môi trường

- Windows 10/11 với **WSL2** (Ubuntu khuyến nghị).
- Python 3 (đã cài trong WSL).
- Wireshark hoặc `tshark` (CLI) để quan sát gói tin.

---

## 2. Cài đặt WSL

Nếu chưa có WSL và Ubuntu:

```powershell
wsl --install -d Ubuntu

```

Đặt Ubuntu làm mặc định:
