# Biểu mẫu

Sao các biểu mẫu này vào hồ sơ làm việc và điền. Biểu mẫu không chứa dữ liệu thật. Thay mọi phần giữ chỗ bằng thuật ngữ của cuộc kiểm toán, hoặc bỏ trường không áp dụng.

## Hồ sơ cuộc kiểm toán

```markdown
# Hồ sơ cuộc kiểm toán

- Tên cuộc kiểm toán:
- Mục đích:
- Quyết định cần hỗ trợ:
- Người đọc và thứ tự đọc:
- Phạm vi trong:
- Phạm vi ngoài:
- Nhóm tiêu chí và nguồn:
- Kỳ và mốc chốt:
- Đối tượng và tổng thể:
- Nguồn bằng chứng và quyền truy cập:
- Loại báo cáo:
- Hợp đồng ngôn ngữ và văn phong:
- Trọng yếu:
- Thang mức độ:
- Thang kết luận:
- Cấp phê duyệt:
- Mô hình cổng:
- Hồ sơ phát hành:
- Bảo mật và phân phối:
- Giới hạn đã biết:
```

## Sổ đăng ký bằng chứng

Dùng cột của tổ chức nếu đã có. Đây là các nhóm, không phải lược đồ cố định.

```csv
ma_bang_chung,ten,mo_ta,loai_bang_chung,he_thong_nguon,don_vi,ky,phien_ban,ma_bam,vi_tri,nguoi_thu_thap,ngay_thu_thap,trang_thai,vi_tri_trich_dan,gioi_han,ho_so_lien_quan
```

## Sổ yêu cầu bằng chứng

```csv
ma_yeu_cau,cau_hoi_hoac_tieu_chi,bang_chung_can,nguoi_phu_trach,han,trang_thai,ngay_nhan,ma_bang_chung,gioi_han,hanh_dong_tiep
```

Trạng thái: chưa yêu cầu, đã yêu cầu, đã nhận, một phần, chưa đủ, ngoài phạm vi.

## Bản đồ độ phủ

```csv
cau_hoi_hoac_tieu_chi,khang_dinh,ma_bang_chung,trang_thai_do_phu,khoang_trong_hoac_gioi_han,nguoi_phu_trach,han
```

Trạng thái độ phủ: đã phủ, phủ một phần, khoảng trống, ngoài phạm vi.

## Hồ sơ quyết định sàng lọc

```markdown
## Quyết định sàng lọc <mã>

- Mục hoặc luận điểm:
- Mã bằng chứng:
- Kết quả kiểm tra bằng chứng:
- Kết quả kiểm tra luận điểm:
- Trạng thái quyết định:
- Giới hạn hoặc khoảng trống:
- Hành động tiếp theo, người phụ trách, hạn:
- Người rà soát:
```

## Ma trận luận điểm và bằng chứng

```csv
ma_luan_diem,noi_dung_luan_diem,loai_luan_diem,ma_bang_chung,loai_bang_chung,do_phu,doi_chung,do_tin_cay,bang_chung_phan_bac,trang_thai
```

## Hồ sơ phát hiện

```markdown
## Phát hiện <mã>: <tiêu đề ngắn>

- Tiêu chí:
- Thực trạng:
- Nguyên nhân:
- Hệ quả hoặc rủi ro:
- Kiến nghị:
- Người phụ trách:
- Hạn:
- Tiêu chí đóng:
- Bằng chứng đóng:
- Người xác nhận độc lập:
- Mức rủi ro:
- Độ tin cậy:
- Trạng thái:
- Mã bằng chứng:
- Giới hạn:
```

## Chuỗi tác động

| Trường | Nội dung |
| --- | --- |
| Sự kiện | Điều đã xảy ra |
| Tác động trực tiếp | Hệ quả bậc một |
| Cơ chế | Cách tác động lan truyền |
| Bên bị ảnh hưởng | Ai hoặc điều gì bị ảnh hưởng |
| Độ trễ | Khi nào tác động xuất hiện |
| Khả năng đảo ngược | Có thể hoàn tác không, chi phí bao nhiêu |
| Kiểm soát bù trừ | Điều gì làm giảm tác động |
| Hệ quả cuối | Kết quả liên quan đến quyết định |

## Bảng điểm rà soát

```markdown
# Bảng điểm rà soát

| Lăng kính | Phạm vi | Kết quả | Bằng chứng | Ngoại lệ | Hành động | Người rà soát |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Kết quả: đạt, không đạt, có điều kiện.

## Ngoại lệ còn mở

| Mã | Ngoại lệ | Mức độ | Người phụ trách | Hạn | Trạng thái |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Xác nhận

- Người rà soát:
- Ngày:
- Bất đồng còn lại:
```

## Bản kê phát hành

```csv
tep,phien_ban,dinh_dang,dung_luong,ma_bam,nguon,trang_thai,nguoi_phu_trach,ngay_phe_duyet
```

## Thư trình

```markdown
# Thư trình

- Tên báo cáo:
- Phiên bản:
- Quyết định hoặc hành động cần thông qua:
- Kết luận chính:
- Điều kiện hoặc giới hạn:
- Tệp đính kèm:
- Trạng thái phê duyệt:
- Phân phối:
- Khoảng trống đã biết:
```

## Chọn mẫu báo cáo

Dùng một mẫu, không dùng tất cả.

```markdown
# Mẫu báo cáo

- Mẫu: bản ghi nhớ quyết định, báo cáo đầy đủ, bảng điều khiển, thuyết trình, điều tra, theo dõi, hồ sơ pháp lý
- Phần quyết định:
  - Kết luận:
  - Lựa chọn quyết định:
  - Vấn đề chính:
  - Điều kiện:
- Phần giải thích:
  - Tiêu chí:
  - Thực trạng:
  - Nguyên nhân:
  - Hệ quả:
  - Kiến nghị:
- Phần kiểm chứng:
  - Bản đồ nguồn:
  - Phương pháp:
  - Giới hạn:
  - Phụ lục:
```

## Điểm cần điều chỉnh

- Biểu mẫu nào là bắt buộc theo phương pháp luận?
- Trường nào riêng của tổ chức?
- Mã và bộ nhãn trạng thái nào áp dụng?
- Ai rà soát và phê duyệt biểu mẫu đã điền?
