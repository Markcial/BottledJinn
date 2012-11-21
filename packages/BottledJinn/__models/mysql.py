# -*- coding: utf-8 *-*


class Atom(object):

    def __init__(self, length, allow_null=False, default=None, comment=''):
        self.length = length
        self.allow_null = allow_null
        self.default = default
        self.comment = comment

    def set_length(self, length):
        assert type(length) is float
        self.length = length

    def set_allow_null(self, allow_null):
        assert type(allow_null) is bool
        self.allow_null = allow_null

    def set_default(self, default):
        self.default = default

    def set_comment(self, comment):
        self.comment = comment


class IntegerAtom(Atom):

    def __init__(self, length, unsigned=False, zerofill=False,
                allow_null=False, default=None, comment=''):
        super(IntegerAtom, self).__init__(length, allow_null,
            default, comment)
        self.datatype_group = 'integer'
        self.unsigned = unsigned
        self.zerofill = zerofill

    def set_unsigned(self, unsigned):
        assert type(unsigned) is bool
        self.unsigned = unsigned

    def set_zerofill(self, zerofill):
        assert type(zerofill) is bool
        self.zerofill = zerofill


class Tinyint(IntegerAtom):

    def __init__(self, length, unsigned=False, zerofill=False, allow_null=False,
                default=None, comment=''):
        super(Tinyint, self).__init__(self, length, unsigned=False,
            zerofill=False, allow_null=False, default=None, comment='')
        self.datatype = 'tinyint'


class Smallint(IntegerAtom):

    def __init__(self, length, unsigned=False, zerofill=False, allow_null=False,
                default=None, comment=''):
        super(Tinyint, self).__init__(self, length, unsigned=False,
            zerofill=False, allow_null=False, default=None, comment='')
        self.datatype = 'smallint'


class Mediumint(IntegerAtom):

    def __init__(self, length, unsigned=False, zerofill=False, allow_null=False,
                default=None, comment=''):
        super(Tinyint, self).__init__(self, length, unsigned=False,
            zerofill=False, allow_null=False, default=None, comment='')
        self.datatype = 'mediumint'
