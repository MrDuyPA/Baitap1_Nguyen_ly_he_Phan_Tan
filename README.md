# Baitap1_Nguyen_ly_he_Phan_Tan

Bài Tập 1 nộp môn Nguyên lý hệ phân tán.

# KVSS - Key Value Store Service (TCP Server/Client)

Dự án này triển khai hệ thống phân tán đơn giản với **TCP server** và **client** để lưu trữ key-value trong bộ nhớ, đồng thời cho phép quan sát các request/response bằng **Wireshark**

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

```powershell
wsl --set-default Ubuntu

```

## 3. Cài wireshark

```powershell
sudo apt update
sudo apt install tshark -y

```

## 4. Run project

Server :

```powershell
python3 server.py

```

Client:
Mở một terminal khác (cũng trong WSL)

```powershell
python3 client.py

```

Client đọc lệnh từ stdin, ví dụ:

```powershell
PUT user1 Alice
GET user1
DEL user1
STATS

```

Wireshark:

Mở một terminal khác ( cũng trong wsl ), sau đó chạy command

```powershell
sudo tshark -i any -f "tcp port 12345" -l -n -x

```

## 5. Note: Kết quả kiếm thử và phần trả lời câu hỏi bài tập trong folder report

# Microservice

## Bài tập được trả lời trong report/Kube
