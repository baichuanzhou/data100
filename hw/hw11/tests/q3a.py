OK_FORMAT=True
test = {   'name': 'q3a',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> len(thetas_used) == 21\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(thetas_used) == len(losses_calculated) # theta history and loss history have 21 items in them\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> thetas_used[0].shape == (2,) # theta history contains theta values\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isscalar(losses_calculated[0]) # loss history is a list of scalar values, not vector\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isscalar(losses_calculated[0]) # loss is decreasing\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
