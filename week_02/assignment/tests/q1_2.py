test = {
  'name': 'Question 1_2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> seafloor_age_data.describe().loc['max']['age_Ma'] == 280.0
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
