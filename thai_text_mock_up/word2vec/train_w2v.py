import re, glob, os, gensim

curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath,os.pardir)) # this will return current directory in which python file resides.
parentDir = os.path.abspath(os.path.join(curDir,os.pardir)) # this will return parent directory in which python file resides.
BASE_DIR_TO_FILE = os.path.abspath(os.path.join(parentDir,os.pardir)) # this will return grand-parent directory in which python file resides.

best_path_list = [BASE_DIR_TO_FILE + "/BEST2010/Train"]
best_all_sentences = []
for path in best_path_list:
    for filename in glob.glob(os.path.join(path, '*.txt')):
        file = open(filename, 'r')
        file_string = file.read()
        file.close()

        file_string = file_string.replace("\n", "")
        file_sentence = file_string.split('|')
        temp_sentence = []
        for sentence in file_sentence:
            temp_sentence.append(sentence.split('/')[0])
        best_all_sentences.append(temp_sentence)
print("Paid BEST processing done!")
word_count = []
for idx, x in enumerate(best_all_sentences):
    for word in x:
        word_count.append(word)

best_free_path_list = [
    BASE_DIR_TO_FILE + "/BEST_data/news/",
    BASE_DIR_TO_FILE + "/BEST_data/encyclopedia/",
    BASE_DIR_TO_FILE + "/BEST_data/novel/",
    BASE_DIR_TO_FILE + "/BEST_data/article/"]
best_free_all_sentences = []
for path in best_free_path_list:
    for filename in glob.glob(os.path.join(path, '*.txt')):
        file = open(filename, 'r')
        file_string = file.read()
        file.close()

        file_string = re.sub(r'<NE>.*<\/NE>', '', file_string)
        file_string = re.sub(r'<AB>.*<\/AB>', '', file_string)
        file_string = file_string.replace("\n", "")
        best_free_all_sentences.append(file_string.split('|'))
print("Free BEST processing done!")
free_word_count = []
for idx, x in enumerate(best_free_all_sentences):
    for word in x:
        free_word_count.append(word)

print("Preprocessing sentences done!\n\tPaid BEST data : " + str(len(best_all_sentences)) + " files, " + str(len(word_count))
      + " words.\n\tFree BEST data : " + str(len(best_free_all_sentences)) + " files, " + str(len(free_word_count))
      + " words.")

all_sentences = best_all_sentences + best_free_all_sentences

# Train word2vec model for sentences
model = gensim.models.Word2Vec(all_sentences, min_count=1)
print("Training model done!")

# Save word2vec model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model.save(BASE_DIR+'/word2vec/w2v.bin')