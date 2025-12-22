import unittest

from main import Row, Table, TableRow, task_1, task_2, task_3, create_many_many_connection, create_one_many_connection


class Test(unittest.TestCase):
    def setUp(self):
        self.tables = [
            Table(1, 'Сотрудники'),
            Table(2, 'Отделы'),
            Table(3, 'Студенты'),
            Table(4, 'Empty table')
        ]

        self.rows = [
            Row(1, 100000, 'Иванов', 1),
            Row(2, 120000, 'Петров', 1),
            Row(3, 123, 'Отдел кадров', 2),
            Row(4, 1234, 'Бухгалтерия', 2),
            Row(5, 4000, 'Баранкин', 3),
            Row(6, 7000, 'Бубликов', 3)
        ]

        self.table_rows = [
            TableRow(1, 1),
            TableRow(2, 1),
            TableRow(3, 2),
            TableRow(4, 2),
            TableRow(5, 3),
            TableRow(6, 3),
            TableRow(1, 3),
            TableRow(2, 3)
        ]

        self.one_to_many = create_one_many_connection(self.tables, self.rows)
        self.many_to_many = create_many_many_connection(self.table_rows, self.tables, self.rows)

        return super().setUp()

    def test_task_1(self):
        """"""
        result = task_1(self.one_to_many)
        correct = ['Отделы', 'Отделы', 'Сотрудники', 'Сотрудники', 'Студенты', 'Студенты']

        for i in range(len(correct)):
            self.assertEqual(result[i][0], correct[i]) # Проверяем, что результат отсортирован по названию

    def test_task_2(self):
        """"""
        result = task_2(self.one_to_many)
        for i in range(len(result) - 1):
            self.assertFalse(result[i][1] < result[i + 1][1]) # Проверяем сортировку по убыванию

        correct = [220000, 11000, 1357]
        for i in range(len(result)):
            self.assertEqual(result[i][1], correct[i]) # Проверяем сортировку по убыванию

    def test_task_3(self):
        """"""
        result = task_3(self.many_to_many)

        # Проверяем фильтр
        correct = ['Сотрудники', 'Студенты']
        wrong = ['Отделы', 'Empty table']
        for i in range(len(correct)):
            self.assertIn(correct[i], result.keys())
        for i in range(len(wrong)):
            self.assertNotIn(wrong[i], result.keys())

        # Проверяем содержимое
        correct = {'Сотрудники': ['Иванов', 'Петров'], 'Студенты': ['Баранкин', 'Бубликов', 'Иванов', 'Петров']}
        for key, value in correct.items():
            self.assertEqual(len(value), len(result[key]))
            for item in value:
                self.assertIn(item, result[key])


if __name__ == "__main__":
    unittest.main()
