import pandas as pd
import os 
from typing import *
from tika import parser
import gensim
import docx
import re

class InfoExtractor:
    @staticmethod
    def extractskills(filename)-> List[str]:
        try:
            text = getDocumentText(filename,parser)
        except:
            print("Error in File :" + filename)
            text=""
        
        data = pd.read_csv(
            os.path.join(os.path.dirname(_file_), "skills.csv")
        )
        skills = list(data.columns.values)
        skillset = []

        for token in gensim.utils.simple_preprocess(text):
            if token in skills:
                skillset.append(token)
        return [i.capitalize() for i in set([i.lower() for i in skillset])]
    

def getDocumentText(f: str, parser) -> Optional[str]:
    if f.endswith(".pdf"):
        new_text = getPDFText(f, parser)
    elif f.endswith(".docx"):
        new_text = getDocxText(f)
    else:
        return None, None
	
    try:
        new_text = re.sub("\n{3,}", "\n", new_text)
        new_text = str(bytes(new_text, "utf-8").replace(b"\xe2\x80\x93", b""), "utf-8")
    except:
        print('Error in Reading File: ' + f)
        new_text = ''
    return new_text

def getDocxText(filename: str) -> str:
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        txt = para.text
        fullText.append(txt)
    return "\n".join(fullText)

def getPDFText(filename: str, parser) -> str:
    raw = parser.from_file(filename)
    new_text = raw["content"]
    if "title" in raw["metadata"]:
        title = raw["metadata"]["title"]
        new_text = new_text.replace(title, "")
    return new_text