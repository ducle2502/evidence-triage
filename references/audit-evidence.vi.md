# Bằng chứng kiểm toán

Bằng chứng kiểm toán là căn cứ để kết luận. Đọc tệp này trước khi ghi nhận bằng chứng ở bất kỳ giai đoạn nào và trước khi bàn giao hồ sơ cho người không tham gia cuộc kiểm toán.

Các khái niệm dưới đây là thực hành kiểm toán nội bộ chung. Tài liệu này không thay thế phương pháp luận của tổ chức hoặc chuẩn mực áp dụng.

## Bằng chứng dùng được

Bằng chứng cần đủ, liên quan và đáng tin cậy. Đủ nghĩa là có đủ lượng để chống đỡ kết luận, xét theo rủi ro và chất lượng bằng chứng. Liên quan nghĩa là bằng chứng gắn với mục tiêu, tổng thể và kỳ đang kiểm tra. Đáng tin cậy nghĩa là nguồn và cách thu thập kiểm chứng được.

Một trích xuất lớn từ dữ liệu không đáng tin không phải bằng chứng đủ. Một trích xuất đáng tin nhưng sai kỳ không trả lời câu hỏi.

## Bằng chứng mạnh hơn

Dùng bằng chứng mạnh nhất có thể. Nêu rõ khi phải dùng bằng chứng yếu hơn.

| Loại bằng chứng | Độ tin cậy | Ghi chú |
| --- | --- | --- |
| Trích xuất hệ thống có truy vấn được ghi lại và đối chiếu nguồn | Cao hơn | Tái lập được và độc lập với người chạy |
| Báo cáo hệ thống có tham số và số dòng rõ | Cao hơn | Lưu cả tham số và kết quả |
| Ảnh chụp hoặc bảng tính xuất khẩu không có truy vấn | Thấp hơn | Khó tái lập và dễ bị sửa |
| Bản tóm tắt thủ công hoặc giải thích bằng lời | Thấp nhất | Dùng làm manh mối, cần đối chứng trước khi dựa vào |

Bằng chứng độc lập thường mạnh hơn bằng chứng từ đơn vị được kiểm toán. Bản gốc thường mạnh hơn bản sao. Hai nguồn độc lập cùng khớp mạnh hơn một nguồn lặp lại.

## Xác định tổng thể

Trước khi kiểm tra, ghi rõ:

- **Phạm vi.** Đơn vị, giao dịch hoặc bản ghi nào được bao gồm.
- **Kỳ.** Ngày bắt đầu và ngày kết thúc, kể cả múi giờ.
- **Bộ lọc.** Mọi nội dung loại trừ và lý do.
- **Nguồn.** Hệ thống, bảng hoặc báo cáo tạo ra tổng thể.
- **Số dòng.** Trước và sau khi lọc.

Tổng thể quyết định phép thử chứng minh được gì. Nếu bỏ sót bản ghi vào muộn, dữ liệu lưu trữ hoặc bút toán điều chỉnh tay, phải nêu rõ.

## Kiểm tra dữ liệu trước khi diễn giải

1. **Đối chiếu số lượng.** So tổng thể với báo cáo nguồn hoặc tổng kiểm soát.
2. **Kiểm tra mốc ngày.** Xác nhận ngày bao gồm, ngày loại trừ, múi giờ và bản ghi đến muộn.
3. **Soát trùng lặp.** Tìm khóa trùng, giao dịch lặp và nhiều bản ghi cho một đối tượng.
4. **Rà giá trị trống và mặc định.** Trường thiếu, giá trị tạm và mốc thời gian mặc định có thể làm sai kết quả.
5. **Đối chiếu phép nối.** Nối nhiều-nối-một và một-nối-nhiều có thể nhân hoặc mất dòng. So số dòng trước và sau.
6. **Lưu truy vấn nguyên trạng.** Lưu tham số, bộ lọc và logic đúng như đã chạy.
7. **Đối chiếu độ lớn.** So tổng, trung bình và phân bố với mốc chuẩn đã biết.

Ghi lại từng bước kiểm tra và kết quả, kể cả kết quả sạch. Bản ghi những gì đã kiểm tra là một phần của bằng chứng.

## Hồ sơ cho bằng chứng từ truy vấn

Mỗi phép thử cần để lại một cặp tệp và một ghi chú ngắn:

- Truy vấn đúng như đã chạy, kèm tham số và môi trường.
- Kết quả, kèm số dòng và mốc thời gian trích xuất.
- Ghi chú nêu mục tiêu, tổng thể, nguồn, bộ lọc, cách diễn giải, giới hạn và kết luận.
- Liên kết từ ghi chú đến tệp truy vấn và tệp kết quả.

Dùng cấu trúc thư mục trong `output-conventions.md`. Nếu kết quả không chạy lại được hoặc không truy được về truy vấn, kết quả đó không phải bằng chứng đứng vững khi bị soát xét.

## Chuỗi bảo quản

- Trích xuất ở chế độ chỉ đọc. Không sửa dữ liệu nguồn.
- Tính mã băm cho trích xuất lớn trước khi chia sẻ hoặc lưu giữ.
- Giữ hồ sơ ở vị trí kiểm soát truy cập. Kho công khai này không phù hợp.
- Ghi ai trích xuất, khi nào và từ đâu.
- Tuân thủ chính sách lưu giữ của tổ chức.

## Giới hạn và thái độ hoài nghi nghề nghiệp

Nêu rõ giới hạn của công việc:

- dữ liệu thiếu hoặc chưa đầy đủ.
- chỉ tiêu thay thế được dùng thay cho thuộc tính thật.
- phép thử không thể thực hiện.
- cách giải thích khác chưa loại trừ.
- giới hạn độ chính xác của ngưỡng và quy tắc đối chiếu.

Kết quả âm nghĩa là phép thử không tìm thấy điều kiện. Kết quả âm không chứng minh điều kiện không tồn tại.

## Mẫu ghi chép

```markdown
## Phép thử <mã>: <tên ngắn>

- Mục tiêu:
- Tổng thể:
- Kỳ:
- Nguồn:
- Bộ lọc và nội dung loại trừ:
- Tệp truy vấn:
- Tệp kết quả:
- Số dòng trước và sau:
- Kiểm tra toàn vẹn dữ liệu:
- Tóm tắt kết quả:
- Cách diễn giải:
- Giới hạn:
- Kết luận:
- Người soát xét:
```

Giữ mẫu đủ ngắn để người khác dùng. Một bản ghi đầy đủ và giản dị tốt hơn một mẫu cầu kỳ không ai điền.

## Từ bằng chứng đến phát hiện

Bằng chứng chống đỡ phát hiện. Trước khi viết kết luận, đọc `audit-findings.vi.md` và tách điều đã quan sát khỏi điều đã suy luận.
