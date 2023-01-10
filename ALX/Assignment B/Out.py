import json
from io import StringIO
results = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(results)
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
"\"foo\bar"
print(json.dumps('\u1234'))
"\u1234"
print(json.dumps('\\'))
"\\"
print(json.dumps({"c": 0, "b": 0, "a": 0},sort_keys=True))
{"a": 0, "b": 0, "c": 0}

io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())
'["streaming API"]'
