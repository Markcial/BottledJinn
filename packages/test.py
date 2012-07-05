from BottleDjinn.session import Session
from BottleDjinn.utils import  generate_session_id

session = Session(generate_session_id())
print session['dasd']
print session['foo']
session['asdaasd'] = 76222
session['test'] = 'asdasdasd'
session[ 'foo' ] = dict( { 'bar' : 'baz', 'spam' : 'eggz' } )