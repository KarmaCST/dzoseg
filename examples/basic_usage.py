from dzoseg import DzongkhaSegmenter

def main():
    # Initialize the segmenter
    ds = DzongkhaSegmenter()

    # Your specific text
    text = "འབྲུག་རྒྱལ་གཞུང་གཙུག་ལག་སློབ་སྡེའི་འོག་ལུ་ཡོད་པའི་ཚན་རིག་དང་འཕྲུལ་རིག་མཐོ་རིམ་སློབ་གྲྭའི་གློག་རིག་དང་འཕྲུལ་རིག་ལས་ཁུངས།"

    print("--- DZONGKHA SEGMENTATION REPORT ---")
    print(f"Original: {text}\n")

    # AI Subword Segmentation
    subwords = ds.segment_subwords(text)
    print("1. Subword Segmentation (AI-based):")
    print(subwords)
    print(f"Token Count: {len(subwords)}\n")

    # Tseg-based Segmentation
    syllables = ds.segment_tseg(text)
    print("2. Tseg-based Segmentation (Traditional Syllable):")
    print(syllables)
    print(f"Syllable Count: {len(syllables)}\n")

if __name__ == "__main__":
    main()