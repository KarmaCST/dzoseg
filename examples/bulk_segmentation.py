from dzoseg import DzongkhaSegmenter

def main():
    ds = DzongkhaSegmenter()

    # We use your specific text as the primary example
    sentences = [
        "འབྲུག་རྒྱལ་གཞུང་གཙུག་ལག་སློབ་སྡེའི་འོག་ལུ་ཡོད་པའི་ཚན་རིག་དང་འཕྲུལ་རིག་མཐོ་རིམ་སློབ་གྲྭའི་གློག་རིག་དང་འཕྲུལ་རིག་ལས་ཁུངས།",
        "བཀྲ་ཤིས་བདེ་ལེགས་ཕུན་སུམ་ཚོགས།",
        "ང་བཅས་རྫོང་ཁ་ལུ་དགའ།"
    ]

    print(f"Processing {len(sentences)} sample phrases...\n")

    for i, text in enumerate(sentences, 1):
        # segment_ids is critical for Neural Network training
        ids = ds.segment_ids(text)
        pieces = ds.segment_subwords(text)

        print(f"Phrase {i}: {text}")
        print(f"Subword Pieces: {pieces}")
        print(f"Vocabulary IDs: {ids}")
        print("-" * 50)

if __name__ == "__main__":
    main()