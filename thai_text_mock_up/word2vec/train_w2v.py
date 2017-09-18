import re, glob, os, gensim

# class MySentences(object):
#     def __init__(self, dirname):
#         self.dirname = dirname
#
#     def __iter__(self):
#         for filename in glob.glob(os.path.join(self.dirname, '*.txt')):
#             file = open(filename, 'r')
#             line = file.read()
#             file.close()
#             line = re.sub(r'<NE>.*<\/NE>', '', line)
#             line = re.sub(r'<AB>.*<\/AB>', '', line)
#             pattern = re.compile(r"[\u0E00-\u0E7F0-9.%]+")
#             yield pattern.findall(line)

path_list = [
    "/Users/AUM/Documents/PROJECT/mockup_senior_project/BEST_data/news/",
    "/Users/AUM/Documents/PROJECT/mockup_senior_project/BEST_data/encyclopedia/",
    "/Users/AUM/Documents/PROJECT/mockup_senior_project/BEST_data/novel/",
    "/Users/AUM/Documents/PROJECT/mockup_senior_project/BEST_data/article/"
]
all_sentences = []
for path in path_list:
    for filename in glob.glob(os.path.join(path, '*.txt')):
        file = open(filename, 'r')
        file_string = file.read()
        file.close()

        file_string = re.sub(r'<NE>.*<\/NE>', '', file_string)
        file_string = re.sub(r'<AB>.*<\/AB>', '', file_string)
        pattern = re.compile(r"[\u0E00-\u0E7F0-9.%]+")
        all_sentences.append(pattern.findall(file_string))
print("Preprocessing sentences done!")

# Train & save word2vec model for sentences
model = gensim.models.Word2Vec(all_sentences)
print("Training model done!")
model.save('/Users/AUM/Documents/PROJECT/mockup_senior_project/thai_text_mock_up/word2vec/w2v')
