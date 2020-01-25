from throwbin import ThrowBin

tb = ThrowBin()

my_paste = tb.post(
    title="My title",
    text="My text",
    syntax="text"
)

print(f"Status {my_paste.status} | Link: {my_paste.link}")