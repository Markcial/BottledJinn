# -*- coding: utf-8 *-*


class Filter(object):

    def __init__(self, value):
        self.value = value

    def is_valid(self):
        return True

    def sanitize(self):
        return self.value


class StringFilter(Filter):

    def __init__(self, value):
        super(StringFilter, self).__init__(value)

    def is_valid(self):
        return type(self.value) is str

    def sanitize(self):
        import re
        return re.escape(self.value)


class EmailFilter(Filter):

    def __init__(self, value):
        super(EmailFilter, self).__init__(value)

    def is_valid(self):
        pass

    def sanitize(self):
        return self.value.lower()
