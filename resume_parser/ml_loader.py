import shutil

from info_extractor import InfoExtractor
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

testAlgo = LogisticRegression(solver='lbfgs', multi_class='auto')

trainResumePathDictionary = {}
trainResumeSkillsDictionary = {}
trainY = []
resumeBaseUrl = "training-data/"
processingSet = ['FE', 'BE', 'DevOps']
dataFrameDictionary = {}

try:
    for currentSet in processingSet:
        currentPath = resumeBaseUrl + currentSet
        trainResumePathDictionary[currentSet] = [os.path.join(currentPath, f) for f in os.listdir(currentPath) if os.path.isfile(os.path.join(currentPath, f))]
except:
    print('Error')
    pass


resumeVectorizer = CountVectorizer()

def prepareResumeNameAsIndex(resumesList):
    indexes = {}
    for i in range(len(resumesList)):
        indexes[i] = resumesList[i].split("/")[len(resumesList[i].split("/")) - 1]
    return indexes


def prepareOutputClassesForTrainingSet(currentSet):
    if currentSet == 'FE':
        trainY.append(0)
    elif currentSet == 'BE':
        trainY.append(1)
    elif currentSet == 'QA':
        trainY.append(2)
    elif currentSet == 'DevOps':
        trainY.append(3)


def extractTrainingText(resumes, currentSet):
    countFilesRead = 0
    trainResumeSkillsDictionary[currentSet] = []
    tempSplittedTextForDataFrame = []
    tempSplittedTextContainerForDataFrame = []
    currentResumeDataFrame = {}
    for currentResume in resumes:
        countFilesRead += 1
        if countFilesRead % 100 == 0:
            print("Resumes Read for " + currentSet + " = " + str(countFilesRead))
        tempSplittedTextForDataFrame = InfoExtractor.extractSkills(currentResume)
        tempSplittedTextContainerForDataFrame.append(tempSplittedTextForDataFrame)
        individualResumeSkills = " ".join(tempSplittedTextForDataFrame)
        trainResumeSkillsDictionary[currentSet].append(individualResumeSkills)
        prepareOutputClassesForTrainingSet(currentSet)
    currentResumeDataFrame = pd.DataFrame(tempSplittedTextContainerForDataFrame)
    tempSplittedTextContainerForDataFrame = []
    tempSplittedTextForDataFrame = []
    currentResumeDataFrame.rename(index=prepareResumeNameAsIndex(trainResumePathDictionary[currentSet]), inplace=True)
    return currentResumeDataFrame


def trainDataSet():
    for currentSet in processingSet:
        dataFrameDictionary[currentSet] = extractTrainingText(trainResumePathDictionary[currentSet], currentSet)
        print('----------Extraction completed for dataset: ' + currentSet + '------------')


def fetchValuesForTraining(currentDataset):
    tempSkillsToTrainSet = []
    for currentSet in processingSet:
        tempSkillsToTrainSet += currentDataset[currentSet]
    return tempSkillsToTrainSet


def normalizeLanguageForMachine():
    Resume_Vector = []
    normalizedData = []

    skillsToTrain = fetchValuesForTraining(trainResumeSkillsDictionary)
    resumeVectorizer.fit(skillsToTrain)

    for text in skillsToTrain:
        vector = resumeVectorizer.transform([text])
        Resume_Vector.append(vector.toarray())

    for x in Resume_Vector:
        normalizedData.append(x[0])

    return normalizedData


def classifyTestedResumes(testResumes, predictedResumes):
    resultDestinationBaseUrl = "result/resumes/"
    namesOnly = []
    predictedNames = []
    for i in range(len(testResumes)):
        namesOnly.append(testResumes[i].split("/")[len(testResumes[i].split("/")) - 1])
    for i in range(len(predictedResumes)):
        currentName = namesOnly[i].split("\\")[len(testResumes[i].split("\\")) - 1]
        if predictedResumes[i] == 0:
            classifyResumesInFolders(testResumes[i], resultDestinationBaseUrl + 'FE/' + currentName)
            predictedNames.append("Front End Resume")
        elif predictedResumes[i] == 1:
            classifyResumesInFolders(testResumes[i], resultDestinationBaseUrl + 'BE/' + currentName)
            predictedNames.append("Back End Resume")
        elif predictedResumes[i] == 2:
            classifyResumesInFolders(testResumes[i], resultDestinationBaseUrl + 'QA/' + currentName)
            predictedNames.append("QA Resume")
        elif predictedResumes[i] == 3:
            classifyResumesInFolders(testResumes[i], resultDestinationBaseUrl + 'DevOps/' + currentName)
            predictedNames.append("DevOps Resume")
    return namesOnly, predictedNames


def testAndClassifyResumes():
    resumePathTest = "uploads"
    testResumes = [os.path.join(resumePathTest, f) for f in os.listdir(resumePathTest) if
                   os.path.isfile(os.path.join(resumePathTest, f))]
    skillsToTrainTest = []
    testResume = ""
    for testResume in testResumes:
        testSkills = InfoExtractor.extractSkills(testResume)
        skillsToTrainTest.append(" ".join(testSkills))
    newArrayToPredict = resumeVectorizer.transform(skillsToTrainTest).toarray()
    predictedResumes = testAlgo.predict(newArrayToPredict)
    return classifyTestedResumes(testResumes, predictedResumes)


def trainMachineLearningAlgorithm(normalizedDataForProcessing, trainY):
    trainX = np.array(normalizedDataForProcessing)
    trainY = np.array(trainY)
    trainY = trainY.reshape(-1, 1)
    testAlgo.fit(trainX, trainY)
    print(trainX.shape)
    print(trainY.shape)


#     "src/data/test/resumes/export_dataframe.csv"
def getTrainingDataFromCSV(file):
    trainingSetFromCSV = pd.read_csv(file)
    trainYFromFile = np.array(trainingSetFromCSV['outputClass']).reshape(-1, 1)
    trainXFromFile = np.array(trainingSetFromCSV.drop(columns=['outputClass']).values.tolist())
    print(trainYFromFile.shape)
    print(trainXFromFile.shape)
    return trainXFromFile, trainYFromFile, trainingSetFromCSV


def normalizeDataAndWriteToFile(file):
    normalizedDataForProcessing = normalizeLanguageForMachine()
    TransformedResumesData = pd.DataFrame(normalizedDataForProcessing)
    TransformedResumesData = TransformedResumesData.join(pd.DataFrame({'outputClass': trainY}))
    print(TransformedResumesData.shape)
    TransformedResumesData.rename(index=prepareResumeNameAsIndex(fetchValuesForTraining(trainResumePathDictionary)),
                                  inplace=True)
    # TransformedResumesData.columns = resumeVectorizer.get_feature_names()
    print(TransformedResumesData.shape)
    export_csv = TransformedResumesData.to_csv(file, index=None, header=True)
    return normalizedDataForProcessing

def classifyResumesInFolders(source, destination):
    if not os.path.exists(destination.rsplit('/', 1)[0]):
        os.makedirs(destination.rsplit('/', 1)[0])
    dest = shutil.copyfile(source, destination)


trainDataSet()

normalizedDataForProcessing = normalizeDataAndWriteToFile('training-data/training_data_for_resumes.csv')

trainMachineLearningAlgorithm(normalizedDataForProcessing, trainY)




