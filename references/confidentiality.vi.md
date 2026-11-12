# Bảo mật

Kho này là công khai. Mọi thứ đã commit đều ai cũng đọc được, kể cả trong lịch sử phiên bản. Đọc tệp này trước khi thêm ví dụ, hồ sơ hoặc hướng dẫn riêng của tổ chức.

## Quy tắc

Không commit dữ liệu của đơn vị chủ quản, khách hàng, người dùng hoặc cá nhân. Không commit bất kỳ nội dung có thể nhận diện tổ chức, cá nhân, hệ thống hoặc môi trường kiểm soát đang vận hành khi chưa được phép.

## Không được commit

- Tên đơn vị chủ quản, khách hàng, sơ đồ tổ chức hoặc tên dự án nội bộ.
- Tên hệ thống, ứng dụng, bảng, cột hoặc lược đồ nội bộ.
- Dữ liệu thật về tài khoản, khách hàng, nhân viên, nhà cung cấp hoặc giao dịch.
- Ngưỡng, tham số điều chỉnh hoặc quy mô tổng thể thật.
- Ảnh chụp công cụ, bảng điều khiển hoặc báo cáo nội bộ.
- Chi tiết sự cố, kết quả điều tra hoặc phát hiện kiểm toán.
- Thuật ngữ nội bộ chưa công khai.
- Thông tin đăng nhập, mã thông báo, chuỗi kết nối hoặc tên máy chủ.

## Được phép commit

- Khung và chuẩn công khai, được trích dẫn và diễn giải.
- Mẫu phân loại và khái niệm kiểm soát chung.
- Ví dụ tổng hợp, ghi rõ là tổng hợp.
- Mẫu cấu trúc không tiết lộ môi trường cụ thể.
- Quan sát tổng hợp không truy ngược được về một tổ chức.

## Giữ tài liệu riêng của tổ chức ở ngoài

Đưa tín hiệu, lược đồ, ngưỡng và vụ việc cũ của nhóm vào:

- kho riêng có kiểm soát truy cập.
- thư mục cục bộ mà `.gitignore` loại trừ, ví dụ `local/`.
- gói tài liệu phân phối qua kênh đã duyệt.

Skill dùng được tài liệu này ở bất kỳ vị trí nào. Tài liệu không cần nằm trong kho này.

Không commit tài liệu riêng "tạm thời" rồi xóa sau. Lịch sử vẫn giữ.

## Che dữ liệu cẩn thận

Khi ví dụ buộc phải giống dữ liệu thật:

- thay mã định danh bằng bí danh ổn định hoặc mã băm.
- dịch ngày theo một hằng số.
- chia số tiền theo một hệ số.
- thay trường văn bản tự do bằng nhóm.
- giảm độ chi tiết, ví dụ dùng khu vực thay cho chi nhánh.
- kiểm tra lại tổ hợp trường còn lại không nhận diện được.

Xóa trường không phải lúc nào cũng xóa rủi ro. Tổ hợp các trường gần định danh có thể dựng lại bản gốc.

## Trước khi commit

- [ ] Không có tên tổ chức, hệ thống, bảng hoặc lược đồ.
- [ ] Không có người, tài khoản, nhà cung cấp hoặc giao dịch thật.
- [ ] Tránh ngưỡng hoặc quy mô tổng thể đang vận hành.
- [ ] Ví dụ tổng hợp được ghi rõ.
- [ ] Không có thông tin đăng nhập, mã thông báo hoặc đường dẫn nội bộ.
- [ ] Đã soát từng dòng thay đổi, kể cả nội dung sửa.
- [ ] Nếu chưa chắc, bỏ ra ngoài.

## Nếu đã commit dữ liệu mật

1. Dừng commit. Coi đây là sự cố bảo mật.
2. Thông báo đầu mối bảo mật hoặc tuân thủ qua kênh đã duyệt.
3. Xóa dữ liệu khỏi thư mục làm việc, lịch sử commit và bản trên máy chủ từ xa theo chỉ dẫn.
4. Đổi ngay mọi thông tin đăng nhập đã lộ.
5. Tuân thủ quy trình sự cố và báo cáo của tổ chức.

Xóa tệp ở một commit sau không xóa khỏi lịch sử. Coi mọi thứ đã đưa lên kho công khai là đã lộ.

## Soát xét

Soát xét tệp này khi mức hiển thị của kho thay đổi hoặc khi có người đóng góp mới. Kho công khai hay không phụ thuộc vào nơi lưu trữ, không phải thiết lập trong tài liệu này.
