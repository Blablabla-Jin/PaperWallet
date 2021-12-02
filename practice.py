import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.digest())
print(m.digest_size)

print(m.block_size)

encryption = hashlib.sha256(b"FekgazcfRFKLMFvxbMvbBXa1Lijd1UEHCrCHheCGwKW7").hexdigest()
print(encryption)
print(encryption == "031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406")
for i in range(len(encryption)):
    print(i)