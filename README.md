<br />
<p align="center">
    <a href="https://github.com/dragonx943/bypass-blitly.io">
        <img src="https://cdn.discordapp.com/attachments/1149612560769880074/1161701565707595786/image.png" alt="Logo">
    </a>

<h3 align="center">UPDATE: TOOL CHỈ HOẠT ĐỘNG VỚI P. 404, KHÔNG CÓ BẢN UPDATE NÀO THÊM HAY FIX LỖI</h3>
<h3 align="center">Bypass Blitly.io</h3>

<p align="center">
    1 công cụ đơn giản được viết bằng python 100%.
    <br />
    <br />
    <a href="https://github.com/dragonx943/bypass-blitly.io/issues">Báo cáo lỗi</a>
    </p>
</p>

<p align="center">
	<img alt="size" src="https://img.shields.io/github/repo-size/dragonx943/bypass-blitly.io">
</p>

<!-- Mục lục -->
<details open="open">
    <summary>Mục lục</summary>
    <ol>
        <li><a href="#giới-thiệu">Giới thiệu</a></li>
        <li><a href="#cài-đặt">Hướng dẫn cài đặt</a></li>
        <li><a href="#liên-hệ">Liên hệ</a></li>
    </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Giới thiệu
<p><strong>Dự án này là gì?</strong></p>
<strong>Bypass Blitly.io</strong> thật chất là một công cụ nhằm hỗ trợ mọi người trích xuất được Link gốc được gắn trong những Link rút gọn kiếm tiền trên nền tảng của <strong>Blitly.io</strong>. Thay vì phải <strong>vào 1 trang Web thứ ba, chờ 60s nhận code, copy paste rồi lấy Link gốc</strong> thì bây giờ <strong>hãy để Tool này hỗ trợ bạn lấy Link gốc nhanh chóng không cần chờ !!!</strong>. Áp dụng cho ae sử dụng Fast Forward nhưng không thể đi đến trang đích, Tool này sẽ giải quyết chuyện đó bằng python và hoàn toàn là tự động.
</p>

<!-- INSTALLATION -->
## Hướng dẫn cài đặt

Sau đây là các bước cơ bản để có thể cài đặt và vận hành.

### Yêu cầu

- Cần [python3](https://www.python.org/downloads/), [git](https://git-scm.com/)
- Cần Link Rút Gọn có tên miền https://blitly.io/...

### Cài Đặt

#### Windows

1. Tải Tool về Laptop/PC [tại đây](https://github.com/dragonx943/bypass-blitly.io/releases/download/releases/bypass.exe)

2. Mở Tool lên và tận hưởng: Nhập Link vào cửa sổ, sau đó ấn **Enter**

#### Android

1. Tải và cài đặt [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=vi&gl=US)

2. Dùng lệnh sau để tự động cài đặt:
    ```sh
    cd ../usr/etc/apt && rm sources.list.d -rf && rm sources.list && echo "deb https://packages.termux.dev/apt/termux-main/ stable main" >> sources.list && apt update && apt install python python-pip git -y
    ```

3. Dùng lệnh sau để tải Tool:
    ```sh
    cd ~ && git clone https://github.com/dragonx943/bypass-blitly.io
    ```

4. Dùng lệnh sau để cài đặt thư viện:
    ```sh
    cd bypass-blitly.io && pip install bs4 requests
    ```

5. Dùng lệnh sau để sử dụng:
    ```sh
    python bypass-blitly.io.py
    ```

P/s: Ngoài dùng Termux ra thì ae cũng có thể dùng với app khác như pydroid3, UserLAnd,...

#### Linux (Debian & Ubuntu):

1. Đăng nhập vào hệ điều hành với quyền quản trị viên (Root) và gõ câu lệnh sau (Cài đặt các gói cần thiết):
    ```sh
    apt install python3 python3-pip python-is-python3 git -y
    ```

2. Dùng git để tải file về:
    ```sh
    cd ~ && git clone https://github.com/dragonx943/bypass-blitly.io
    ```

3. Cài đặt thư viện cho python:
    ```sh
    cd bypass-blitly.io && pip3 install bs4 requests
    ```

4. Chạy Tool:
    ```sh
    python bypass-blitly.io.py
    ```

#### iPhone/iPad

1. Tải [iSH Shell](https://apps.apple.com/us/app/ish-shell/id1436902243) (cần iOS 11+)

2. Mở app, cài đặt gói cần thiết:
      ```sh
      apk update && apk add python3 py3-pip git && ln -sf python3 /usr/bin/python
      ```

3. Dùng git để tải file về:
    ```sh
    cd ~ && git clone https://github.com/dragonx943/bypass-blitly.io
    ```

4. Cài đặt thư viện cho python:
    ```sh
    cd bypass-blitly.io && pip3 install bs4 requests
    ```

5. Chạy Tool:
    ```sh
    python bypass-blitly.io.py
    ```

## Đóng góp

Sự đóng góp của bạn sẽ khiến cho project ngày càng tốt hơn, các bước để bạn có thể đóng góp

1. Fork project này
2. Tạo một branch mới chứa tính năng của bạn (`git checkout -b feature/AmazingFeature`)
3. Commit những gì bạn muốn đóng góp (`git commit -m 'Add some AmazingFeature'`)
4. Đẩy branch chứa tính năng của bạn lên (`git push origin feature/AmazingFeature`)
5. Tạo một pull request mới và sự đóng góp của bạn đã sẵn sàng để có thể đóng góp!

## Liên hệ

Nothing here =)))
