
class Comment:
    def __init__(self,data,type = 'normal'):
        self.type = type
        self.string = data

    ranks = {}
    categories = []
    def rank(self,rule):
        words = self.string.split(" ")

        for word in words:

            if word in rule.words:

                if self.ranks.get(rule.type) is None:
                    self.ranks[rule.type] = 1
                else:
                    self.ranks[rule.type] += 1

                if self.ranks[rule.type] >= rule.minWords and rule.type not in self.categories:
                    self.categories.append(rule.type)


class Rule:
    def __init__(self,words,type = 'spam',minWords = 1):
        print(self,words,type)
        self.type = type
        self.words = words
        self.minWords = minWords

class Filter:
    def __init__(self,rules,name = 'normal'):
        self.name = name
        self.rules = rules
    def filter(self,comments):
        toRemove = []
        for comment in comments:
            for rule in self.rules:
                comment.rank(rule)
            if len(comment.categories):
                toRemove.append(comment)

        for comment in toRemove:
            comments.remove(comment)
        return comments,toRemove

rule1 = Rule(['boobs','ass'],'porn')
rule2 = Rule(['win','iphone'],'spam')

rules = [rule1,rule2]

comments = [Comment('I love egypt'),Comment('I love ass'),Comment('win  2 Phone'), Comment('win iphone')]
filter = Filter(rules,'spam and porn')
print([comment.string for comment in filter.filter(comments)[0]])
