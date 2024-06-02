class Author:
    
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Invalid name")
        self._name = name
        self._articles = []
        self._magazines = set()

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article


    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Invalid name")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Invalid category")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Invalid name")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Invalid category")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        authors = {}
        for article in self._articles:
            if article.author not in authors:
                authors[article.author] = 0
            authors[article.author] += 1
        return [author for author, count in authors.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        most_articles_magazine = max(cls._all_magazines, key=lambda magazine: len(magazine._articles), default=None)
        if most_articles_magazine is None or len(most_articles_magazine._articles) == 0:
            return None
        return most_articles_magazine

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Invalid author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Invalid magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid title")
        self._author = author
        self._magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Invalid author")
        self._author._articles.remove(self)
        self._author = value
        self._author._articles.append(self)

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Invalid magazine")
        self._magazine._articles.remove(self)
        self._magazine = value
        self._magazine._articles.append(self)