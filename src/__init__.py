"""
AI Coding Assistant Package

Package chứa các module chính cho AI Coding Assistant sử dụng LangChain và Gemini.
"""

__version__ = "1.0.0"
__author__ = "AI Coding Assistant Team"

from .coding_assistant import AICodingAssistant
from .advanced_file_tool import advanced_file_tool

__all__ = ["AICodingAssistant", "advanced_file_tool"]
