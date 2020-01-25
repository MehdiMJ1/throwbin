# Throwbin
Modern throwbin.io API wrapper.
# Installing
Just write into your console this:
```sh
python -m pip install throwbin
```
# Usage
There is some methods of using throwbin API.
## Post
### Post synchronous
```python
from throwbin import ThrowBin

tb = ThrowBin()

my_paste = tb.post(
    title="My title",
    text="My text",
    syntax="text"
)

print(f"Status {my_paste.status} | Link: {my_paste.link}")
```
