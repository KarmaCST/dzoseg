import os

class DzongkhaTokenizer:
    def __init__(self):
        """
        Initializes the tokenizer and loads the 32k unigram model.
        """
        # This matches your 'ls' output exactly
        self.model_path = os.path.join(
            os.path.dirname(__file__), "models", "dzo_unigram_32000.model"
        )
        self.sp = None

        try:
            import sentencepiece as spm
            if os.path.exists(self.model_path):
                self.sp = spm.SentencePieceProcessor(model_file=self.model_path)
            else:
                print(f"Warning: Model not found at {self.model_path}")
        except ImportError:
            print("Warning: 'sentencepiece' library not installed.")

    def segment_tseg(self, text):
        """Splits text by the Dzongkha tseg (་)."""
        if not text:
            return []
        return [s.strip() for s in text.split('་') if s.strip()]

    def segment_subwords(self, text):
        """Uses the 32k unigram model to segment text."""
        if self.sp:
            return self.sp.encode_as_pieces(text)
        return []