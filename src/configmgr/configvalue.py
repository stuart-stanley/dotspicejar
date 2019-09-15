

class ConfigManagerValueBase(object):
    def __init__(self, value_type):
        self.__children = {}
        self.__value_type = value_type
        self.__key = 'not-set'  # TODO: should we assert-lock bad access w/o setting this?
        # TODO record value_type's namespace and reject overloading any of the names

    @property
    def cm_is_empty(self):
        return False

    def cm_set_name(self, name):
        assert self.__key == 'not-set', \
            "coding-error: tried to set name more than once (prior={}, extra={}".format(
                self.__key, name)

        self.__key = name

    def __getattr__(self, key):
        if key not in self.__children:
            self.__children[key] = ConfigManagerValueEmpty()
            self.__children[key].cm_set_name(key)
        return self.__children[key]

    def __setattr__(self, key, value):
        print(self, "setattr", "key=", key, value)
        if key.startswith('_') or key.startswith("cm_"):
            print("override set ", key, value)
            super(ConfigManagerValueBase, self).__setattr__(key, value)
            return

        if key not in self.__children:
            if isinstance(value, int):
                new_var = ConfigManagerValueInt(value)
                print("new_var", new_var, type(new_var))
            else:
                raise NotImplementedError("config-value {} type {} not supported yet".format(value, type(value)))
            self.__children[key] = new_var
            new_var.cm_set_name = key
        self.__children[key]


class ConfigManagerValueInt(ConfigManagerValueBase, int):
    def __init__(self, *args, **kwargs):
        int.__init__(self)
        ConfigManagerValueBase.__init__(self, int)

    def __new__(cls, *args, **kwargs):
        # Note: see ConfigManagerValueBase doco on creation for _why_ this works.
        return super(cls, cls).__new__(cls, *args, **kwargs)


class ConfigManagerValueEmpty(ConfigManagerValueBase):
    def __init__(self):
        ConfigManagerValueBase.__init__(self, type(None))

    @property
    def cm_is_empty(self):
        # wish we could basically make this act like "None", but since that is a language-singleton,
        # there really isn't a way for 'if foo is None': to work on it. So, we have this hack.
        return True
