from langchain.agents import AgentType, initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from advanced_file_tool import advanced_file_tool
from dotenv import load_dotenv
import os

class AICodingAssistant:
    """
    AI Coding Assistant - Tự động tạo và lưu code files
    """
    
    def __init__(self, api_key: str = None, model: str = "gemini-2.0-flash-exp", temperature: float = 0.1):
        """
        Khởi tạo AI Coding Assistant
        
        Args:
            api_key: Gemini API key (nếu None sẽ load từ .env)
            model: Model Gemini sử dụng
            temperature: Độ sáng tạo của model (0.0 - 1.0)
        """
        load_dotenv()
        
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY in .env file or pass api_key parameter.")
        
        self.model = model
        self.temperature = temperature
        
        # Khởi tạo LLM client
        self.client = ChatGoogleGenerativeAI(
            model=self.model,
            google_api_key=self.api_key,
            temperature=self.temperature
        )
        
        # Prompt cho AI Coding Assistant
        self.prompt = ChatPromptTemplate.from_template("""
        Bạn là một AI Coding Assistant chuyên nghiệp. Nhiệm vụ của bạn là:

        1. **Phân tích yêu cầu**: Hiểu rõ người dùng muốn tạo gì (script, ứng dụng, function, class, etc.)

        2. **Tạo code hoàn chỉnh**: Viết code chất lượng cao, có comment đầy đủ, tuân thủ best practices

        3. **Tự động lưu file**: Sử dụng tool "Advanced File Manager" để tạo file code trong thư mục ./outputs

        4. **Quy tắc đặt tên file**:
           - Python: .py extension
           - JavaScript: .js extension  
           - HTML: .html extension
           - CSS: .css extension
           - JSON: .json extension
           - Text: .txt extension
           - Và các extension khác tùy theo ngôn ngữ

        5. **Cấu trúc file**:
           - Tên file mô tả rõ chức năng
           - Code có comment giải thích
           - Có docstring cho functions/classes
           - Tuân thủ coding standards

        6. **Khi người dùng yêu cầu**:
           - Nếu chỉ yêu cầu code: Tạo file với tên phù hợp
           - Nếu yêu cầu cụ thể: Sử dụng tên file được chỉ định
           - Nếu yêu cầu nhiều file: Tạo từng file riêng biệt

        7. **Trả lời**: Thông báo rõ ràng về file đã tạo, đường dẫn, và chức năng của code

        Hãy bắt đầu với yêu cầu của người dùng!
        """)
        
        # Khởi tạo agent
        self.agent = initialize_agent(
            tools=[advanced_file_tool],
            llm=self.client,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,
            verbose=True
        )
        
        print(f"AI Coding Assistant initialized with model: {self.model}")
    
    def create_code(self, user_request: str) -> dict:
        """
        Tạo code theo yêu cầu của người dùng
        
        Args:
            user_request: Yêu cầu của người dùng (ví dụ: "Tạo function Python tính tổng")
            
        Returns:
            dict: Kết quả từ agent
        """
        try:
            print(f"Processing request: {user_request}")
            result = self.agent.invoke({"input": user_request})
            return result
        except Exception as e:
            error_msg = str(e)
            
            # Xử lý rate limit error
            if "429" in error_msg or "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
                print("⚠️  Rate Limit Warning:")
                print("   - Gemini API có giới hạn 10 requests/phút cho free tier")
                print("   - Vui lòng đợi 1-2 phút và thử lại")
                print("   - Hoặc upgrade lên paid plan để có quota cao hơn")
                print(f"   - Error details: {error_msg}")
                return {
                    "error": "rate_limit_exceeded",
                    "message": "Gemini API rate limit exceeded. Please wait 1-2 minutes and try again.",
                    "details": error_msg
                }
            
            # Xử lý các lỗi khác
            print(f"❌ Error occurred: {error_msg}")
            import traceback
            traceback.print_exc()
            return {
                "error": "general_error", 
                "message": f"An error occurred: {error_msg}",
                "details": error_msg
            }
    
    def get_output_files(self) -> list:
        """
        Lấy danh sách files trong thư mục outputs
        
        Returns:
            list: Danh sách tên files
        """
        outputs_dir = os.path.join(os.path.dirname(__file__), "outputs")
        if os.path.exists(outputs_dir):
            return os.listdir(outputs_dir)
        return []
    
    def read_file(self, filename: str) -> str:
        """
        Đọc nội dung file trong thư mục outputs
        
        Args:
            filename: Tên file (ví dụ: "sum_list.py")
            
        Returns:
            str: Nội dung file
        """
        file_path = os.path.join(os.path.dirname(__file__), "outputs", filename)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return f"File {filename} not found"
    
    def get_rate_limit_info(self) -> dict:
        """
        Lấy thông tin về rate limit của Gemini API
        
        Returns:
            dict: Thông tin rate limit
        """
        return {
            "free_tier_limits": {
                "requests_per_minute": 10,
                "requests_per_day": 1500,
                "model": "gemini-2.0-flash-exp"
            },
            "tips": [
                "Đợi 1-2 phút giữa các requests",
                "Sử dụng ít requests hơn",
                "Upgrade lên paid plan để có quota cao hơn",
                "Sử dụng model khác nếu cần"
            ],
            "current_model": self.model
        } 