OK_FORMAT=True
test = {   'name': 'q8c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> len(thetas_used_stoch) == len(losses_calculated_stoch) == 21 # theta history and loss history are 20 items in them\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> thetas_used_stoch[0].shape == (2,) # theta history contains theta values\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isscalar(losses_calculated_stoch[0]) # loss history should be a list of values, not vector\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> losses_calculated_stoch[1] - losses_calculated_stoch[-1] > 0 # loss is decreasing\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
