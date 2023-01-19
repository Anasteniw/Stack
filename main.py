#1. Необходимо реализовать класс Stack со следующими методами:
# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.

# 2.Проверка сбалансированности скобок

Correct_algorithm = {
    '(': ')',
    '[': ']',
    '{': '}'
}

Balanced_brackets = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
Unbalanced_brackets = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, elem):
        self.append(elem)
        return

    def pop(self):
        if not self.isEmpty():
            elem = self[-1]
            self.__delitem__(-1)
        return elem


    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check_balanced(brack_str):
    stack = Stack()
    for el in brack_str:
        if el in Correct_algorithm:
            stack.push(el)
        elif el == Correct_algorithm.get(stack.peek()):
            stack.pop()
        else:
            return "Несбалансированно"
    return "Сбалансированно"


if __name__ == '__main__':
    for brack_str in Balanced_brackets + Unbalanced_brackets:
        print(f'{brack_str}{check_balanced(brack_str)}')