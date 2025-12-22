"""
FelipedelosH
2025

Enter a LONG TEXT and Display in parts.
"""
class TextPaginator:
    def __init__(self, text: str, words_per_page: int = 10):
        self.words_per_page = max(1, int(words_per_page))
        self.set_text(text)

    def set_text(self, text: str):
        self.words = (text or "").split()
        self.index = 0

    def current_page(self) -> str:
        start = self.index
        end = min(len(self.words), start + self.words_per_page)
        return " ".join(self.words[start:end])

    def next_page(self) -> str:
        if self.is_done():
            return ""
        self.index = min(len(self.words), self.index + self.words_per_page)
        return self.current_page()

    def is_done(self) -> bool:
        return self.index >= len(self.words)
    
    def is_last_page(self) -> bool:
        return self.index + self.words_per_page >= len(self.words)
    
    def total_pages(self) -> int:
        if not self.words:
            return 0
        return (len(self.words) + self.words_per_page - 1) // self.words_per_page

    def reset(self):
        self.index = 0
