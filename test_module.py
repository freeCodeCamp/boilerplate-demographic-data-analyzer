import unittest

import demographic_data_analyzer


class DemographicAnalyzerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data = False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        race_message = "Expected race count values to be {}".format(expected)
        self.assertCountEqual(actual, expected, msg=race_message)
        
    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        average_message = "Expected different value for average age of men."
        self.assertAlmostEqual(actual, expected, msg=average_message)

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4 
        percentage_message = "Expected different value for percentage with Bachelors degrees."
        self.assertAlmostEqual(actual, expected, msg=percentage_message)

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        higher_message = "Expected different value for percentage with higher education that earn >50K."
        self.assertAlmostEqual(actual, expected, msg=higher_message)
  
    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        test_lower_message = "Expected different value for percentage without higher education that earn >50K.")
        self.assertAlmostEqual(actual, expected, msg=test_lower_message)

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        test_min_message = "Expected different value for minimum work hours."
        self.assertAlmostEqual(actual, expected, msg=test_min_message)     

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10
        test_rich_message = "Expected different value for percentage of rich among those who work fewest hours."
        self.assertAlmostEqual(actual, expected, msg=test_rich_message)   

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        highest_earning_string = "Expected different value for highest earning country."
        self.assertEqual(actual, expected, highest_earning_string)   

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        test_highest_message = "Expected different value for highest earning country percentage."
        self.assertAlmostEqual(actual, expected, msg=test_highest_message)   

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        top_IN_string = "Expected different value for top occupations in India."
        self.assertEqual(actual, expected, top_IN_string)      


if __name__ == "__main__":
    unittest.main()
