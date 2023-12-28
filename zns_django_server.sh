#!/bin/bash

# Đường dẫn đến thư mục của Django project
PROJECT_DIR=/home/taitd/lee_zalo_zns/zns_management_system

# Tên virtual environment
VENV_NAME=myworld

# Địa chỉ và cổng của Django server
ADDRESS=127.0.0.1
PORT=5003

start() {
    cd $PROJECT_DIR

    # Activate virtual environment
    source $VENV_NAME/bin/activate

    # Chạy Django server trong nền
    nohup python3 manage.py runserver $ADDRESS:$PORT > /dev/null 2>&1 &
    echo "Django server đã bắt đầu."
}

stop() {
    cd $PROJECT_DIR

    # Tìm và kết thúc quá trình Django server
    pkill -f "python3 manage.py runserver $ADDRESS:$PORT"
    echo "Django server đã dừng."
}

# Xử lý tham số dòng lệnh
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
        echo "Sử dụng: $0 {start|stop}"
        exit 1
        ;;
esac

exit 0
