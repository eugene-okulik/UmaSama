text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")
parts = text.split()
result = []
for text1 in parts:
    if text1.endswith(',') or text1.endswith('.'):
        result.append(text1[:-1] + 'ing' + text1[-1])
    else:
        result.append(text1 + 'ing')
print(' '.join(result))
