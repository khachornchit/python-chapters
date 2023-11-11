def get_keywords(query):
    words = query.split()
    n = len(words)
    keywords = []

    for i in range(len(words)):
        keyword1 = ' '.join(words[i:n])
        keywords.append(keyword1)

        if (i > 0):
            keyword2 = ' '.join(words[0:n-i])
            keywords.append(keyword2)

        if (i > 0 and i < n-1):
            keyword3 = ' '.join(words[i:n-1])
            keywords.append(keyword3)

    return keywords


if __name__ == "__main__":
    query = "the engineering student mechanical"
    keywords = get_keywords(query)

    for keyword in keywords:
        print(keyword)
