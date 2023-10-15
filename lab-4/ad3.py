import pyperclip
import emoji


text_to_copy = "Hello, this is a test message copied to the clipboard."
pyperclip.copy(text_to_copy)


pasted_text = pyperclip.paste()
print("Pasted Text:", pasted_text)


message = "Python is fun! :snake: :thumbsup:"
message_with_emojis = emoji.emojize(message)
print("Message with Emojis:", message_with_emojis)
