# test_local.py
import sys
import os

# Add the 'src' directory to your path so Python finds your local code
sys.path.insert(0, os.path.abspath("src"))

from dzoseg.segmenter import DzongkhaTokenizer

try:
    ds = DzongkhaTokenizer()
    text = "འབྲུག་རྒྱལ་གཞུང་གཙུག་ལག་སློབ་སྡེའི་འོག་ལུ་ཡོད་པའི་ཚན་རིག་དང་འཕྲུལ་རིག་མཐོ་རིམ་སློབ་གྲྭའི་གློག་རིག་དང་འཕྲུལ་རིག་ལས་ཁུངས།"
    
    print("--- Local Test Results ---")
    print(f"Subwords: {ds.segment_subwords(text)}")
    print(f"Tseg:     {ds.segment_tseg(text)}")
    
    # Check if model loaded
    if ds.sp:
        print("\n✅ Success: SentencePiece model loaded correctly!")
    else:
        print("\n❌ Failed: Model still not loading. Check your path in segmenter.py")

except Exception as e:
    print(f"An error occurred: {e}")