OK_FORMAT=True
test = {   'name': 'q7b',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert res_q7b.shape == (15, 3)\n>>> list(res_q7b.columns) == ['name1', 'name2', 'total']\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> assert np.all(np.sort(res_q7b['total'])[::-1] == res_q7b['total'].to_numpy())\n>>> res_q7b['total'].sum() == 886\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
