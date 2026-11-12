# An toàn công khai

Quy tắc chuyển kinh nghiệm kiểm toán thật thành ví dụ công khai mà không lộ thông tin mật. Đọc `confidentiality.vi.md` trước. Tệp này áp dụng quy tắc đó cho tài liệu báo cáo kiểm toán.

Kho này là công khai. Mọi thứ đã đưa lên đều ai cũng đọc được, kể cả trong lịch sử phiên bản. Xóa ở lần sửa sau không thu hồi được.

## Quy tắc

Không công bố thông tin có thể nhận diện:

- đơn vị chủ quản, khách hàng hoặc đối tác
- cá nhân, tài khoản, nhà cung cấp hoặc giao dịch
- hệ thống, ứng dụng, mô-đun, bảng hoặc lược đồ đang vận hành
- chương trình, dự án, sự cố hoặc cuộc điều tra
- ngưỡng, quy mô tổng thể hoặc cấu hình kiểm soát mô tả môi trường thật
- quan điểm pháp lý hoặc quy định có thể gắn với một vụ việc cụ thể.

Bài học nào chỉ kể được khi nêu một trong các thông tin trên thì phải trừu tượng thêm, hoặc bỏ.

## Nội dung bị cấm

- Tên tổ chức, công ty mẹ, công ty con hoặc khách hàng.
- Tên dự án, chương trình, hệ thống, nhà cung cấp hoặc sản phẩm.
- Mã nội bộ, tiền tố phiếu, tiền tố bằng chứng hoặc quy ước đặt tên phản ánh môi trường thật.
- Ngày, số tiền, số lượng, tỷ lệ, ngưỡng hoặc quy mô thật.
- Dấu vết sự cố: tổ hợp thời gian, hệ thống, lỗi và tác động đủ để nhận diện.
- Tên cá nhân, chức danh gắn với một người, địa chỉ email, số điện thoại hoặc mã tài khoản.
- Đường dẫn nội bộ, thư mục chia sẻ, ổ đĩa hoặc mã tài liệu.
- Ảnh chụp, biểu trưng, sơ đồ tổ chức, bìa báo cáo hoặc bảng trích xuất.
- Trích dẫn pháp luật, số hiệu văn bản hoặc quy trình riêng của một khu vực tài phán.
- Thông tin đăng nhập, mã thông báo, chuỗi kết nối hoặc tên máy chủ.

## Nội dung được phép

- Khung và chuẩn công khai, được diễn giải và trích dẫn.
- Khái niệm kiểm soát và kỹ thuật kiểm toán chung.
- Ví dụ tổng hợp, ghi rõ là tổng hợp.
- Mẫu cấu trúc không tiết lộ môi trường cụ thể.
- Quan sát tổng hợp không truy ngược được về một tổ chức.
- Ví dụ ghép từ nhiều bối cảnh.

## Cách trừu tượng hóa

Khi cần ví dụ:

1. **Đổi ngành.** Chuyển ví dụ sang ngành, quy trình hoặc loại kiểm soát khác.
2. **Đổi đơn vị.** Dùng tổ chức chung, không dùng tổ chức thật.
3. **Thay đổi quy mô.** Không giữ số lượng, số tiền hoặc tỷ lệ thật.
4. **Dịch chuyển thời gian.** Không giữ ngày, thời lượng hoặc trình tự nếu có thể nhận diện.
5. **Trừu tượng hóa hệ thống.** Mô tả kiểm soát, không mô tả sản phẩm.
6. **Bỏ chi tiết vai.** Dùng vai chung, không dùng chức danh gắn với một người.
7. **Ghép đặc điểm.** Tạo tổ hợp không trùng với một cuộc kiểm toán thật.
8. **Bỏ tổ hợp nhận diện.** Nhiều chi tiết vô hại khi đứng riêng có thể nhận diện khi ghép lại.

## Xóa siêu dữ liệu

Trước khi công bố một tệp:

- xóa tên người tạo và ngày sửa cuối
- xóa bình luận và theo dõi sửa
- bỏ thuộc tính tài liệu và trường tùy chỉnh
- gỡ ảnh và tệp đính kèm nhúng
- bỏ trang ẩn, dòng ẩn và cột ẩn
- kiểm tra nội dung hiển thị không còn đường dẫn hoặc mã định danh
- kiểm tra cả tên tệp và tên thư mục.

Thân tệp sạch nhưng tên tệp lộ thông tin vẫn là công bố thông tin mật.

## Quét từ khóa cấm

Lập danh sách từ khóa riêng, không công khai. Danh sách gồm:

- tên tổ chức và công ty mẹ
- tên dự án, chương trình và hệ thống
- nhà cung cấp và sản phẩm
- tiền tố mã nội bộ
- tiêu đề báo cáo nội bộ
- đường dẫn thư mục nguồn
- số hiệu sự cố, ngày và số tiền cụ thể
- tên cá nhân liên quan.

Chạy quét trước mỗi lần commit. Không đưa danh sách từ khóa vào kho công khai.

## Đọc thủ công

Quét tự động bỏ sót ngữ cảnh. Đọc từng tệp như thể bạn là người soát xét pháp lý hoặc tuân thủ của tổ chức. Hỏi:

- Người đọc có nhận diện được tổ chức từ tổ hợp chi tiết không?
- Có thể nhận diện cá nhân hoặc hệ thống đang vận hành từ nội dung không?
- Có thể suy ra sự cố mật từ nội dung không?
- Ví dụ này cần thiết hay chỉ để trang trí?
- Ví dụ chung có dạy cùng bài học không?

Nếu câu trả lời cuối là có, dùng ví dụ chung.

## Người soát xét thứ hai

Trước khi commit:

1. Người soát xét thứ hai đọc bản sửa đổi công khai, không chỉ tên tệp.
2. Danh sách từ khóa và các câu hỏi đọc thủ công được kiểm tra lại.
3. Xác nhận được ghi vào hồ sơ nội bộ, không ghi vào nội dung công khai.
4. Nếu chưa chắc, bỏ hoặc trừu tượng thêm.

## Tuyên bố công khai

Dùng câu ngắn, chính xác:

> Đây là các bài học tổng hợp từ quá trình lập báo cáo kiểm toán nội bộ. Ví dụ đã được hư cấu và không mô tả một tổ chức, cá nhân, hệ thống hoặc cuộc kiểm toán cụ thể.

Không nêu tên khách hàng, khu vực tài phán hoặc sự cố cụ thể. Không ngụ ý ví dụ là thật.

## Lịch sử phiên bản

Nếu thông tin mật đã được đưa lên:

1. Dừng commit.
2. Coi đây là sự cố bảo mật.
3. Thông báo đầu mối bảo mật hoặc tuân thủ qua kênh đã duyệt.
4. Xóa nội dung khỏi thư mục làm việc, lịch sử commit và bản trên máy chủ từ xa theo chỉ dẫn.
5. Đổi mọi thông tin đăng nhập đã lộ.
6. Tuân thủ quy trình sự cố và báo cáo của tổ chức.

Xóa tệp ở một commit sau không xóa khỏi lịch sử. Coi mọi thứ đã đưa lên kho công khai là đã lộ.

## Danh mục trước khi công bố

- [ ] Không có tên tổ chức, dự án, hệ thống, nhà cung cấp hoặc sản phẩm.
- [ ] Không có người, tài khoản, nhà cung cấp hoặc giao dịch thật.
- [ ] Tránh ngày, số tiền, số lượng, tỷ lệ hoặc ngưỡng thật.
- [ ] Không có dấu vết sự cố hoặc tổ hợp nhận diện.
- [ ] Không có đường dẫn nội bộ, địa chỉ email hoặc thông tin đăng nhập.
- [ ] Loại bỏ ảnh chụp, biểu trưng hoặc bảng trích xuất.
- [ ] Ví dụ được ghi rõ là tổng hợp.
- [ ] Đã xóa siêu dữ liệu, bình luận và theo dõi sửa.
- [ ] Quét từ khóa cấm đạt.
- [ ] Đọc thủ công đạt.
- [ ] Người soát xét thứ hai xác nhận.
- [ ] Tuyên bố công khai chính xác.
- [ ] Lịch sử sạch hoặc đang xử lý theo quy trình sự cố.

## Điểm cần điều chỉnh

- Từ khóa nào là nhạy cảm với tổ chức này?
- Ai là người soát xét thứ hai?
- Kênh phê duyệt nào áp dụng trước khi đưa lên công khai?
- Chính sách lưu giữ và xử lý sự cố nào áp dụng?
