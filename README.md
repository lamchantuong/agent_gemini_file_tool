# LangChain AI Coding Assistant

Dự án sử dụng LangChain và Google Gemini để tạo AI Coding Assistant tự động.

## Cài đặt và Setup

### 1. Cài đặt Dependencies

```bash
# Cài đặt dependencies chung cho toàn bộ dự án
pip install -r requirements.txt
```

### 2. Cấu hình Environment Variables

Tạo file `.env` trong thư mục gốc:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Chạy AI Coding Assistant

```bash
# Chạy coding assistant
python run_coding_assistant.py
```

## Cấu trúc Dự án

```
agent_gemini_file_tool/
├── requirements.txt            # Dependencies
├── README.md                   # Hướng dẫn
├── .gitignore                  # Git ignore
├── coding_assistant.py         # AI Coding Assistant chính
├── advanced_file_tool.py       # Tool quản lý file
├── run_coding_assistant.py     # Script chạy assistant
├── agent_gemini_base_url_fall.py
├── new.py
└── outputs/                    # Thư mục chứa code được tạo
```

## Tính năng

- 🤖 AI Coding Assistant với Google Gemini
- 📁 Tự động tạo và quản lý file code
- 🔧 Hỗ trợ nhiều ngôn ngữ lập trình
- ⚡ Xử lý rate limit thông minh
- 📝 Tạo code chất lượng cao với comments

## Lưu ý

- Gemini API có giới hạn 10 requests/phút cho free tier
- Đợi 1-2 phút giữa các requests để tránh rate limit
- Upgrade lên paid plan để có quota cao hơn

## Troubleshooting

### Lỗi Rate Limit
```
⚠️ Rate Limit Warning:
   - Gemini API có giới hạn 10 requests/phút cho free tier
   - Vui lòng đợi 1-2 phút và thử lại
```

### Lỗi API Key
```
❌ Failed to initialize assistant: Gemini API key is required
```
Giải pháp: Kiểm tra file `.env` và đảm bảo `GEMINI_API_KEY` được set đúng. 