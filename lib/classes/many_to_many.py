class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string with 5 to 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title

        # Add this article to the author and magazine's list of articles
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise ValueError("Name must be a string with 2 to 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not 2 <= len(new_name) <= 16:
            raise ValueError("Name must be a string with 2 to 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        magazines = [mag for mag in globals().values() if isinstance(mag, cls)]
        if not magazines:
            return None
        return max(magazines, key=lambda mag: len(mag.articles()), default=None)


# Example usage

# Create authors
author1 = Author("John Doe")
author2 = Author("Jane Smith")

# Create magazines
magazine1 = Magazine("Tech Monthly", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

# Create articles
article1 = author1.add_article(magazine1, "The Rise of AI")
article2 = author1.add_article(magazine2, "Healthy Living Tips")
article3 = author2.add_article(magazine1, "Quantum Computing Explained")

# Access properties and methods
print(author1.name)  # John Doe
print(author1.articles())  # [article1, article2]
print(author1.magazines())  # [magazine1, magazine2]
print(author1.topic_areas())  # ['Technology', 'Health']

print(magazine1.name)  # Tech Monthly
print(magazine1.category)  # Technology
print(magazine1.articles())  # [article1, article3]
print(magazine1.contributors())  # [author1, author2]
print(magazine1.article_titles())  # ['The Rise of AI', 'Quantum Computing Explained']
print(magazine1.contributing_authors())  # None

print(article1.author.name)  # John Doe
print(article1.magazine.name)  # Tech Monthly
print(article1.title)  # The Rise of AI

# Change magazine name
magazine1.name = "Tech Innovations"
print(magazine1.name)  # Tech Innovations

# Change magazine category
magazine2.category = "Wellness"
print(magazine2.category)  # Wellness
