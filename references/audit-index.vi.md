# Tham chiếu Báo cáo Kiểm toán Nội bộ

Đây là điểm vào cho bộ tài liệu báo cáo kiểm toán trong thư mục này. Nội dung dùng chung cho nhiều loại cuộc kiểm toán: tài chính, vận hành, tuân thủ, công nghệ, bảo đảm dự án, bên thứ ba, gian lận và điều tra. Các tệp trình bày mẫu và quy tắc quyết định, không phải một quy trình bắt buộc.

Bản tiếng Anh: [`audit-index.md`](audit-index.md).

Đọc `audit-evidence.vi.md` và `audit-findings.vi.md` trước nếu cần kiến thức nền về bằng chứng và cấu trúc phát hiện. Các tệp còn lại mở rộng nền đó sang sàng lọc bằng chứng, kiểm tra luận điểm, kiến trúc báo cáo, viết, rà soát và phát hành.

## Đọc theo công việc

| Công việc | Bản tiếng Việt | Bản tiếng Anh |
| --- | --- | --- |
| Mở cuộc kiểm toán mới | `audit-engagement-profile.vi.md` | `audit-engagement-profile.md` |
| Tiếp nhận bằng chứng | `audit-evidence-model.vi.md` | `audit-evidence-model.md` |
| Sàng lọc, xếp hạng bằng chứng | `audit-evidence-triage.vi.md` | `audit-evidence-triage.md` |
| Kiểm tra luận điểm và kết luận | `audit-claim-and-conclusion.vi.md` | `audit-claim-and-conclusion.md` |
| Thiết kế báo cáo | `audit-report-architecture.vi.md` | `audit-report-architecture.md` |
| Viết và biên tập | `audit-drafting-and-style.vi.md` | `audit-drafting-and-style.md` |
| Soát xét bản nháp | `audit-review-lenses.vi.md` | `audit-review-lenses.md` |
| Phát hành báo cáo | `audit-release-and-issuance.vi.md` | `audit-release-and-issuance.md` |
| Tra cứu lỗi thường gặp | `audit-failure-modes.vi.md` | `audit-failure-modes.md` |
| Chuẩn bị ví dụ công khai | `audit-public-safety.vi.md` | `audit-public-safety.md` |
| Dùng biểu mẫu | `audit-templates.vi.md` | `audit-templates.md` |
| Kiến thức nền về bằng chứng | `audit-evidence.vi.md` | `audit-evidence.md` |
| Kiến thức nền về phát hiện | `audit-findings.vi.md` | `audit-findings.md` |
| Quy tắc công khai | `confidentiality.vi.md` | `confidentiality.md` |

## Nguyên tắc chung

1. **Bằng chứng đi trước kết luận.** Nêu câu hỏi và tiêu chí trước khi chọn bằng chứng. Không chọn bằng chứng để khớp với kết luận đã có.
2. **Bằng chứng chỉ phù hợp với một luận điểm cụ thể.** Bản trích xuất hệ thống có thể chứng minh số lượng. Văn bản ký duyệt có thể chứng minh thẩm quyền. Biên bản họp chỉ chứng minh cuộc họp đã diễn ra.
3. **Không bịa số.** Chỉ tiêu bị chặn hoặc chưa đo là một phát hiện, không phải số 0. Ghi rõ lý do chặn, bằng chứng còn thiếu và ảnh hưởng đến mức bảo đảm.
4. **Chọn quy trình theo hồ sơ cuộc kiểm toán.** Dùng hồ sơ để chọn loại báo cáo, thang kết luận, độ sâu rà soát, cổng kiểm soát và bộ hồ sơ phát hành.
5. **Giữ lịch sử phiên bản.** Giữ bản cũ và ghi nhận việc thay thế.
6. **An toàn công khai.** Kho này là công khai. Đọc `confidentiality.vi.md` trước khi thêm bất kỳ tên, số, đường dẫn hoặc ảnh chụp nào.
7. **Giữ vai trò chuyên môn.** Tài liệu này chỉ hỗ trợ. Phương pháp luận của tổ chức, chuẩn mực áp dụng, ý kiến pháp lý và cấp phê duyệt vẫn là căn cứ cuối cùng.

## Giọng văn

- Mở bằng kết luận hoặc số liệu.
- Mỗi đoạn một đến hai câu. Câu trung bình 15 đến 24 chữ, không quá 35 chữ.
- Nêu tử số, mẫu số và kỳ khi dùng tỷ lệ.
- Tách hoạt động trung gian khỏi đầu ra kiểm chứng.
- Rủi ro tương lai chỉ dùng một lần "có thể", không chồng thêm từ giảm nhẹ.
- Ghi "chưa đủ bằng chứng" khi chưa đủ.
- Không quy kết ý định, không dùng từ kịch tính.

## Cách các tệp liên kết

```text
Hồ sơ cuộc kiểm toán
        |
        v
Mô hình bằng chứng ---> Sàng lọc bằng chứng ---> Luận điểm và kết luận
                                                       |
                                                       v
                                            Kiến trúc báo cáo ---> Viết
                                                       |                 |
                                                       v                 v
                                                 Soát xét <--- Lỗi thường gặp
                                                       |
                                                       v
                                            Phát hành báo cáo
                                                       |
                                                       v
                                            An toàn công khai
```

Sơ đồ chỉ một đường đi thường gặp, không phải trình tự bắt buộc. Mỗi cuộc kiểm toán có thể bắt đầu ở một tệp bất kỳ, quay lại hoặc chỉ dùng một phần.

## Điểm cần điều chỉnh

- Tệp nào là bắt buộc theo phương pháp luận của tổ chức?
- Cuộc kiểm toán dùng loại báo cáo và thang kết luận nào?
- Cần những lăng kính rà soát nào, ở độ sâu nào?
- Cấp phê duyệt yêu cầu những cổng và hồ sơ nào?
- Ngôn ngữ và quy ước trích dẫn nào được áp dụng?
