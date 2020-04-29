from tkinter import *
from tkinter.scrolledtext import ScrolledText


class Trie:
    def __init__(self, is_word=False, links=None):
        self.is_word = is_word
        self.links = {} if links is None else links

    def add(self, word):
        n = self
        for c in word:
            if c not in n.links:
                n.links[c] = Trie()
            n = n.links[c]
        n.is_word = True

    def starting_with(self, prefix):
        n = self
        for c in prefix:
            if c not in n.links:
                return []
            n = n.links[c]
        return self.all_below(n, prefix)

    def all_below(self, n, s):
        m = [s] if n.is_word else []
        if n.links == {}:
            return m
        for c in n.links:
            m.extend(self.all_below(n.links[c], s+c))
        return m


def update_list(e):
    textbox.delete(1.0, END)
    val = e.keysym
    if val == 'BackSpace':
        txt.pop()
    else:
        txt.append(val)
    for word in t.starting_with("".join(txt)):
        textbox.insert(END, word)


t = Trie()
for word in open("wordlist.txt"):
    t.add(word)


root = Tk()

txt = []

entry = Entry()
entry.bind('<Key>', update_list)
textbox = ScrolledText(height=20, width=20)

entry.grid(row=0, column=0)
textbox.grid(row=1, column=0)


mainloop()
