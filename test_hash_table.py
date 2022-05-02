from unittest import main, TestCase

from custom_hashtable.hash_table import HashTable


class TestHashTable(TestCase):
    def test_init(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        self.assertEqual([None, None, None, None], table._HashTable__values)
        self.assertEqual(4, table.max_capacity)

    def test_get_item_dunder(self):
        table = HashTable()
        table['name'] = 'Test'
        table['age'] = 0
        result = table['name']
        self.assertEqual('Test', result)

    def test_get_item_dunder_non_existing_key_raises(self):
        table = HashTable()
        table['name'] = 'Test'
        table['age'] = 0
        with self.assertRaises(KeyError) as ex:
            result = table['smth']
        self.assertEqual('smth', str(ex.exception.args[0]))

    def test_set_item_dunder_replace_value_of_existing_key(self):
        table = HashTable()
        table['name'] = 'Test'
        self.assertEqual('Test', table['name'])
        table['name'] = 'New Test'
        self.assertEqual('New Test', table['name'])

    def test_table_is_full_set_item_dunder_resizes(self):
        table = HashTable()
        table['name'] = 'Test'
        table['age'] = 0
        table['new name'] = 'New Test'
        table['some'] = 'Another Test'
        self.assertEqual(4, table.size())
        self.assertEqual(4, table.max_capacity)
        table['weight'] = 400
        self.assertEqual(5, table.size())
        self.assertEqual(8, table.max_capacity)

# Collision:
    def test_set_item_collision_linear_approach(self):
        table = HashTable()
        table['name'] = 'Test'
        occ_index = table._HashTable__keys.index('name')
        self.assertEqual(1, occ_index)
        expected_index = table._HashTable__calc_index('age')
        self.assertEqual(1, expected_index)
        table['age'] = 0
        self.assertEqual(2, table._HashTable__keys.index('age'))

# Overflow:
    def test_set_item_dunder_linear_approach_starts_at_beginning_after_reaches_end(self):
        table = HashTable()
        table['name'] = 'Test'
        table['age'] = 0
        table['new name'] = 'New Test'
        self.assertEqual([None, 'name', 'age', 'new name'], table._HashTable__keys)
        self.assertEqual([None, 'Test', 0, 'New Test'], table._HashTable__values)
        table['some'] = 'Another Test'
        self.assertEqual(['some', 'name', 'age', 'new name'], table._HashTable__keys)
        self.assertEqual(['Another Test', 'Test', 0, 'New Test'], table._HashTable__values)

    def test_add_adds_pair(self):
        table = HashTable()
        self.assertEqual([None]*4, table._HashTable__keys)
        table.add('age',12)
        self.assertEqual([None, 'age', None, None],table._HashTable__keys)

    def test_dunder_str(self):
        table = HashTable()
        table['name'] = 'Test'
        table['age'] = 0
        result = table.__str__()
        expected_result = '{ name: Test, age: 0 }'
        self.assertEqual(expected_result, result)

    def test_get_non_existing_key_returns_none(self):
        table = HashTable()
        self.assertEqual([None] * 4, table._HashTable__keys)
        result = table.get('some key')
        self.assertEqual(None, result)

    def test_get_with_default_value(self):
        table = HashTable()
        self.assertEqual([None] * 4, table._HashTable__keys)
        result = table.get('some key', 'default value')
        self.assertEqual('default value', result)

    def test_get_existing_key_returns_value(self):
        table = HashTable()
        table['name'] = 'Test'
        result = table.get('name')
        self.assertEqual('Test', result)


if __name__ == '__main__':
    main()

