# Mô hình bằng chứng kiểm toán

Bằng chứng cần được nhận diện, gắn phiên bản, xác định nguồn và theo dõi trong suốt cuộc kiểm toán. Đọc tệp này sau `audit-engagement-profile.vi.md` và cùng với `audit-evidence.vi.md`.

`audit-evidence.vi.md` trình bày tính đầy đủ, tính liên quan, độ tin cậy, tổng thể, kiểm tra dữ liệu và chuỗi bảo quản. Tệp này trình bày phần phía trên: danh tính, vòng đời, tính kịp thời, cấp nguồn và khác biệt giữa yêu cầu với bằng chứng đã nhận.

## Nhóm bằng chứng

Bằng chứng không chỉ là tài liệu. Các nhóm thường gặp:

- Tài liệu: chính sách, quy trình, phê duyệt, biên bản, hợp đồng.
- Trích xuất hệ thống: truy vấn, báo cáo, nhật ký, cấu hình, danh sách truy cập.
- Phỏng vấn và đi thực địa: lời kể về sự việc.
- Quan sát: điều kiện kiểm toán viên trực tiếp thấy.
- Xác nhận: phản hồi từ bên thứ ba hoặc nguồn độc lập.
- Ý kiến pháp lý hoặc ý kiến chuyên gia.
- Bằng chứng vật lý.
- Báo cáo bên ngoài: cơ quan quản lý, kiểm toán độc lập, tư vấn, tổ chức chứng nhận.

Mỗi nhóm chứng minh một loại sự việc khác nhau. Biên bản phỏng vấn chỉ cho biết người ta kể quy trình ra sao. Nó không chứng minh quy trình luôn chạy như vậy.

## Danh tính bằng chứng

Dùng bộ định danh, không dùng tên tệp:

```text
mã băm nội dung + nguồn + đơn vị + kỳ + phiên bản
```

Hệ quả:

- Cùng tên tệp từ hai nguồn có thể là hai tài liệu khác nhau.
- Cùng mã băm từ hai vị trí có thể là cùng một tài liệu.
- Tệp đổi tên không phải tài liệu mới.
- Bản mới cùng tên là một mục bằng chứng mới.
- Bản sao cục bộ không phải nguồn gốc chỉ vì dễ mở hơn.

Gán mã bằng chứng ổn định. Giữ bảng ánh xạ từ mã cục bộ sang sổ chính khi nhiều báo cáo hoặc nhiều nhóm cùng dùng mã riêng.

## Siêu dữ liệu

Tối thiểu cần ghi:

| Nhóm | Trường ví dụ |
| --- | --- |
| Danh tính | Mã bằng chứng, tên, mô tả, phiên bản |
| Nguồn | Hệ thống nguồn, chủ sở hữu, đường dẫn hoặc vị trí, cách thu thập |
| Đơn vị | Pháp nhân, khối, khu vực, đối tác |
| Kỳ | Ngày sự việc, ngày ban hành, ngày thu thập, ngày chốt dữ liệu, ngày hiệu lực |
| Toàn vẹn | Mã băm, dung lượng, định dạng, số trang hoặc số dòng |
| Trạng thái | Hiện hành, bị thay thế, đã ban hành, tham khảo, bản nháp, chưa xác nhận, khoảng trống |
| Truy vết | Vị trí trích dẫn chính xác, hồ sơ làm việc liên quan, phát hiện liên quan |
| Trách nhiệm | Người thu thập, ngày thu thập, người rà soát |
| Giới hạn | Điều bằng chứng không chứng minh được, khoảng trống, hạn chế truy cập |

Tổ chức có thể thêm trường. Không ép một số cột cố định.

## Nhãn trạng thái

Dùng một bộ nhãn thống nhất. Bộ mặc định có thể là:

- **Hiện hành.** Bản có thẩm quyền đang dùng.
- **Bị thay thế.** Đã có bản mới. Giữ lại để tra cứu lịch sử.
- **Đã ban hành.** Đã được cấp có thẩm quyền ký hoặc công bố.
- **Tham khảo.** Có ích để hiểu bối cảnh. Không đủ làm căn cứ duy nhất cho kết luận trọng yếu.
- **Bản nháp.** Chưa được duyệt. Không dùng như bản cuối.
- **Chưa xác nhận.** Chỉ có một nguồn hoặc chưa kiểm chứng. Ghi nhãn rõ.
- **Khoảng trống.** Thiếu, không truy cập được hoặc không đủ. Ghi rõ ảnh hưởng đến mức bảo đảm.

Đây là nhãn mặc định. Ánh xạ sang phương pháp luận của tổ chức.

## Vòng đời chỉ bổ sung

Bằng chứng thay đổi bằng cách bổ sung, không thay thế:

1. Bản mới nhận mã bằng chứng mới.
2. Bản cũ chuyển sang trạng thái bị thay thế, không bị xóa.
3. Giữ bản cũ trong kho bằng chứng.
4. Sổ đăng ký ghi chuỗi thay thế.
5. Báo cáo trích dẫn đúng phiên bản đã dùng.

Không ghi đè tệp, không đồng bộ hai chiều đè lên kho bằng chứng, không "dọn dẹp" bản cũ. Lịch sử là một phần của bằng chứng.

## Nguồn gốc và bản làm việc

Nguồn gốc và bản làm việc có thể lệch nhau. Cần đối chiếu:

1. So mã băm nội dung.
2. Nếu trùng, ghi nhận kết quả kiểm tra.
3. Nếu khác, xem lịch sử phiên bản của nguồn.
4. Khi nguồn mới hơn, đăng ký phiên bản mới.
5. Nếu bản làm việc cũ hơn, ghi giới hạn bản cũ. Không trình bày bản cũ là hiện hành.
6. Nếu không truy cập được nguồn, ghi giới hạn truy cập và nguồn của bản sao.

Bản làm việc chỉ là công cụ. Bản làm việc không phải nguồn có thẩm quyền.

## Các mốc thời gian

Không dùng một trường "ngày" duy nhất. Cần theo dõi:

- **Ngày sự việc.** Thời điểm sự việc xảy ra.
- **Ngày ban hành.** Thời điểm tài liệu được phát hành.
- **Thời điểm thu thập.** Thời điểm kiểm toán viên nhận được.
- **Mốc chốt dữ liệu.** Trạng thái dữ liệu tại thời điểm trích xuất.
- **Mốc hiệu lực.** Thời điểm quy định, phê duyệt hoặc phiên bản bắt đầu có hiệu lực.

Ảnh chụp xu hướng có thể cũ so với mốc chốt nhưng vẫn dùng được để xem hướng đi. Một tài liệu có thể hiện hành nhưng mô tả sự việc cũ. Kết luận phải nêu rõ dùng mốc nào.

Theo dõi cả việc nguồn còn được cập nhật hay đã ngừng. Một nguồn ngừng cập nhật là tín hiệu. Nguồn ngừng cập nhật có thể do đóng băng, bỏ quy trình hoặc công việc đang diễn ra ngoài hệ thống nhìn thấy.

## Cấp nguồn và tính độc lập

Dùng bằng chứng mạnh nhất hiện có. Nếu phải dùng bằng chứng yếu hơn, nêu rõ. Bộ mặc định:

| Cấp | Ví dụ | Mạnh nhất cho |
| --- | --- | --- |
| Hệ thống hoặc máy | Truy vấn có nhật ký, trích xuất, cấu hình, nhật ký truy cập | Số lượng, trạng thái, mốc thời gian, kiểm tra đầy đủ |
| Tài liệu gốc đã ký hoặc ban hành | Phê duyệt, hợp đồng, chính sách, thông báo chính thức | Thẩm quyền, nghĩa vụ, quan điểm chính thức |
| Đối chứng độc lập | Kiểm toán độc lập, cơ quan quản lý, giám sát độc lập, xác nhận | Nguồn mâu thuẫn, tính độc lập |
| Tự báo cáo hoặc tường thuật | Báo cáo tiến độ, biên bản họp, bản tóm tắt nháp | Manh mối và bối cảnh, không phải bằng chứng hoàn thành |
| Khẳng định không nguồn | Lời nói không có ghi chép | Không dùng một mình |

Tài liệu do đơn vị được kiểm toán viết chứng minh điều đơn vị đó khẳng định. Tài liệu này không chứng minh điều khẳng định là đúng. Biên bản họp chứng minh cuộc họp đã được ghi nhận. Biên bản không chứng minh hành động đã hoàn thành.

## Nhu cầu và nguồn cung

Giữ hai sổ liên kết:

1. **Sổ yêu cầu bằng chứng.** Nội dung cần, người cung cấp, thời hạn và trạng thái: chưa yêu cầu, đã yêu cầu, đã nhận, một phần, chưa đủ, ngoài phạm vi.
2. **Sổ đăng ký bằng chứng.** Nội dung đã nhận, danh tính, nguồn, phiên bản, trạng thái, vị trí trích dẫn và giới hạn.

Liên kết hai sổ bằng mã bằng chứng. Không lặp trường. "Một phần" không phải "thiếu". Đó là bằng chứng đã chấp nhận kèm giới hạn.

## Cổng sàng lọc bằng chứng

Trước khi viết hoặc sửa báo cáo:

1. Liệt kê mọi số, tên, ngày và kết luận trọng yếu trong bản nháp.
2. Ánh xạ từng mục sang nguồn gốc và vị trí chính xác.
3. Mở nguồn và kiểm tra giá trị.
4. Ghi kết quả: xác nhận, sửa, hạ cấp hoặc khoảng trống đã biết.
5. Không chuyển sang viết khi còn số trọng yếu chưa có nguồn.

Cổng này ngăn báo cáo mang một con số không ai bảo vệ được.

## Liên hệ với `audit-evidence.vi.md`

Dùng `audit-evidence.vi.md` cho:

- tính đầy đủ, tính liên quan và độ tin cậy.
- xác định tổng thể và kiểm tra tính đầy đủ.
- kiểm tra toàn vẹn dữ liệu.
- hồ sơ truy vấn và kết quả.
- chuỗi bảo quản.
- giới hạn và thái độ hoài nghi nghề nghiệp.

Dùng tệp này cho:

- danh tính và siêu dữ liệu.
- vòng đời và thay thế phiên bản.
- đối chiếu nguồn với bản làm việc.
- tính kịp thời và việc nguồn còn cập nhật hay không.
- cấp nguồn và tính độc lập.
- theo dõi yêu cầu và nguồn cung.
- cổng sàng lọc trước khi viết.

## Điểm cần điều chỉnh

- Phương pháp luận dùng nhóm bằng chứng và nhãn trạng thái nào?
- Trường danh tính nào là bắt buộc?
- Nguồn nào có thẩm quyền cho từng loại bằng chứng?
- Mốc thời gian nào quan trọng với kết luận?
- Cách theo dõi yêu cầu, tiếp nhận và khoảng trống?
- Ai thực hiện cổng sàng lọc và vào thời điểm nào?
