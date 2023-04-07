#morris_pratt algoritması
def morris_pratt(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m

    # Longest Proper Prefix which is also a Suffix (LPS) tablosunu doldurma
    i = 1
    j = 0
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    # Morris-Pratt algoritmasının ana döngüsü
    i = 0
    j = 0
    indices = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            # Eşleşme bulundu, indeksi kaydet ve pattern'i sıfırla
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

# Dosyadan metin okuma
with open("alice_in_wonderland.txt", "r") as file:
    text = file.read()

pattern = "upon"
result = morris_pratt(text, pattern)
print("Eşleşme Indeksleri:")
print(result)