import os
import sentencepiece as spm

class DzongkhaTokenizer:
    def __init__(self, model_type="subword"):
        # Get the path to the models folder inside the package
        self.model_dir = os.path.join(os.path.dirname(__file__), "models")
        self.model_path = os.path.join(self.model_dir, "dzongkha_subword.model")
        
        self.sp = spm.SentencePieceProcessor()
        if os.path.exists(self.model_path):
            self.sp.load(self.model_path)
        else:
            print(f"Warning: Model not found at {self.model_path}")

    def segment_subwords(self, text):
        """Segments text into subwords using SentencePiece."""
        return self.sp.encode_as_pieces(text)

    def segment_tseg(self, text):
        """Segments text based on the traditional Tseg (་)."""
        return text.replace(" ", "").split("་")