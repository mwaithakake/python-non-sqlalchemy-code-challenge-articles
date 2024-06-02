class Article:
    all = []
    def __init__(self, author, magazine, title= "title"):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Titles must be of type str and between 5 and 50 characters, inclusive")
        self._author = author
        self._magazine = magazine
        self._title = title
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    def get_title(self):
        return self._title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be of type Author")
        self._author._articles.remove(self)
        self._author = new_author
        new_author._articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine._articles.remove(self)
        self._magazine = new_magazine
        new_magazine._articles.append(self)

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Names must be of type str and longer than 0 characters")
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
        return list({article.magazine.category for article in self._articles})

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Names must be of type str and between 2 and 16 characters, inclusive")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Categories must be of type str and longer than 0 characters")
        
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = set()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Names must be of type str and between 2 and 16 characters, inclusive")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Categories must be of type str and longer than 0 characters")
        self._category = new_category

    def add_article(self, author, title):
        new_article = Article(author, self, title)
        self._articles.append(new_article)
        return new_article

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def titles(self):
        return [article.title for article in self._articles]

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    

    def contributing_authors(self):
        author_article_count = {}
        for article in self._articles:
            author = article.author
            if author in author_article_count:
                author_article_count[author] += 1
            else:
                author_article_count[author] = 1

        authors_with_more_than_two_articles = [author for author, count in author_article_count.items() if count > 2]
        return authors_with_more_than_two_articles if authors_with_more_than_two_articles else None