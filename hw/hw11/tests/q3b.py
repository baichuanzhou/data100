OK_FORMAT=True
test = {   'name': 'q3b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> len(thetas_used_decay) == len(losses_calculated_decay) == 21 # theta history and loss history are 20 items in them\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> thetas_used_decay[0].shape == (2,) # theta history contains theta values\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isscalar(losses_calculated_decay[0]) # loss history should be a list of values, not vector\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> losses_calculated_decay[1] - losses_calculated_decay[-1] > 0 # loss is decreasing\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
