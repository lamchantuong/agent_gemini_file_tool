from langchain.tools import StructuredTool
import os
from typing import Optional

# ALLOWED_DIR hiển thị cho người dùng (đường dẫn tương đối)
ALLOWED_DIR = "./outputs"
# ACTUAL_DIR là đường dẫn thực tế để tạo file
ACTUAL_DIR = os.path.join(os.path.dirname(__file__), "outputs")

def advanced_file_tool(action: str, file_path: Optional[str] = None, content: Optional[str] = None, directory: Optional[str] = None) -> str:
    """
    Công cụ quản lý file nâng cao
    
    Args:
        action: 'create', 'read', 'write', 'delete', 'list_dir'
        file_path: Đường dẫn file
        content: Nội dung (dùng cho write)
        directory: Thư mục (dùng cho list_dir)
    
    Returns:
        Kết quả thao tác
    """
    try:
        # Tạo thư mục outputs nếu chưa tồn tại
        if not os.path.exists(ACTUAL_DIR):
            os.makedirs(ACTUAL_DIR)
            
        # Chuyển đổi đường dẫn từ ALLOWED_DIR sang ACTUAL_DIR
        if file_path and file_path.startswith(ALLOWED_DIR):
            actual_file_path = file_path.replace(ALLOWED_DIR, ACTUAL_DIR, 1)
        elif file_path and not file_path.startswith(ACTUAL_DIR) and action != 'list_dir':
            return "Lỗi: Đường dẫn file không hợp lệ"
        else:
            actual_file_path = file_path
            
        if action == 'create' or action == 'write':
            if not actual_file_path:
                return "Lỗi: Thiếu file_path"
            mode = 'w' if action == 'create' else 'a'
            
            with open(actual_file_path, mode, encoding='utf-8') as f:
                f.write(content or '')
            return f"Thành công: Đã {'tạo' if mode == 'w' else 'ghi vào'} file {file_path}"
            
        elif action == 'read':
            if not actual_file_path:
                return "Lỗi: Thiếu file_path"
            with open(actual_file_path, 'r', encoding='utf-8') as f:
                return f.read()
                
        elif action == 'delete':
            if not actual_file_path:
                return "Lỗi: Thiếu file_path"
            os.remove(actual_file_path)
            return f"Đã xóa file {file_path}"
            
        elif action == 'list_dir':
            dir_to_list = directory or ACTUAL_DIR
            files = os.listdir(dir_to_list)
            return "\n".join(files)
            
        else:
            return "Hành động không hợp lệ. Chọn: create, read, write, delete hoặc list_dir"
            
    except Exception as e:
        return f"Lỗi: {str(e)}"

# Tạo StructuredTool
advanced_file_tool = StructuredTool.from_function(
    func=advanced_file_tool,
    name="Advanced File Manager",
    description=f"""
    Công cụ quản lý file với các chức năng:
    
    Sử dụng tool này với tên "Advanced File Manager" và các tham số:
    - Tạo file: action='create', file_path='./outputs/tên_file.py', content='nội dung code'
    - Ghi thêm vào file: action='write', file_path='./outputs/tên_file.py', content='nội dung thêm'
    - Đọc file: action='read', file_path='./outputs/tên_file.py'
    - Xóa file: action='delete', file_path='./outputs/tên_file.py'
    - Liệt kê file: action='list_dir', directory='./outputs'
    
    Lưu ý: 
    - Đường dẫn file phải bắt đầu bằng {ALLOWED_DIR}
    - Luôn sử dụng tên tool "Advanced File Manager"
    - Không sử dụng "create" hoặc "write" trực tiếp
    """
)