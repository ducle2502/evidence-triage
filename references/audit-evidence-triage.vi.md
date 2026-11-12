# Sàng lọc bằng chứng kiểm toán

Sàng lọc bằng chứng để xác định mỗi mục chứng minh được gì, mục nào cần đối chứng và mục nào còn thiếu. Đây không phải việc xếp hạng mức độ đáng ngờ của tệp. Đây là phép thử mức độ phù hợp giữa bằng chứng và luận điểm.

Dùng tệp này sau `audit-evidence-model.vi.md`. Dùng `audit-evidence.vi.md` cho các kiểm tra nền về tính đầy đủ, tính liên quan và độ tin cậy.

## Hai câu hỏi

Đặt hai câu hỏi riêng:

1. **Kiểm tra bằng chứng.** Mục này có dùng được theo tiêu chuẩn của chính nó không?
2. **Kiểm tra luận điểm.** Tập bằng chứng này có chống đỡ được đúng luận điểm không?

Một tài liệu xác thực vẫn có thể không đạt kiểm tra luận điểm vì sai kỳ. Một kết luận đúng vẫn có thể không đạt vì tập bằng chứng không phủ đủ. Không gộp hai câu hỏi thành một điểm tin cậy.

| Kiểm tra bằng chứng | Kiểm tra luận điểm |
| --- | --- |
| Có liên quan đến mục tiêu không? | Tập bằng chứng có phủ mọi phần của luận điểm không? |
| Có hiện hành tại mốc chốt không? | Loại bằng chứng có chứng minh được luận điểm này không? |
| Nguồn có đủ tin cậy và độc lập không? | Mẫu và tổng thể có đủ để khái quát không? |
| Có thể tái lập hoặc kiểm tra lại không? | Từng phần có được trích dẫn không? |
| Phạm vi của mục có rõ không? | Có bằng chứng phản bác không, và đã xử lý chưa? |

## Bộ tiêu chí sàng lọc

Chấm từng mục hoặc luận điểm trọng yếu theo các chiều dưới đây. Dùng thang do hồ sơ cuộc kiểm toán quy định. Câu hỏi quan trọng hơn nhãn.

| Chiều | Câu hỏi | Lỗi thường gặp |
| --- | --- | --- |
| Liên quan | Có liên quan đến mục tiêu, tổng thể và kỳ không? | Tài liệu tốt nhưng sai đơn vị |
| Độ tin cậy | Nguồn và cách thu thập có đáng tin không? | Ảnh chụp không có truy vấn hoặc tham số |
| Tính thời sự | Có hiện hành tại mốc chốt không? | Ảnh chụp xu hướng dùng làm trạng thái hiện tại |
| Khả năng kiểm chứng | Người khác có tái lập hoặc kiểm tra được không? | Bản tóm tắt không có vị trí nguồn |
| Độ phủ | Có phủ toàn bộ luận điểm hay chỉ một phần? | Một ngoại lệ bị coi là toàn bộ tổng thể |
| Đối chứng | Có nguồn độc lập hoặc mâu thuẫn trọng yếu không? | Lặp lại cùng một nguồn |
| Trọng yếu | Giá trị khác có làm thay đổi quyết định không? | Dùng độ chính xác cho mục không trọng yếu |
| Khả năng hành động | Bước tiếp theo là gì? | Khoảng trống không có người phụ trách hoặc yêu cầu |

## Trạng thái quyết định

Dùng một bộ kết quả thống nhất. Bộ mặc định có thể là:

- **Chấp nhận.** Dùng được cho luận điểm như đã nêu.
- **Chấp nhận kèm giới hạn.** Dùng được, nhưng giới hạn phải đi cùng luận điểm.
- **Yêu cầu cập nhật.** Mục đã cũ hoặc chưa đầy đủ. Đề nghị bản hiện hành.
- **Cần đối chứng.** Chỉ một nguồn, tự báo cáo hoặc có mâu thuẫn. Tìm nguồn độc lập.
- **Khoảng trống.** Thiếu hoặc không truy cập được. Ghi ảnh hưởng đến mức bảo đảm.
- **Ngoài phạm vi.** Không liên quan đến mục tiêu này. Giữ lại nếu trọng yếu cho cuộc kiểm toán khác.
- **Loại bỏ.** Không đáng tin hoặc không đại diện. Không dùng làm căn cứ.

Không dùng "chấp nhận" cho mục chỉ chống đỡ một phần luận điểm. Tách luận điểm hoặc ghi giới hạn.

## Gắn nhãn kép

Với mọi nhãn làm thay đổi quyết định, ghi hai giá trị:

- nhãn theo kế hoạch, theo khai báo hoặc theo ý định.
- nhãn theo quan sát, theo thực tế hoặc theo mức đã triển khai.

Chênh lệch là một phát hiện, không phải lỗi cần làm sạch dữ liệu. Không gộp hai nhãn thành một nhãn "cuối cùng" mà không ghi lại khác biệt.

## Bản đồ độ phủ

Giữ bản đồ từ câu hỏi, tiêu chí hoặc khẳng định sang bằng chứng và trạng thái.

Với mỗi dòng, ghi câu hỏi, tiêu chí hoặc khẳng định, mã bằng chứng,
trạng thái, khoảng trống hoặc giới hạn, người phụ trách và hạn.

Bản đồ này cho biết kết luận đã được phủ chưa. Một kết luận có bằng chứng mạnh cho một phần và không có gì cho phần khác là kết luận chưa được phủ.

## Khoảng trống và chỉ tiêu bị chặn

Khoảng trống là một phát hiện, không phải ô trống. Ghi rõ:

- thiếu gì.
- vì sao thiếu: chưa yêu cầu, chưa cung cấp, không truy cập được, không đo được, đã mất hoặc ngoài kỳ.
- ảnh hưởng đến mức bảo đảm nào.
- điều gì sẽ đóng khoảng trống.
- ai phụ trách yêu cầu.
- khi nào kiểm tra lại.

Nếu không đo được, không ghi số 0. Ghi "chưa đo" và nêu lý do. Số 0 bịa còn xấu hơn khoảng trống thừa nhận vì nó trông giống bằng chứng.

## Chỉ tiêu phái sinh và số tổng hợp

Mọi số tổng hợp cần chuỗi nguồn gốc:

```text
trường gốc -> phép biến đổi -> cách nhóm -> số tổng hợp -> câu trong báo cáo
```

Gắn nhãn mọi cách nhóm được suy ra, ánh xạ, nội suy hoặc dựa trên trường trống. Kiểm tra lại số tổng hợp với bản ghi gốc trước khi dùng trong phát hiện. Biểu đồ hay bảng điều khiển giấu cách tính thì không phải bằng chứng cho tổng thể bên dưới.

## Xử lý mâu thuẫn

Khi hai nguồn lệch nhau, không chọn nguồn dễ dùng hơn. So sánh:

1. **Định nghĩa.** Hai nguồn đo cùng một thứ không?
2. **Phạm vi.** Cùng đơn vị, địa điểm và ngoại lệ không?
3. **Mốc chốt.** Cùng kỳ và cùng ngày chốt dữ liệu không?
4. **Mẫu số.** Cùng tổng thể và đơn vị tính không?
5. **Cấp phê duyệt.** Cùng thẩm quyền và trạng thái ký không?
6. **Trạng thái.** Hiện hành, bản nháp, bị thay thế hay chưa xác nhận?

Ghi lại so sánh và quyết định. Nếu không giải quyết được, gắn nhãn luận điểm đang tranh chấp và nêu điều kiện để giải quyết.

## Chống cộng trùng tác động

Trước khi xếp hạng phát hiện theo tác động:

- xác định nhóm đối tượng cùng chịu một rủi ro.
- nêu phát hiện nào dùng chung một nhóm.
- áp dụng quy tắc chống cộng trùng rõ ràng.
- đối chiếu tổng với nhóm.
- tách mức độ nghiêm trọng khỏi độ tin cậy.

Một tổng lớn do cộng các phát hiện chồng lấn không phải rủi ro lớn hơn. Đó là lỗi số học.

## Điểm dừng

Dừng sàng lọc khi bằng chứng mới không còn làm thay đổi quyết định. Luôn có thêm tài liệu để tìm. Phép thử là mục mới có làm thay đổi kết luận, mức xếp hạng, kiến nghị hoặc điều kiện đóng không. Nếu không, ghi là bối cảnh và chuyển tiếp.

## Hồ sơ sàng lọc

Giữ quyết định để người khác kiểm tra:

```markdown
## Quyết định sàng lọc <mã>

- Mục hoặc luận điểm:
- Mã bằng chứng:
- Kết quả kiểm tra bằng chứng:
- Kết quả kiểm tra luận điểm:
- Trạng thái quyết định:
- Giới hạn hoặc khoảng trống:
- Hành động tiếp theo / người phụ trách / hạn:
- Người soát xét:
```

## Điểm cần điều chỉnh

- Phương pháp luận dùng chiều sàng lọc và trạng thái quyết định nào?
- Ai sở hữu bản đồ độ phủ, và bao lâu cập nhật một lần?
- Số tổng hợp nào trọng yếu đến mức cần kiểm tra lại độc lập?
- Mâu thuẫn được báo lên cấp nào?
- Điểm dừng của cuộc kiểm toán này là gì?
