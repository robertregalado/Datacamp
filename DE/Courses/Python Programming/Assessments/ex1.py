
# ==============Iterator======================
x = (i for i in range(5))
print(next(x))
print(next(x))

# ============Right/Left Justify==============
s = 'fox'
print(s.rjust(4)) # ' fox'
print(s.ljust(4)) # 'fox '

# ==============Extend========================
my_languages = ['English', 'Dutch']
languages = ('French', 'Spanish')

print(my_languages.extend(languages))

