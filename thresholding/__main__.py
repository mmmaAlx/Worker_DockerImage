import json
import sys
import cv2

def count_words(wordlist_filepath,threshold_n):
    image=cv2.imread(wordlist_filepath,-1)
    _,imageThreshold=cv2.threshold(image,threshold_n,255,cv2.THRESH_BINARY)
    return imageThreshold

if len(sys.argv) == 1:
    # When called with no args, print the task specs.
    with open('thresholding/spec.json', 'r') as spec:
        print(json.dumps(json.loads(spec.read()), indent=4))

else:
    task_name = sys.argv[1]
    if task_name == 'thresholding':
        # Expects an input file path, and an output file path.
        wordlist_filepath, wordcount_filepath = sys.argv[2:4]
        threshold_n = 128
        result = count_words(wordlist_filepath,threshold_n)
        print(wordlist_filepath)
        
        print(wordcount_filepath)
        cv2.imwrite(wordcount_filepath,result)
    else:
        sys.stderr.write('Task "%s" not found.\n' % (task_name,))
