import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        person1 = BookLover('Samantha', 'samanthamilan@gmail.com', "Mystery", 0, pd.DataFrame(columns=['book_name', 'book_rating']))
        person1.add_book('Gone with the Wind', 5)
        
        self.assertTrue(person1.book_list['book_name'].values == 'Gone with the Wind')


    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        person2 = BookLover('Samantha', 'samanthamilan@gmail.com', "Mystery", 0, pd.DataFrame(columns=['book_name', 'book_rating']))
        person2 = person2.add_book('Gone with the Wind', 5)
        person2 = person2.add_book('Gone with the Wind', 5)
        expected = 1

        self.assertEqual(person2.num_books, expected)

                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        person2 = BookLover('Samantha', 'samanthamilan@gmail.com', "Mystery", 0, pd.DataFrame(columns=['book_name', 'book_rating']))
        person2 = person2.add_book('Gone with the Wind', 5)

        self.assertTrue(person2.has_read('Gone with the Wind'))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        person2 = BookLover('Samantha', 'samanthamilan@gmail.com', "Mystery", 0, pd.DataFrame(columns=['book_name', 'book_rating']))
        person2 = person2.add_book('Gone with the Wind', 5)
        person2 = person2.add_book('Call to the Wind', 4)

        self.assertFalse(person2.has_read('The Great Gatsby'))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        person3 = BookLover('Samantha', 'samanthamilan@gmail.com', "Mystery", 0, pd.DataFrame(columns=['book_name', 'book_rating']))
        person3 = person3.add_book('Gone with the Wind', 5)
        person3.add_book('Call to the Wind', 4)
        person3.add_book('A Sad Story', 3)
        person3.add_book('Sorry', 4)
        person3.add_book('Hey Ho', 2)
        expected = 5
        
        self.assertEqual(person3.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        person4 = BookLover('Person', 'samantha@gmail.com', "Thriller", 0, pd.DataFrame(columns=['book_name', 'book_rating']))
        person4.add_book('Gone with the Wind', 5)
        person4.add_book('Call to the Wind', 4)
        person4.add_book('A Sad Story', 3)
        person4.add_book('Sorry', 1)
        person4.add_book('Hey Ho', 2)
        expected = 2
        
        self.assertEqual(len(person4.fav_books()), expected)

                
if __name__ == '__main__':
    unittest.main(verbosity=3)