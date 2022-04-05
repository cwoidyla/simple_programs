import gensim.downloader as api

model = api.load("word2vec-google-news-300")

def analogy(worda, wordb, wordc):
    """
    worda is to wordb, as wordc is to _____

    worda: str
    wordb: str
    wordc: str
    return: list
    """
    result = model.most_similar(negative=[worda],
                                positive=[wordb, wordc])
    return result


if __name__ == '__main__':
    # king is to man, as queen is to ____
    print(analogy('king','man','queen'))
    """
    [('woman', 0.7609436511993408), ('girl', 0.6139993667602539), ('teenage_girl', 0.6040962338447571), 
    ('teenager', 0.5825759172439575), ('lady', 0.5752555131912231), ('boy', 0.5077577829360962), 
    ('policewoman', 0.5066847801208496), ('schoolgirl', 0.5052095651626587), ('blonde', 0.48696184158325195), 
    ('person', 0.48637545108795166)]
    """