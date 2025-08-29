#!/usr/bin/env python3
"""
AI Coding Assistant Runner
Sử dụng để chạy AI Coding Assistant với input từ người dùng
"""

import sys
import os

# Thêm src vào Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from coding_assistant import AICodingAssistant
import sys

def main():
    """Main function để chạy AI Coding Assistant"""
    
    print("🤖 AI Coding Assistant")
    print("=" * 50)
    
    try:
        # Khởi tạo AI Coding Assistant
        assistant = AICodingAssistant()
        print("✅ Assistant initialized successfully!")
        
        # Hiển thị thông tin rate limit
        rate_info = assistant.get_rate_limit_info()
        print(f"\n📊 Rate Limit Info:")
        print(f"   - Model: {rate_info['current_model']}")
        print(f"   - Free tier: {rate_info['free_tier_limits']['requests_per_minute']} requests/phút")
        print(f"   - Daily limit: {rate_info['free_tier_limits']['requests_per_day']} requests/ngày")
        
        # Hiển thị files hiện có
        existing_files = assistant.get_output_files()
        if existing_files:
            print(f"\n📁 Existing files in outputs: {', '.join(existing_files)}")
        else:
            print("\n📁 No existing files in outputs directory")
        
        # Nhận input từ người dùng
        print("\n💡 Enter your coding request (or 'quit' to exit):")
        print("Examples:")
        print("- Tạo function Python để tính giai thừa")
        print("- Tạo class JavaScript để quản lý todo list")
        print("- Tạo file HTML với form đăng ký")
        print("- Tạo script Python để crawl website")
        
        while True:
            try:
                user_input = input("\n🎯 Your request: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not user_input:
                    print("❌ Please enter a valid request")
                    continue
                
                # Tạo code theo yêu cầu
                print(f"\n🔄 Processing: {user_input}")
                result = assistant.create_code(user_input)
                
                if "error" in result:
                    if result.get("error") == "rate_limit_exceeded":
                        print(f"⏳ {result.get('message', 'Rate limit exceeded')}")
                        print("💡 Tips:")
                        print("   - Đợi 1-2 phút và thử lại")
                        print("   - Sử dụng ít requests hơn")
                        print("   - Upgrade lên paid plan nếu cần")
                    else:
                        print(f"❌ Error: {result.get('message', 'Unknown error')}")
                else:
                    print(f"✅ Success! Output: {result.get('output', 'Code created successfully')}")
                    
                    # Hiển thị files mới tạo
                    new_files = assistant.get_output_files()
                    if len(new_files) > len(existing_files):
                        new_file = [f for f in new_files if f not in existing_files][0]
                        print(f"📄 New file created: {new_file}")
                        
                        # Hiển thị nội dung file
                        print(f"\n📝 File content:")
                        print("-" * 40)
                        content = assistant.read_file(new_file)
                        print(content)
                        print("-" * 40)
                        
                        existing_files = new_files
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                
    except Exception as e:
        print(f"❌ Failed to initialize assistant: {e}")
        print("Make sure you have set GEMINI_API_KEY in your .env file")
        sys.exit(1)

if __name__ == "__main__":
    main() 