import re, reprlib

# 고전적인 디자인 패턴을 따른 반복자, 반복형 처리
# 파이썬스럽지 못한 코드임

RE_WORD = re.compile('\w+')

class Sentence:

  def __init__(self, text):
    self.text = text
    self.words = RE_WORD.findall(text)

  def __getitem__(self, index):
    return self.words[index]

  def __len__(self):
    return len(self.words)

  def __repr__(self):
    return 'Sentence(%s)' % reprlib.repr(self.text)


class SentenceIterator :

  def __init__(self, words):
    self.words = words
    self.index = 0

  def __next__(self):
    try :
      word = self.words[self.index]
    except IndexError :
      raise StopIteration()

    self.index += 1
    return word

  def __iter__(self):
    return self
