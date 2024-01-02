# test_hashtable.py

from hashtable import HashTable


'''def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100'''


'''def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]'''


def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table['hola'] = 'hello'
    hash_table[98.6] = 37
    hash_table[False] = True

    assert 'hello' in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
