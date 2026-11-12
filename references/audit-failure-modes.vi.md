# Các kiểu thất bại thường gặp

Danh mục dưới đây liệt kê cách báo cáo kiểm toán đi sai. Mỗi mục nêu dấu hiệu, lý do, cách sửa và cách phòng ngừa. Dùng danh mục này để tự kiểm tra trước khi viết, rà soát hoặc phát hành.

Danh mục không đầy đủ. Nếu gặp kiểu mới, thêm vào và ánh xạ sang tệp chủ đề liên quan.

## Lỗi bằng chứng

| Lỗi | Dấu hiệu | Vì sao sai | Cách sửa | Phòng ngừa |
| --- | --- | --- | --- | --- |
| Dùng tên tệp làm dữ liệu | Số chỉ có trong tên tệp hoặc tên thư mục | Nội dung có thể nói khác | Mở nguồn và kiểm tra | Coi siêu dữ liệu là chỉ dẫn, không phải bằng chứng |
| Dùng bản cũ | Bản làm việc cũ hơn nguồn | Báo cáo mô tả trạng thái đã bị thay thế | Đối chiếu mã băm và lịch sử nguồn | Ghi nguồn và mốc chốt |
| Nhầm nguồn | Hai bản cùng tài liệu khác nhau | Có thể trích dẫn sai bản | Đăng ký phiên bản mới và đánh dấu bản cũ | Sổ bằng chứng chỉ bổ sung |
| Dùng tài liệu tự soạn | Chỉ có tài liệu của đơn vị được kiểm toán | Chứng minh lời khẳng định, không chứng minh sự việc | Tìm nguồn độc lập hoặc nguồn hệ thống | Áp dụng phép thử cấp nguồn |
| Coi biên bản họp là tiến độ | Biên bản ghi thảo luận, không ghi kết quả | Hoạt động bị nhầm là kết quả | Kiểm tra hành động trong hệ thống hoặc đầu ra | Tách thảo luận, quyết định, hành động và kết quả |
| Dùng chỉ tiêu phái sinh | Cách nhóm dựa trên trường trống, ánh xạ hoặc nội suy | Số tổng hợp trông như dữ liệu gốc | Truy nguồn và kiểm tra lại bản ghi | Yêu cầu chuỗi nguồn cho mọi số tổng hợp |
| Cộng trùng | Cùng một rủi ro bị đếm trong nhiều phát hiện | Tổng phóng đại rủi ro | Xác định nhóm và quy tắc chống cộng trùng | Đối chiếu tổng với nhóm |
| Ghi số 0 cho chỉ tiêu bị chặn | Không đo được nhưng báo cáo 0 | Số 0 trông như kết quả sạch | Ghi "chưa đo" kèm lý do | Coi chỉ tiêu bị chặn là trạng thái riêng |
| Thiếu mẫu số | Tỷ lệ không có tổng thể hoặc mẫu | Người đọc không đánh giá được | Nêu tử số, mẫu số, kỳ và đơn vị | Dùng mẫu tỷ lệ |
| Độ chính xác giả | Số có nhiều chữ số thập phân hơn nguồn | Tạo cảm giác chính xác không có thật | Làm tròn theo nguồn hoặc dùng khoảng | Khớp độ chính xác với bằng chứng |
| Giấu khoảng trống | Khoảng trống đã biết không được nêu | Kết luận trông đầy đủ hơn thực tế | Nêu khoảng trống và ảnh hưởng | Giữ sổ khoảng trống |
| Kết luận vượt bằng chứng | Kết luận rộng hơn tập bằng chứng | Không bảo vệ được phát hiện | Thu hẹp luận điểm hoặc mở rộng bằng chứng | Chạy kiểm tra luận điểm |
| Vượt nhân quả | Trình tự bị trình bày như nguyên nhân | Nhầm tương quan với nhân quả | Nêu cơ chế và kiểm tra phương án khác | Dùng chuỗi sự kiện và phép thử bác bỏ |
| Gộp nhánh | Nhiều nguyên nhân độc lập bị ghép thành một chuỗi | Câu chuyện gọn hơn bằng chứng | Tách nhánh và ghi trạng thái từng nhánh | Không gộp khi thiếu cơ chế |
| Không có điều kiện bác bỏ | Không bằng chứng nào làm kết luận yếu đi | Kết luận không thể kiểm chứng | Nêu điều kiện làm thay đổi kết luận | Chạy kiểm tra đảo kết luận |
| So sánh kỳ không tương đương | Hai kỳ khác phạm vi hoặc phương pháp | Xu hướng là sản phẩm của cách đo | Chuẩn hóa kỳ hoặc nêu giới hạn | Kiểm tra khả năng so sánh trước khi so |

## Lỗi luận điểm và kết luận

| Lỗi | Dấu hiệu | Vì sao sai | Cách sửa | Phòng ngừa |
| --- | --- | --- | --- | --- |
| Lẫn thực tế và suy luận | Suy luận được viết như quan sát | Người đọc không biết đâu là chứng minh | Gắn nhãn thực tế, suy luận, kịch bản | Dùng cột loại luận điểm |
| Lẫn nguyên nhân và triệu chứng | Kiến nghị chỉ xử lý triệu chứng | Điều kiện tái diễn | Tách nguyên nhân trực tiếp, gốc, đóng góp | Dùng bảng nguyên nhân |
| Gọi xử lý bề mặt là gốc | Hành động chỉ xóa biểu hiện | Cơ chế nền vẫn còn | Xác định lỗi kiểm soát và cơ chế | Hỏi vì sao đến khi hết bằng chứng |
| Nêu nguyên nhân gốc chưa chứng minh | Giả thuyết được trình bày như đã xác nhận | Phát hiện dễ bị phản biện | Giữ trạng thái chưa đủ bằng chứng | Ghi mức độ sâu bằng chứng |
| Quy kết ý định | Báo cáo ngụ ý hành vi cố ý | Không công bằng và có rủi ro pháp lý | Mô tả hành vi và lỗi kiểm soát | Yêu cầu bằng chứng cho ý định |
| Quy lỗi cá nhân | Nêu tên người là nguyên nhân | Bỏ qua điều kiện hệ thống | Phân tích thẩm quyền, đào tạo, khối lượng, kiểm soát | Dùng góc nhìn hệ thống |
| Đánh giá quyết định bằng kết quả | Dùng thông tin sau sự việc để phê bình | Thiên lệch nhìn lại | Đánh giá theo thông tin có tại thời điểm | Ghi rõ tập thông tin |
| Không xét phương án khác | Chỉ có một cách giải thích | Bỏ sót yếu tố gây nhiễu | Liệt kê và kiểm tra phương án khác | Dùng bảng bác bỏ |

## Lỗi báo cáo

| Lỗi | Dấu hiệu | Vì sao sai | Cách sửa | Phòng ngừa |
| --- | --- | --- | --- | --- |
| Chôn kết luận | Phải đọc đến cuối mới thấy câu trả lời | Người quyết định không hành động được | Đưa kết luận và đề nghị lên đầu | Dùng phần quyết định |
| Đưa mã kỹ thuật vào thân bài | Thân bài đọc như nhật ký thao tác trên hệ thống | Người đọc mất thông điệp | Chuyển mã sang bản đồ nguồn hoặc phụ lục | Lọc thuật ngữ |
| Tỷ lệ tích cực che điều kiện bắt buộc | Nêu tỷ lệ hoàn thành cao, bỏ cổng bắt buộc | Người đọc có thể phê duyệt sai | Nêu cả tỷ lệ và điều kiện bắt buộc | Dùng bảng cổng |
| Coi hoạt động là hoàn thành | Cuộc họp, tài liệu hoặc đào tạo được tính là xong | Kết quả chưa được xác minh | Tách hoạt động, đầu ra, kết quả, bảo đảm | Dùng phép thử đóng |
| Tác động chung chung | "Tạo rủi ro" mà không có đường truyền | Người đọc không ưu tiên được | Nêu đường truyền, độ trễ, khả năng đảo ngược | Dùng chuỗi tác động |
| Kiến nghị không có căn cứ | Hành động không có chủ, không khả thi, không đo được | Không thể đóng | Thêm chủ, hạn, tiêu chí, bằng chứng, người xác nhận | Dùng mẫu kiến nghị |
| Không có bằng chứng đóng | Chấp nhận lời khẳng định | Phát hiện có thể tái diễn | Xác định bằng chứng chứng minh khắc phục | Yêu cầu xác nhận độc lập |
| Phụ thuộc phụ lục | Thân bài không hiểu được nếu thiếu phụ lục | Báo cáo không tự đứng | Đưa lập luận thiết yếu vào thân bài | Chạy phép thử tự đứng |
| Số không nhất quán | Cùng chỉ tiêu khác nhau giữa tài liệu | Mất niềm tin | Dùng một nguồn và một phép đối chiếu | Kiểm tra chéo tài liệu |
| Tên đơn vị thay đổi | Cùng đơn vị có nhiều tên | Không rõ ai chịu trách nhiệm | Định nghĩa tên lần đầu và dùng nhất quán | Kiểm tra tên |
| Báo cáo quá tải | Mọi chi tiết nằm ở thân bài | Khó tìm quyết định | Chuyển chi tiết sang phần giải thích và phần kiểm chứng | Áp dụng nguyên tắc người đọc trước |

## Lỗi rà soát

| Lỗi | Dấu hiệu | Vì sao sai | Cách sửa | Phòng ngừa |
| --- | --- | --- | --- | --- |
| Người soát xét sửa kết luận | Người soát xét viết lại phát hiện | Chủ sở hữu mất trách nhiệm | Ghi ngoại lệ, để chủ sở hữu quyết định | Tách soát xét khỏi sở hữu |
| Một người soát mọi thứ | Cùng người kiểm tra số, nhân quả, ngôn ngữ và gói | Không đủ chuyên môn và chú ý | Giao lăng kính độc lập | Dùng danh mục lăng kính |
| Không kiểm tra bác bỏ | Chỉ hỏi "có được chống đỡ không" | Kết luận yếu vẫn sống | Chạy kiểm tra đảo kết luận | Thêm lăng kính phản biện |
| Không mô phỏng phản biện | Nhóm giả định báo cáo sẽ được chấp nhận | Không chuẩn bị cho chất vấn | Mô phỏng công bố và phản biện | Thêm lăng kính phản biện |
| Không xét hệ quả ngoài ý muốn | Kiến nghị tạo rủi ro mới | Cách sửa thành vấn đề tiếp theo | Kiểm tra tác động bậc hai | Thêm lăng kính hệ quả |
| Soát xét trùng lặp | Nhiều người đọc cùng phạm vi | Tốn công mà không thêm bảo đảm | Giao phạm vi khác nhau | Lập kế hoạch theo lăng kính |
| Không có hồ sơ | Không chứng minh được đã soát gì | Soát xét không kiểm toán được | Ghi lăng kính, phạm vi, kết quả, bằng chứng, người soát | Dùng bảng điểm soát xét |

## Lỗi phát hành

| Lỗi | Dấu hiệu | Vì sao sai | Cách sửa | Phòng ngừa |
| --- | --- | --- | --- | --- |
| Lệch phiên bản | Báo cáo và gói khác phiên bản | Người đọc dùng sai tệp | Tạo lại gói từ nguồn đã duyệt | Ghi phiên bản vào bản kê |
| Trùng thư trình | Có hai thư trình | Người nhận hành động sai bản | Giữ một thư trình mỗi phiên bản | Dọn thư mục phát hành |
| Đường dẫn cục bộ | Tệp trỏ đến thư mục cá nhân hoặc tạm | Lộ thông tin và hỏng với người nhận | Thay bằng liên kết ổn định, đúng quyền | Quét đường dẫn |
| Công thức chưa tính lại | Bảng tính hiện giá trị cũ | Số báo cáo sai | Tính lại và kiểm tra giá trị đã lưu | Thêm bước kiểm tra công thức |
| Tràn trang | Bảng hoặc tiêu đề chạy khỏi trang | Báo cáo không đọc được trên bản in | Kết xuất lại và sửa bố cục | Kiểm tra từng trang |
| Thiếu mã băm | Bản kê không có mã băm | Không kiểm tra được toàn vẹn | Thêm mã băm và kiểm tra lại | Dùng mẫu bản kê |
| Sửa sau phê duyệt | Nội dung đổi sau khi ký | Bản phát hành không phải bản đã duyệt | Tạo phiên bản mới và duyệt lại | Khóa tệp đã duyệt |
| Sót dữ liệu nhạy cảm | Còn siêu dữ liệu, bình luận hoặc theo dõi sửa | Lộ thông tin mật | Xóa siêu dữ liệu và soát lại | Kiểm tra bảo mật trước phát hành |

## Lỗi quản trị

| Lỗi | Dấu hiệu | Vì sao sai | Cách sửa | Phòng ngừa |
| --- | --- | --- | --- | --- |
| Quy trình quá cứng nhắc | Phương pháp áp đặt sẵn số bước, số cổng hoặc phần cố định | Không phù hợp cuộc kiểm toán | Dùng hồ sơ để chọn mẫu | Giữ quy trình cấu hình được |
| Coi số kế hoạch là sự thật | Mục tiêu tự báo cáo được dùng như kết quả | Báo cáo lặp lại lời khẳng định chưa kiểm chứng | Kiểm tra nguồn | Tách kế hoạch, thực tế và bằng chứng |
| Đóng theo lời khẳng định | Đơn vị nói đã sửa | Điều kiện có thể còn | Kiểm tra bằng chứng đóng | Yêu cầu xác nhận độc lập |
| Chỉ xử lý lỗi cá nhân | Dừng ở người mắc lỗi | Điều kiện hệ thống còn | Kiểm tra thẩm quyền, đào tạo, khối lượng, kiểm soát | Dùng góc nhìn hệ thống |
| Không có tỷ lệ nền | Kỳ bất thường được coi là xu hướng | Bỏ qua hồi quy về trung bình | So với tỷ lệ nền | Thêm kiểm tra mốc so sánh |
| Không có điểm dừng | Nhóm tiếp tục thu thập bằng chứng | Tê liệt phân tích | Dừng khi bằng chứng mới không đổi quyết định | Đặt ngưỡng quyết định |
| Kết luận có trước | Bằng chứng được chọn để khớp kết luận | Thiên lệch xác nhận | Nêu câu hỏi và tiêu chí trước | Chạy kiểm tra bằng chứng phản bác |
| Khái quát quá mức | Phương pháp trừu tượng đến mức không hướng dẫn được | Người đọc không hành động | Giữ quy tắc quyết định cụ thể và ví dụ | Thử phương pháp trên tình huống thật |
| Lộ thông tin mật | Tên, số hoặc sự cố thật xuất hiện trong ví dụ công khai | Không thể thu hồi | Xóa và xử lý theo quy trình sự cố | Dùng danh mục an toàn công khai |

## Điểm cần điều chỉnh

- Kiểu lỗi nào dễ xảy ra nhất với loại cuộc kiểm toán này?
- Kiểu nào chặn phát hành, kiểu nào chỉ cảnh báo?
- Ai sửa từng lỗi?
- Cách ghi nhận và theo dõi lỗi giữa các cuộc kiểm toán?
