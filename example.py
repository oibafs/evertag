from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

dev_token = "S=s1:U=964f4:E=17f4cd248ae:C=177f52118f8:P=1cd:A=en-devtoken:V=2:H=bce832d858b0c97cfbfa33b4e2b5ef8d"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
    print n.name

noteStore = client.get_note_store()
note = Types.Note()
note.title = "I'm a test note!"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
note = noteStore.createNote(note)

noteStore = client.get_note_store()
notebook = Types.Notebook()
notebook.name = "My Notebook"
notebook = noteStore.createNotebook(notebook)
print notebook.guid