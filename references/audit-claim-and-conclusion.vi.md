# Luận điểm và kết luận kiểm toán

Kết luận chỉ đứng vững khi luận điểm được kiểm tra bằng loại bằng chứng phù hợp. Đọc tệp này cùng `audit-findings.vi.md`. Tệp đó trình bày cấu trúc phát hiện và mức độ nghiêm trọng. Tệp này trình bày loại luận điểm, độ sâu nhân quả, bằng chứng phản bác và độ tin cậy.

## Loại luận điểm và bằng chứng phù hợp

Mỗi loại luận điểm cần một loại bằng chứng khác nhau. Nêu loại luận điểm trước khi chọn bằng chứng.

| Loại luận điểm | Nội dung khẳng định | Bằng chứng mạnh nhất | Bằng chứng thay thế yếu |
| --- | --- | --- | --- |
| Hiện hữu | Mục đó có tồn tại | Quan sát trực tiếp, bản ghi hệ thống | Danh sách nói mục đó tồn tại |
| Phát sinh | Sự việc đã xảy ra | Nhật ký có mốc thời gian, chứng từ gốc | Bản tóm tắt tường thuật |
| Đầy đủ | Mọi mục đã được bao gồm | Tổng thể đã đối chiếu, tổng kiểm soát | Mẫu không có tổng thể |
| Chính xác | Giá trị đúng | Tính lại, xác nhận độc lập | Số được sao chép |
| Định giá | Giá trị được đo đúng | Mô hình, đầu vào và kiểm tra độc lập | Ước tính của đơn vị |
| Quyền và nghĩa vụ | Đơn vị kiểm soát hoặc có nghĩa vụ | Hợp đồng, ý kiến pháp lý, sổ đăng ký | Lời khẳng định |
| Trình bày | Phân loại và thuyết minh đúng | Tiêu chí và danh mục kiểm tra | Bản nháp |
| Tuân thủ | Quy định đã được chấp hành | Văn bản quy định, ngày hiệu lực, bằng chứng kiểm tra | Bản tóm tắt chính sách |
| Hiệu quả | Kiểm soát vận hành tốt | Kiểm tra thiết kế và vận hành | Một quan sát đơn lẻ |
| Hiệu suất | Nguồn lực được dùng hợp lý | Chi phí, thời gian, đầu ra và mốc so sánh | Ý kiến |
| Nguyên nhân | Vì sao sự việc xảy ra | Chuỗi sự kiện, cơ chế, phản chứng | Câu chuyện hợp lý |
| Tác động | Sự việc thay đổi điều gì | Đường truyền tác động, giá trị chịu rủi ro, độ nhạy | Câu rủi ro chung |
| Dự báo | Điều gì có thể xảy ra | Tỷ lệ nền, xu hướng, giả định, độ nhạy | Ngoại suy từ một kỳ |

Một luận điểm có thể đúng nhưng không được chống đỡ. Một luận điểm có thể được chống đỡ bằng loại bằng chứng không phù hợp. Cả hai đều là lỗi.

## Thực tế, suy luận và kịch bản có điều kiện

Gắn nhãn mọi câu trọng yếu:

- **Thực tế.** Quan sát trực tiếp và truy vết được đến vị trí nguồn.
- **Suy luận.** Kết luận có lý do. Nêu lập luận, phương án khác đã xem xét và điều kiện làm thay đổi kết luận.
- **Kịch bản có điều kiện.** Điều có thể xảy ra nếu một giả định đúng. Nêu điều kiện kích hoạt, cơ chế, độ trễ và khả năng đảo ngược.

Không để suy luận đọc như thực tế. Không để kịch bản đọc như tổn thất đã xảy ra.

## Chuỗi sự kiện

Với luận điểm nhân quả, dựng chuỗi:

1. Trạng thái ban đầu.
2. Thay đổi hoặc sự kiện làm trạng thái khác đi.
3. Sự kiện kích hoạt.
4. Biểu hiện đầu tiên.
5. Lan truyền sang quy trình, bản ghi hoặc đơn vị khác.
6. Biện pháp đã thực hiện.
7. Kết quả sau biện pháp.
8. Kiểm soát đã thất bại.
9. Khoảng trống kiểm soát còn lại.

Nếu thiếu một mắt xích trọng yếu, ghi kết luận chưa đầy đủ. Không lấp khoảng trống bằng câu chuyện hợp lý.

## Chuỗi vì sao

Dùng chuỗi vì sao đến mức bằng chứng cho phép. Mỗi dòng có sáu trường:

| Trường | Câu hỏi |
| --- | --- |
| Câu hỏi và câu trả lời | Đã hỏi gì và kết luận gì? |
| Bằng chứng | Mục nào chống đỡ, ở vị trí nào? |
| Cơ chế | Nguyên nhân này tạo ra hệ quả bằng cách nào? |
| Phương án khác | Còn cách giải thích nào khác? |
| Trạng thái | Đã xác nhận, có chống đỡ, không được chống đỡ hay chưa đủ bằng chứng? |
| Độ sâu | Bằng chứng thực sự đi đến tầng vì sao thứ mấy? |

Dừng ở tầng cuối cùng có bằng chứng trực tiếp. Câu chuyện sâu hơn có thể hấp dẫn. Câu chuyện đó không phải phát hiện.

## Nhóm nguyên nhân

Tách riêng:

- **Nguyên nhân trực tiếp.** Điều kiện trước mắt tạo ra hệ quả.
- **Nguyên nhân gốc.** Cơ chế nền cho phép nguyên nhân trực tiếp tồn tại hoặc tái diễn.
- **Yếu tố đóng góp.** Yếu tố làm tăng khả năng hoặc tác động nhưng không đủ tạo ra hệ quả.
- **Trùng hợp hoặc yếu tố gây nhiễu.** Có liên hệ với hệ quả nhưng không nằm trên đường nhân quả.

Không gộp các nhánh độc lập thành một chuỗi cho gọn. Không gọi biện pháp xử lý bề mặt là xử lý nguyên nhân gốc.

## Bằng chứng phản bác

Với mọi luận điểm trọng yếu, hỏi:

1. Bằng chứng nào sẽ làm luận điểm sai hoặc yếu đi?
2. Đã tìm bằng chứng đó chưa?
3. Nếu tìm thấy, đã xử lý thế nào?
4. Nếu chưa tìm thấy, vì sao?

Một luận điểm không có điều kiện bác bỏ được viết quá mạnh. Ghi lại bằng chứng phản bác và lý do nó có hoặc không làm thay đổi kết luận.

## Yếu tố gây nhiễu và tỷ lệ nền

Trước khi kết luận A gây ra B, kiểm tra:

- A xảy ra trước B không?
- Có cơ chế liên kết A với B không?
- Hiện tượng có lặp lại không?
- Có yếu tố thứ ba giải thích cả A và B không?
- Nếu bỏ A, B có còn xảy ra không?
- Tỷ lệ nền của B là bao nhiêu?
- Thay đổi có phải chỉ là hồi quy về trung bình không?

Một trình tự không phải nguyên nhân. Một kỳ bất thường không phải xu hướng.

## Sổ lập luận

Giữ sổ ngắn cho mỗi kết luận trọng yếu:

- giả thuyết ban đầu.
- bằng chứng ủng hộ và phản bác.
- giả định phải đúng.
- phương án khác đã xem xét và lý do loại bỏ.
- quyết định và người soát xét.

Đây không phải báo cáo. Đây là dấu vết để người soát xét thấy cách kết luận được hình thành, kể cả các nhánh đã bỏ.

## Độ tin cậy và thang kết luận

Tách độ tin cậy khỏi mức độ nghiêm trọng. Một phát hiện tác động cao có thể có độ tin cậy trung bình. Một phát hiện tác động thấp có thể chắc chắn.

Với mỗi kết luận trọng yếu, ghi:

- kết luận.
- mức tin cậy và lý do.
- bằng chứng có sức nặng nhất.
- bằng chứng có thể làm thay đổi kết luận.
- điều kiện sửa đổi kết luận.
- người soát xét chịu trách nhiệm.

Dùng thang kết luận trong hồ sơ cuộc kiểm toán. Ví dụ gồm đạt, cần cải thiện, không đạt. Đây là ví dụ, không phải thang bắt buộc.

## Báo lên chuyên gia

Báo lên khi:

- bằng chứng chưa đủ hoặc mâu thuẫn.
- luận điểm phụ thuộc vào đánh giá pháp lý, thuế, bảo hiểm, kỹ thuật hoặc chuyên môn khác.
- kết luận sẽ nêu tên cá nhân hoặc cáo buộc ý định.
- tác động vượt qua pháp nhân, khu vực tài phán hoặc ranh giới quản lý.

Gắn nhãn cần chuyên gia và nêu rõ câu hỏi chuyên gia phải trả lời.

## Không quy kết ý định

Không kết luận ý định, thông đồng hoặc hành vi cố ý từ một lỗi, một khoảng trống hoặc một ngoại lệ. Mô tả hành vi, lỗi kiểm soát và hệ quả. Nếu ý định là vấn đề trọng yếu, gắn nhãn cáo buộc hoặc câu hỏi chuyên gia và nêu bằng chứng cần có.

## Không quy lỗi cá nhân khi chưa xem hệ thống

Trước khi nêu tên một cá nhân, kiểm tra:

- Người đó có thẩm quyền và được đào tạo không?
- Hệ thống hoặc quy trình có cho phép hành vi đó không?
- Có kiểm soát bù trừ không?
- Khối lượng công việc hoặc thời hạn có phải yếu tố không?
- Điều kiện tương tự có xuất hiện ở nơi khác không?

Phần lớn lỗi vận hành bắt nguồn từ điều kiện hệ thống, không phải từ hành vi cá nhân. Không dùng một cá nhân thay cho phân tích kiểm soát.

## Điểm cần điều chỉnh

- Phương pháp luận dùng loại luận điểm và nhãn kết luận nào?
- Thang độ tin cậy nào được phê duyệt?
- Chuỗi sự kiện phải sâu đến đâu với cuộc kiểm toán này?
- Ai phản biện luận điểm nhân quả và cáo buộc ý định?
- Điều kiện nào kích hoạt tham vấn chuyên gia?
