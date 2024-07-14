text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

def wordcount(text):
    #字符替换
    text = text.replace(",", "").replace(".", "").replace("!", "")
    words = text.split()
    
    #统计每个单词数量
    word_counts = {}
    for word in words:
        #转换小写字母
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

   
    return word_counts


word_counts = wordcount(text)
#打印结果
for word, count in word_counts.items():
    print(f"{word}: {count}")
 