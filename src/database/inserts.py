from datetime import date

from src import db
from src.database.models import Book, Author


def insert():
    lewis_carroll = Author(name="Lewis Carroll")
    robert_stevenson = Author(name="Robert Louis Balfour Stevenson")
    maurice_herzog = Author(name="Maurice Herzog")
    diane_setterfield = Author(name="Diane Setterfield")
    aldous_huxley = Author(name="Aldous Huxley")

    book_alice_in_wonderland = Book(
        title="Alice In Wonderland",
        author=lewis_carroll,
        description="This edition contains Alice's Adventures in Wonderland and its sequel Through the Looking Glass. "
                    "It is illustrated throughout by Sir John Tenniel, whose drawings for the books add so much "
                    "to the enjoyment of them.",
        release_date=date(1993, 1, 1),
        publisher="Wordsworth Editions",
        language="eng",
        rating=5.0
    )
    book_treasure_island = Book(
        title="Treasure Island",
        author=robert_stevenson,
        description="Treasure Island is a tale of pirates and villains, maps, treasure and shipwreck. "
                    "When young Jim Hawkins finds a packet in Captain Flint's sea chest, he could not know that "
                    "the map inside it would lead him to unimaginable treasure.",
        release_date=date(1998, 1, 1),
        publisher="Wordsworth Editions",
        language="eng",
        rating=5.0
    )
    book_annapurna = Book(
        title="Annapurna",
        author=maurice_herzog,
        description="In 1950, no mountain higher than 8,000 meters had ever been climbed. "
                    "Maurice Herzog and other members of the French Alpine Club resolved to try. "
                    "This is the enthralling story of the first conquest of Annapurna and the harrowing descent. "
                    "With breathtaking courage and grit manifest on every page, Annapurna is one of the greatest "
                    "adventure stories ever told.",
        release_date=date(1951, 1, 1),
        publisher="Random House",
        language="eng",
        rating=3.5
    )
    book_the_thirteenth_tale = Book(
        title="The Thirteenth Tale",
        author=diane_setterfield,
        description="The story of the residents of Angelfield House and follows ageing novelist Vida Winter, who "
                    "enlists a young writer to finally tell the story of her life - including her mysterious childhood "
                    "spent in Angelfield House, which burned to the ground when she was a teenager.",
        release_date=date(2006, 9, 12),
        publisher="Atria Books",
        language="eng",
        rating=4.5
    )
    book_brave_new_world = Book(
        title="Brave New World",
        author=aldous_huxley,
        description="The novel examines a futuristic society, called the World State, that revolves around science and "
                    "efficiency. In this society, emotions and individuality are conditioned out of children at a young"
                    " age, and there are no lasting relationships because “every one belongs to every one else”",
        release_date=date(1932, 1, 1),
        publisher="Chatto & Windus",
        language="eng",
        rating=3.5
    )

    db.session.add_all([lewis_carroll, robert_stevenson, maurice_herzog, diane_setterfield, aldous_huxley])

    db.session.add(book_alice_in_wonderland)
    db.session.add(book_treasure_island)
    db.session.add(book_annapurna)
    db.session.add(book_the_thirteenth_tale)
    db.session.add(book_brave_new_world)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print("Start inserts...")
    insert()
    print("Finish inserts successful")
