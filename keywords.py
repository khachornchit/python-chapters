if __name__ == "__main__":
    query = "the engineering student mechanical"
    words = query.split()
    n = len(words)

    # Get keywords
    for i in range(len(words)):
        keyword1 = ' '.join(words[i:n])
        print(keyword1)

        if (i > 0):
            keyword2 = ' '.join(words[0:n-i])
            print(keyword2)

        if (i > 0 and i < n-1):
            keyword3 = ' '.join(words[i:n-1])
            print(keyword3)
