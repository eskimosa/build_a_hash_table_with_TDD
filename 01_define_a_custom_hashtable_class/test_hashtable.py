from hashtable import HashTable


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None


def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100


# UPDATE: new hash table should start with empty slots for the stored values
def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]
