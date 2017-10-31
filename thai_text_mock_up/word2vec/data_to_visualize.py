import os
import gensim
import numpy as np

# Load & train word2vec model
model = gensim.models.Word2Vec.load('/Users/AUM/Documents/PROJECT/mockup_senior_project/thai_text_mock_up/word2vec/w2v.bin')
count = len(model.wv.vocab)

# create a list of vectors
embedding = np.empty((count, 100), dtype=np.float32)
for i, word in enumerate(model.wv.vocab):
    if i < count:
        embedding[i] = model[word]
    else: break

# write labels
with open('log/metadata.txt', 'w') as f:
    for idx, word in enumerate(model.wv.vocab):
        if idx < count:
            if (idx < (count - 1)):
                f.write(word + '\n')
            else:
                f.write(word)
        else: break
print("metadata.txt done!")

# # write labels
# write_string = ""
# with open('log/vector.tsv', 'w') as f:
#     for idx, array in enumerate(embedding):
#         if idx < count:
#             for i in array:
#                 f.write(str(i) + '\t')
#             if (idx < (count-1)):
#                 f.write('\n')
#             print(idx)
#         else: break
# print("vector.tsv done!")