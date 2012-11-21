

class Input(object):

    def __init__(self, id, name, label='', attrs={}):
        self.id = id
        self.name = name
        self.label = label
        self.attrs = attrs

    def render(self):
        return """<label for="%s">%s
                    <input type="text" name="%s" placeholder="%s" %s />
                  </label>""" % (
                      self.id,
                      self.label,
                      self.name,
                      self.label,
                      " ".join(
                        ['%s="%s"' % (k, v) for k, v in self.attrs.iteritems()]
                      )
                )

if __name__ == '__main__':

