from Repository import FakeRepository


class DiaryRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.diaries= []

    def add(self, diary):
        self.diaries.append(diary)

    def remove(self, diary):
        if self.diaries:
            for c in self.diaries:
                if c.name == diary.name:
                    self.diaries.remove(c)

    def get_all(self):
        return self.diaries

    def get_by_name(self, name):
        if self.diaries:
            for c in self.diaries:
                if c.name == name:
                    return c
        return "Категория не найдена"