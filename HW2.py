import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


def main():
    """ Variables """

    votes = []  # Ranking of buildings by the architects
    truth = []
    numVoters = None
    numBuilding = None

    # reading the files
    with open('voters.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            votes.append(line)
    numVoters = len(votes)
    numBuilding = len(votes[0])


    with open('truth.csv') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            truth.append(line)
    # print(truth)



    """ Ranking """

    # # Calculate Pai
    # myPAI = pai(votes, numBuilding, numVoters)
    #
    # # Borda Ranking
    # bordaRanking = UW_borda(votes, numBuilding)
    # print("Borda", bordaRanking)
    # bordaPTDRanking = PTD_borda(votes, numBuilding, numVoters, myPAI)
    # print("PTD Borda", bordaPTDRanking)
    # bordaDTDRanking = DTD_borda(votes, numBuilding, numVoters, bordaRanking)
    # print("DTD Borda", bordaDTDRanking)
    #
    # # Copeland Ranking
    # copelandRanking = UW_Copeland(votes, numBuilding)
    # print("Copland", copelandRanking)
    # copelandPTDRanking = PTD_Copeland(votes, numBuilding, numVoters, myPAI)
    # print("PTD Copland", copelandPTDRanking)
    # copelandDTDRanking = DTD_Copeland(votes, numBuilding, numVoters, copelandRanking)
    # print("DTD Copland", copelandDTDRanking)

    """ Ploting """

    # plt.style.use('seaborn')
    # paiDis = pai(votes, numBuilding, numVoters)
    # disTruth = disFromTruth(votes, numBuilding, numVoters, truth)
    # print(paiDis)
    # print(disTruth)
    # plt.scatter(disTruth.values(), paiDis.values())
    # plt.tight_layout()
    # plt.title("Scatter Plot")
    # plt.xlabel("Distance From The Truth")
    # plt.ylabel("Proxy Distance")
    # plt.savefig('scatterPlot')


    randomSmaples = 10

    disUWBorda = [0] * 17
    disPTDBorda = [0] * 17
    disDTDBorda = [0] * 17
    disUWCopland = [0] * 17
    disPTDCopland = [0] * 17
    disDTDCopland = [0] * 17

    # sampleZise = 1
    x = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]
    # print(len(x))
    # index = 0
    # while sampleZise <= 85:
    #     disUWBorda[index] = 0
    #     disPTDBorda[index] = 0
    #     disDTDBorda[index] = 0
    #     disUWCopland[index] = 0
    #     disPTDCopland[index] = 0
    #     disDTDCopland[index] = 0
    #     sampleZise += 5
    #     index += 1


    # print(truth)
    newTruth = []
    for ind in range(len(truth[1])):
        newTruth.append(int(truth[0][truth[1].index(str(ind))]))
    # print(newTruth)



    for num in range(randomSmaples):
        # Intervals of 5 between [5,85]
        print ("sample ",num+1)
        sampleZise = 5
        index = 0
        while sampleZise <= 85:
            print("sample size",sampleZise)
            newSet = []
            # print("sample size",sampleZise)
            for n in range(sampleZise):
                # print("n", n)
                number = random.randint(0, 84)
                newSet.append(votes[number])

            # print (newSet)
            # print(len(newSet))
            # print(numVoters)

            myNewPai = pai(newSet, numBuilding, len(newSet))
            # print(myNewPai)
            # print(len(myNewPai))
            # print(newSet)
            # print(len(newSet))

            UWBorda = UW_borda(newSet, numBuilding)
            distanse = sampleDisFromTruth(UWBorda, newTruth)
            disUWBorda[index] += distanse/randomSmaples

            PTDBorda = PTD_borda(newSet, numBuilding, len(newSet), myNewPai)
            distanse = sampleDisFromTruth(PTDBorda, newTruth)
            disPTDBorda[index] += distanse/randomSmaples

            DTDBorda = DTD_borda(newSet, numBuilding, len(newSet), UWBorda)
            distanse = sampleDisFromTruth(DTDBorda, newTruth)
            disDTDBorda[index] += distanse / randomSmaples

            UWCopland = UW_Copeland(newSet, numBuilding)
            distanse = sampleDisFromTruth(UWCopland, newTruth)
            disUWCopland[index] += distanse / randomSmaples

            PTDCopland = PTD_Copeland(newSet, numBuilding, len(newSet), myNewPai)
            distanse = sampleDisFromTruth(PTDCopland, newTruth)
            disPTDCopland[index] += distanse / randomSmaples

            DTDCopland = DTD_Copeland(newSet, numBuilding, len(newSet), UWCopland)
            distanse = sampleDisFromTruth(DTDCopland, newTruth)
            disDTDCopland[index] += distanse / randomSmaples

            sampleZise += 5
            index += 1


    print(disUWBorda)
    print(len(disUWBorda))
    print(disPTDBorda)
    print(disDTDBorda)
    print(disUWCopland)
    print(disPTDCopland)
    print(disDTDCopland)
    print(x)
    print(len(x))

    plt.figure(figsize=(15, 5))
    plt.plot(x, disUWBorda)
    plt.plot(x, disPTDBorda)
    plt.plot(x, disDTDBorda)
    plt.title("Borda Plot", fontsize=16)
    plt.xlabel("Sample Size", fontsize=13)
    plt.ylabel("True Error Distance", fontsize=13)
    plt.legend(['UW Borda', 'PTD Borda', 'DTD Borda'], loc=0)
    plt.savefig('BordaPlot')

    plt.figure(figsize=(15, 5))
    plt.plot(x, disUWCopland)
    plt.plot(x, disPTDCopland)
    plt.plot(x, disDTDCopland)
    plt.title("Copland Plot", fontsize=16)
    plt.xlabel("Sample Size", fontsize=13)
    plt.ylabel("True Error Distance", fontsize=13)
    plt.legend(['UW Copland', 'PTD Copland', 'DTD Copland'], loc=0)
    plt.savefig('CoplandPlot')



def sampleDisFromTruth(voting, truth):
    # print(voting)
    # print(truth)

    base = []
    countDis = 0

    for index, first in enumerate(voting):
        for second in voting[index + 1:]:
            base.append((first, second))

    for index, first in enumerate(truth):
        for second in truth[index + 1:]:
            if (first, second) not in base:
                countDis += 1
    # print(base)

    return countDis


def pai(votes, numBuilding, numVoters):
    # The normalize number
    fact = 1
    for i in range(1, numBuilding - 1):
        fact = fact * i
    n = int((fact * numBuilding * (numBuilding - 1)) / (fact * 2))

    base = {}  # Key per vote (1 to 'numVoters', values is array of preferences
    for baseIndex, vote in enumerate(votes):
        base[baseIndex + 1] = []
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                base[baseIndex + 1].append((first, second))

    d = {}
    for first in range(1, numVoters):
        for second in range(first + 1, numVoters + 1):
            d[first, second] = 0
            for preferences in base[first]:
                if preferences not in base[second]:
                    d[first, second] += 1
            d[first, second] = d[first, second] / n
    # print(d)
    # print(len(d))

    pai = {}
    for keys, value in d.items():
        if keys[0] in pai.keys():
            pai[keys[0]] += value / (numVoters - 1)
        else:
            pai[keys[0]] = value / (numVoters - 1)
        if keys[1] in pai.keys():
            pai[keys[1]] += value / (numVoters - 1)
        else:
            pai[keys[1]] = value / (numVoters - 1)
    # print (pai)
    return pai


def disFromTruth (votes,numBuilding, numVoters, truth):
    # The normalize number
    fact = 1
    for i in range(1, numBuilding - 1):
        fact = fact * i
    n = int((fact * numBuilding * (numBuilding - 1)) / (fact * 2))

    newTruth = []
    for ind in range(len(truth[1])):
        newTruth.append(truth[0][truth[1].index(str(ind))])
    # print(newTruth)

    base = {}  # Key per vote (1 to 'numVoters', values is array of preferences
    for baseIndex, vote in enumerate(votes):
        base[baseIndex + 1] = []
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                base[baseIndex + 1].append((first, second))
    # print(base)
    base[0] = []
    for index, first in enumerate(newTruth):
        for second in newTruth[index + 1:]:
            base[0].append((first, second))
    # print(base[0])

    w = {}
    for index in range(1, numVoters + 1):
        w[index] = 0
        for preferences in base[0]:
            if preferences not in base[index]:
                w[index] += 1
        w[index] = 0.5 - (w[index] / n)
    # print(w)

    return w


def UW_borda(votes, numBuilding):
    """
    :param votes: Ranking of buildings by the architects
    :param numBuilding: Number of buildings
    :return: Array of ranking of the buildings by 'borda' social choice,
            Each value represents the height of the building from 0 to 'numBuilding' - 1
    """

    bordaScore = [0] * numBuilding
    bordaRank = [0] * numBuilding

    for vote in votes:
        score = 0
        for rank in vote:
            bordaScore[int(rank)] += score
            score += 1

    ranking = numBuilding - 1
    pos = []

    # print(bordaScore)
    while ranking > -1:
        pos = []
        maxValue = max(bordaScore)
        for index, rank in enumerate(bordaScore):
            if rank == maxValue:
                # print(index)
                pos.append(index)
                bordaScore[index] = -1
        # print(pos)
        while len(pos) > 0:
            rand = np.random.choice(pos)
            # print(rand)
            # print(ranking)
            pos.remove(rand)
            # bordaRank[rand] = ranking
            bordaRank[ranking] = rand
            ranking -= 1
        # print(bordaScore)
        # print(bordaRank)
    return bordaRank


def PTD_borda(votes, numBuilding, numVoters, pai):
    """
    :param votes: Ranking of buildings by the architects
    :param numBuilding: Number of buildings
    :param numVoters: Number of Voters
    :return: Array of ranking of the buildings by 'borda PTD' social choice,
            Each value represents the height of the building from 0 to 'numBuilding' - 1
    """

    # # The normalize number
    # fact = 1
    # for i in range(1, numBuilding-1):
    #     fact = fact * i
    # n = int((fact*numBuilding*(numBuilding-1))/(fact*2))
    #
    # # print(n)
    # base = {}  # Key per vote (1 to 'numVoters', values is array of preferences
    # for baseIndex, vote in enumerate(votes):
    #     base[baseIndex + 1] = []
    #     for index, first in enumerate(vote[:-1]):
    #         for second in vote[index+1:]:
    #             base[baseIndex + 1].append((first, second))
    #
    # d = {}
    # for first in range(1, numVoters):
    #     for second in range(first+1, numVoters+1):
    #         d[first, second] = 0
    #         for preferences in base[first]:
    #             if preferences not in base[second]:
    #                 d[first, second] += 1
    #         d[first, second] = d[first, second]/n
    # # print(d)
    # # print(len(d))
    #
    # pai = {}
    # for keys, value in d.items():
    #     if keys[0] in pai.keys():
    #         pai[keys[0]] += value/(numVoters-1)
    #     else:
    #         pai[keys[0]] = value/(numVoters-1)
    #     if keys[1] in pai.keys():
    #         pai[keys[1]] += value/(numVoters-1)
    #     else:
    #         pai[keys[1]] = value/(numVoters-1)
    #
    # # print(pai)
    # # print(len(pai))
    # # print(pai)

    w = {}
    for key, value in pai.items():
        w[key] = 0.5 - value

    # print(w)
    # print(len(w))

    bordaScore = [0] * numBuilding
    bordaRank = [0] * numBuilding
    # print(len(bordaRank))

    for index, vote in enumerate(votes):
        score = 0
        for rank in vote:
            bordaScore[int(rank)] += ( score * w[index + 1])
            score += 1

    ranking = numBuilding - 1
    pos = []

    while ranking > -1:
        maxValue = max(bordaScore)
        for index, rank in enumerate(bordaScore):
            if rank == maxValue:
                pos.append(index)
                bordaScore[index] = -1
        while len(pos) > 0:
            rand = np.random.choice(pos)
            pos.remove(rand)
            # bordaRank[rand] = ranking
            # print("len",len(bordaRank))
            # print("renk",ranking)
            bordaRank[ranking] = rand
            ranking -= 1
    return bordaRank


def DTD_borda(votes, numBuilding, numVoters, bordaRanking):

    # The normalize number
    fact = 1
    for i in range(1, numBuilding - 1):
        fact = fact * i
    n = int((fact * numBuilding * (numBuilding - 1)) / (fact * 2))

    base = {}  # Key per vote (1 to 'numVoters', values is array of preferences
    for baseIndex, vote in enumerate(votes):
        base[baseIndex + 1] = []
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                base[baseIndex + 1].append((int(first), int(second)))

    base[0] = []
    for index, first in enumerate(bordaRanking):
        for second in bordaRanking[index + 1:]:
            base[0].append((first, second))
    # print(base[0])

    w = {}
    for first in range(1, numVoters + 1):
        w[first] = 0
        for preferences in base[first]:
            if preferences not in base[0]:
                w[first] += 1
        w[first] = 0.5 - (w[first] / n)

    # print(w)

    bordaScore = [0] * numBuilding
    bordaRank = [0] * numBuilding

    for index, vote in enumerate(votes):
        score = 0
        for rank in vote:
            bordaScore[int(rank)] += (score * w[index + 1])
            score += 1

    ranking = numBuilding - 1
    pos = []

    while ranking > -1:
        maxValue = max(bordaScore)
        for index, rank in enumerate(bordaScore):
            if rank == maxValue:
                pos.append(index)
                bordaScore[index] = -1
        while len(pos) > 0:
            rand = np.random.choice(pos)
            pos.remove(rand)
            # bordaRank[rand] = ranking
            bordaRank[ranking] = rand
            ranking -= 1
    return bordaRank


def UW_Copeland(votes, numBuilding):
    """
    :param votes: Ranking of buildings by the architects
    :param numBuilding: Number of buildings
    :return: Array of ranking of the buildings by 'copeland' social choice,
            Each value represents the height of the building from 0 to 'numBuilding' - 1
    """

    coplandScore = [0] * numBuilding
    coplandRank = [0] * numBuilding

    graph = {}

    for vote in votes:
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                if (int(first), int(second)) in graph.keys():
                    graph[int(first), int(second)] = graph[int(first), int(second)] + 1
                else:
                    graph[int(first), int(second)] = 1

    fixGraph = {}

    for first in range(numBuilding-1):
        for second in range(first+1, numBuilding):
            if (first, second) in graph.keys():
                posDir = graph[first, second]
            else:
                posDir = 0
            if (second, first) in graph.keys():
                negDir = graph[second, first]
            else:
                negDir = 0

            if posDir > negDir:
                fixGraph[first, second] = 1
            elif posDir == negDir:
                fixGraph[first, second] = 0.5
                fixGraph[second, first] = 0.5
            else:
                fixGraph[second, first] = 1

    for key, value in fixGraph.items():
        coplandScore[key[1]] = coplandScore[key[1]] + value

    ranking = numBuilding - 1
    pos = []

    while ranking > -1:
        maxValue = max(coplandScore)
        for index, rank in enumerate(coplandScore):
            if rank == maxValue:
                pos.append(index)
                coplandScore[index] = -1
        while len(pos) > 0:
            rand = np.random.choice(pos)
            pos.remove(rand)
            # coplandRank[rand] = ranking
            coplandRank[ranking] = rand
            ranking -= 1

    return coplandRank


def PTD_Copeland(votes, numBuilding, numVoters, pai):

    # # The normalize number
    # fact = 1
    # for i in range(1, numBuilding-1):
    #     fact = fact * i
    # n = int((fact*numBuilding*(numBuilding-1))/(fact*2))
    #
    # base = {}  # Key per vote (1 to 'numVoters', values is array of preferences
    # for baseIndex, vote in enumerate(votes):
    #     base[baseIndex + 1] = []
    #     for index, first in enumerate(vote[:-1]):
    #         for second in vote[index + 1:]:
    #             base[baseIndex + 1].append((first, second))
    #
    # d = {}
    # for first in range(1, numVoters):
    #     for second in range(first + 1, numVoters + 1):
    #         d[first, second] = 0
    #         for preferences in base[first]:
    #             if preferences not in base[second]:
    #                 d[first, second] += 1
    #         d[first, second] = d[first, second] / n
    #
    #
    # pai = {}
    # for keys, value in d.items():
    #     if keys[0] in pai.keys():
    #         pai[keys[0]] += value / (numVoters - 1)
    #     else:
    #         pai[keys[0]] = value / (numVoters - 1)
    #     if keys[1] in pai.keys():
    #         pai[keys[1]] += value / (numVoters - 1)
    #     else:
    #         pai[keys[1]] = value / (numVoters - 1)

    w = {}
    for key, value in pai.items():
        w[key] = 0.5 - value

    coplandScore = [0] * numBuilding
    coplandRank = [0] * numBuilding

    graph = {}

    for baseIndex, vote in enumerate(votes):
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                if (int(first), int(second)) in graph.keys():
                    graph[int(first), int(second)] = graph[int(first), int(second)] + (1*w[baseIndex+1])
                else:
                    graph[int(first), int(second)] = 1

    fixGraph = {}

    for first in range(numBuilding - 1):
        for second in range(first + 1, numBuilding):
            if (first, second) in graph.keys():
                posDir = graph[first, second]
            else:
                posDir = 0
            if (second, first) in graph.keys():
                negDir = graph[second, first]
            else:
                negDir = 0

            if posDir > negDir:
                fixGraph[first, second] = 1
            elif posDir == negDir:
                fixGraph[first, second] = 0.5
                fixGraph[second, first] = 0.5
            else:
                fixGraph[second, first] = 1

    # print(graph)
    # print (fixGraph)
    for key, value in fixGraph.items():
        coplandScore[key[1]] = coplandScore[key[1]] + value

    ranking = numBuilding - 1
    pos = []

    while ranking > -1:
        maxValue = max(coplandScore)
        for index, rank in enumerate(coplandScore):
            if rank == maxValue:
                pos.append(index)
                coplandScore[index] = -1
        while len(pos) > 0:
            rand = np.random.choice(pos)
            pos.remove(rand)
            # coplandRank[rand] = ranking
            coplandRank[ranking] = rand
            ranking -= 1

    return coplandRank


def DTD_Copeland(votes, numBuilding, numVoters, copelandRanking):

    # The normalize number
    fact = 1
    for i in range(1, numBuilding - 1):
        fact = fact * i
    n = int((fact * numBuilding * (numBuilding - 1)) / (fact * 2))

    base = {}  # Key per vote (1 to 'numVoters', values is array of preferences
    for baseIndex, vote in enumerate(votes):
        base[baseIndex + 1] = []
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                base[baseIndex + 1].append((int(first), int(second)))

    base[0] = []
    for index, first in enumerate(copelandRanking):
        for second in copelandRanking[index + 1:]:
            base[0].append((first, second))
    # print(base[0])

    w = {}
    for first in range(1, numVoters + 1):
        w[first] = 0
        for preferences in base[first]:
            if preferences not in base[0]:
                w[first] += 1
        w[first] = 0.5 - (w[first] / n)

    coplandScore = [0] * numBuilding
    coplandRank = [0] * numBuilding

    graph = {}

    for baseIndex, vote in enumerate(votes):
        for index, first in enumerate(vote[:-1]):
            for second in vote[index + 1:]:
                if (int(first), int(second)) in graph.keys():
                    graph[int(first), int(second)] = graph[int(first), int(second)] + (1*w[baseIndex+1])
                else:
                    graph[int(first), int(second)] = 1

    fixGraph = {}

    for first in range(numBuilding - 1):
        for second in range(first + 1, numBuilding):
            if (first, second) in graph.keys():
                posDir = graph[first, second]
            else:
                posDir = 0
            if (second, first) in graph.keys():
                negDir = graph[second, first]
            else:
                negDir = 0

            if posDir > negDir:
                fixGraph[first, second] = 1
            elif posDir == negDir:
                fixGraph[first, second] = 0.5
                fixGraph[second, first] = 0.5
            else:
                fixGraph[second, first] = 1

    # print(graph)
    # print (fixGraph)
    for key, value in fixGraph.items():
        coplandScore[key[1]] = coplandScore[key[1]] + value

    ranking = numBuilding - 1
    pos = []

    while ranking > -1:
        maxValue = max(coplandScore)
        for index, rank in enumerate(coplandScore):
            if rank == maxValue:
                pos.append(index)
                coplandScore[index] = -1
        while len(pos) > 0:
            rand = np.random.choice(pos)
            pos.remove(rand)
            # coplandRank[rand] = ranking
            coplandRank[ranking] = rand
            ranking -= 1

    return coplandRank


if __name__ == "__main__":
    main()
