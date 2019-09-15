from .configvalue import ConfigManagerValueEmpty


def cfm_init(*args, **kwargs):
    _ConfigManagerCenter(*args, **kwargs)


class _CFMEntry(object):
    def __init__(self):
        self.__our_cfm = None

    def pytest_reset(self):
        self.__our_cfm = None

    def __getattr__(self, key):
        print("CFME gettr", key)
        if self.__our_cfm is None:
            assert _ConfigManagerCenter._cfm_singleton is not None, \
                'trying to use configuration before init'

            self.__our_cfm = _ConfigManagerCenter._cfm_singleton

        return getattr(self.__our_cfm, key)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            print("setting in super", key, value)
            self.__dict__[key] = value
        else:
            if self.__our_cfm is None:
                assert _ConfigManagerCenter._cfm_singleton is not None, \
                    'trying to use configuration before init'

                self.__our_cfm = _ConfigManagerCenter._cfm_singleton
            print("CFME settr", key, value, self.__our_cfm)
            setattr(self.__our_cfm, key, value)


class _ConfigManagerCenter(object):
    _cfm_singleton = None

    def __init__(self, *args, **kwargs):
        assert _ConfigManagerCenter._cfm_singleton is None, \
            'can only create the configuration manager once'
        _ConfigManagerCenter._cfm_singleton = self
        print("making empty")
        self.__root_values = ConfigManagerValueEmpty()
        print("done making empty")

    def __getattr__(self, key):
        print("manager getting key", key)
        return getattr(self.__root_values, key)

    def __setattr__(self, key, value):
        print("manager set", key, value)
        if key.startswith('_'):
            print("setting in super center", key, value)
            self.__dict__[key] = value
        else:
            print("setting in root_value", key, value)
            setattr(self.__root_values, key, value)


cfm = _CFMEntry()


def pytest_reset():
    _ConfigManagerCenter._cfm_singleton = None
    cfm.pytest_reset()
