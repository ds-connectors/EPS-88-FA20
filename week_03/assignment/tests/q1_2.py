test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 16250.0 < earthquakes_mag5.describe().loc['count']['latitude'] < 16275.0
          True
          >>> 1290.0 < earthquakes_mag6.describe().loc['count']['latitude'] < 1303.0
          True
          >>> earthquakes_mag7.describe().loc['count']['latitude'] == 137.0
          True
          >>> earthquakes_mag8.describe().loc['count']['latitude'] == 9.0
          True
          >>> earthquakes_mag9.describe().loc['count']['latitude'] == 1.0
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
