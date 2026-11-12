<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg?v=2">
  <img src="assets/banner.svg?v=2" alt="Banner evidence-triage">
</picture>

# evidence-triage

< [English](./README.md) | Tiếng Việt >

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Version](https://img.shields.io/badge/version-3.0.0-0F172A)
[![CI](https://github.com/ducle2502/evidence-triage/actions/workflows/ci.yml/badge.svg)](https://github.com/ducle2502/evidence-triage/actions/workflows/ci.yml)
![Synthetic data only](https://img.shields.io/badge/data-synthetic%20only-15803D)

Skill phân loại bằng chứng cho nhóm kiểm toán nội bộ: tìm kiểu bất
thường, xếp hạng việc cần xem trước, rồi đi đến kết luận bằng văn bản
cho một nhóm hồ sơ.

> [!IMPORTANT]
> Đây là kho công khai. Không đưa dữ liệu của cơ quan, khách hàng, cá
> nhân, tên hệ thống hoặc bảng nội bộ, ngưỡng đã hiệu chỉnh, hay kết quả
> điều tra thật vào kho. Mọi ví dụ đều là dữ liệu mô phỏng. Xem
> [references/confidentiality.md](references/confidentiality.md).

## Vì sao

Khi nhận một yêu cầu mơ hồ, trợ lý AI thường chạy truy vấn theo nhiều
hướng rồi trả về những quan sát trông lạ nhưng không chứng minh được
điều gì. Công việc kiểm toán còn khó hơn: kết quả phải đứng vững khi bị
rà soát. Người rà soát sẽ hỏi bạn đã kiểm tra tổng thể nào, chạy truy
vấn gì, và loại trừ khả năng khác ra sao.

Skill trả lời những câu hỏi đó trước khi viết báo cáo:

- Chia công việc thành ba giai đoạn, mỗi giai đoạn có đầu ra riêng.
- Đặt quy tắc để biết khi nào một thuộc tính chung đủ để nối hai đối
  tượng.
- Yêu cầu bằng chứng có thể chạy lại và truy vết được.
- Giữ mọi phiên làm việc trong một thư mục để người rà soát sau có thể
  tiếp tục.

## Cách hoạt động

| Giai đoạn | Câu hỏi | Dùng trong kiểm toán | Đầu ra |
| --- | --- | --- | --- |
| **Hunting** | Chúng ta đang bỏ sót gì? | Nhận diện rủi ro, kiểm toán liên tục, phát hiện bất thường | Truy vấn và tệp trích xuất đưa ra các tổng thể ứng viên |
| **Triage** | Việc gì cần xem trước? | Phân loại ưu tiên ngoại lệ | Danh sách xếp hạng kèm ranh giới nhóm và mức độ rủi ro |
| **Investigation** | Đã xảy ra gì và có chứng minh được không? | Điều tra và lưu hồ sơ | Bộ bằng chứng và kết luận bằng văn bản |

Ba giai đoạn thường chạy theo thứ tự. Bạn có thể bắt đầu ở bất kỳ giai
đoạn nào. Skill đọc yêu cầu, xác định bạn đang ở giai đoạn nào rồi mở
tài liệu tham chiếu tương ứng.

## Phần kiểm toán

Skill nằm trong quy trình kiểm toán và không thay thế kiểm toán viên,
phương pháp luận hay chuẩn mực.

- **Bằng chứng.** Bằng chứng phải đầy đủ, phù hợp và đáng tin cậy.
  Tổng thể phải trọn vẹn. Skill ghi lại truy vấn, tệp trích xuất và các
  bước kiểm tra. Xem
  [references/audit-evidence.md](references/audit-evidence.md).
- **Phát hiện.** Skill tách thực trạng quan sát được khỏi tiêu chí,
  nguyên nhân, ảnh hưởng và kiến nghị. Skill cũng tách dữ kiện, suy luận
  và ý kiến. Xem
  [references/audit-findings.md](references/audit-findings.md).
- **Bảo mật.** Kho công khai chỉ chứa nội dung chung. Tri thức riêng
  của tổ chức để ở nơi tách biệt. Xem
  [references/confidentiality.md](references/confidentiality.md).
- **Phán đoán.** Skill tập hợp bằng chứng và lập luận. Kiểm toán viên
  quyết định, xếp hạng và ký.

Bộ tài liệu báo cáo trong
[references/audit-index.vi.md](references/audit-index.vi.md) mở rộng
phần này sang hồ sơ cuộc kiểm toán, thiết kế báo cáo, rà soát, phát
hành và an toàn công khai.

Nếu tổ chức của bạn có thuật ngữ hoặc phương pháp riêng, hãy dùng
chúng. Phần mặc định ở đây chỉ là điểm bắt đầu.

## Cách kích hoạt

Mô tả công việc bằng ngôn ngữ thường ngày. Ví dụ:

- "Quý này có gì bất thường trong các thay đổi hồ sơ nhà cung cấp?" → hunting
- "Xếp hạng 200 ngoại lệ bút toán này." → triage
- "12 hồ sơ nhà cung cấp này trông có liên quan. Điều tra chúng." → investigation
- "Số lần truy cập bảng thanh toán ngoài giờ tăng vọt tháng trước. Chuyện gì đã xảy ra?" → hunting → triage → investigation
- "Soát các phê duyệt đã bỏ qua người duyệt thứ hai." → investigation

Chỉ cần mô tả công việc. Skill xác định bạn đã có nhóm đối tượng hay
chưa và chuyển đến đúng giai đoạn.

## Cài đặt

Clone kho hoặc tải ZIP từ **Code → Download ZIP** rồi giải nén vào thư
mục cài đặt.

### Claude Code

Cài ở cấp người dùng để dùng trong mọi dự án:

```bash
git clone https://github.com/ducle2502/evidence-triage.git \
  ~/.claude/skills/evidence-triage
```

Hoặc dùng tệp ZIP:

```bash
unzip evidence-triage-main.zip -d ~/.claude/skills/
mv ~/.claude/skills/evidence-triage-main ~/.claude/skills/evidence-triage
```

Khởi động lại Claude Code rồi kiểm tra bằng `/skills`, hoặc thử một câu
hỏi kiểm toán.

Muốn cài cho một dự án, đặt thư mục này trong
`.claude/skills/evidence-triage/` của dự án đó.

### Claude Cowork

Cowork cài gói mở rộng, không cài trực tiếp từng tệp. Nếu chạy Cowork
qua ứng dụng Claude desktop, Cowork đọc cùng thư mục cấp người dùng,
nên hướng dẫn cho Claude Code vẫn dùng được.

Kho chưa có tệp khai báo `.claude-plugin/plugin.json`. Nếu cần cài
dưới dạng gói mở rộng tùy chỉnh, hãy thêm tệp khai báo tối thiểu trong
một bản sao riêng hoặc mở issue.

### OpenAI Codex

Với Codex, cài theo từng kho bằng cách đặt tệp dưới `.agents/skills/`
tại thư mục gốc của kho bạn đang làm việc:

```bash
mkdir -p .agents/skills
git clone https://github.com/ducle2502/evidence-triage.git \
  .agents/skills/evidence-triage
```

Codex tìm các gói này dưới `.agents/skills/` bằng cách đi ngược lên từ
thư mục làm việc.

Cài toàn cục: đăng ký đường dẫn trong `~/.codex/config.toml`:

```toml
[[skills]]
path = "/absolute/path/to/evidence-triage"
enabled = true
```

Gọi `/skills` trong Codex CLI hoặc IDE, hoặc mô tả một tác vụ kiểm
toán.

## Cấu trúc kho

```text
evidence-triage/
├── SKILL.md                       # điểm vào và bộ định tuyến
├── references/
│   ├── hunting.md                 # giai đoạn hunting (tìm kiểu mới)
│   ├── triage.md                  # giai đoạn triage (xếp hạng ngoại lệ)
│   ├── investigation.md           # giai đoạn điều tra (đưa nhóm đến kết luận)
│   ├── linkage-attributes.md      # khi nào thuộc tính chung nối các đối tượng
│   ├── fraud-patterns.md          # các kiểu gian lận phổ biến và dấu hiệu
│   ├── output-conventions.md
│   ├── audit-evidence.md          # chuẩn bằng chứng, hồ sơ, chuỗi bảo quản
│   ├── audit-findings.md          # thực trạng / tiêu chí / nguyên nhân / ảnh hưởng / kiến nghị
│   ├── confidentiality.md         # quy tắc kho công khai và che dữ liệu
│   ├── audit-index.md             # điểm vào bộ tài liệu báo cáo kiểm toán
│   ├── audit-engagement-profile.md
│   ├── audit-evidence-model.md
│   ├── audit-evidence-triage.md
│   ├── audit-claim-and-conclusion.md
│   ├── audit-report-architecture.md
│   ├── audit-drafting-and-style.md
│   ├── audit-review-lenses.md
│   ├── audit-failure-modes.md
│   ├── audit-release-and-issuance.md
│   ├── audit-public-safety.md
│   ├── audit-templates.md
│   └── audit-index.vi.md          # bản tiếng Việt của audit-index
├── assets/                        # banner và ảnh xem trước
├── docs/                          # kiến trúc và thiết lập GitHub
├── scripts/                       # kiểm tra kho
├── .github/                       # biểu mẫu issue, mẫu PR, nhãn, CI
├── README.md
├── README.vi.md
├── AGENTS.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── VISION.md
├── CHANGELOG.md
└── LICENSE
```

## Tùy biến cục bộ

Mỗi nhóm kiểm toán có tín hiệu, lược đồ dữ liệu, ngưỡng và sự cố
riêng. Giữ những nội dung đó ngoài kho này:

1. Đặt chúng trong một kho riêng hoặc thư mục cục bộ như `local/`, đã
   được `.gitignore` loại trừ.
2. Thêm tệp .md cho tín hiệu có tên, lược đồ dữ liệu, kiểu rủi ro,
   ngưỡng và sự cố trước đây.
3. Trỏ tới một gói riêng, hoặc bản sao `SKILL.md` cục bộ, đến các tệp
   đó. Không đưa tên tệp nội bộ vào bảng tham chiếu công khai.
4. Giữ kho công khai ở dạng chung.

Phần tùy biến riêng có thể nằm ở đâu cũng được, miễn ngoài kho này. Không bao giờ commit dữ liệu
thật "tạm thời", vì lịch sử git vẫn giữ lại. Xem
[references/confidentiality.md](references/confidentiality.md).

## Nguồn gốc

Kho này bắt đầu từ
[finic-ai/fraud-investigation-skills](https://github.com/finic-ai/fraud-investigation-skills)
theo giấy phép MIT. Phương pháp ba giai đoạn và các kiểu gian lận đến
từ dự án đó. Bản này định hướng lại công cụ cho kiểm toán nội bộ và bổ
sung phần bằng chứng, phát hiện và bảo mật.

Người duy trì: duke2502.

## Giấy phép

MIT. Xem [LICENSE](LICENSE). Bản quyền gốc thuộc Finic. Phần chỉnh sửa
thuộc duke2502.
