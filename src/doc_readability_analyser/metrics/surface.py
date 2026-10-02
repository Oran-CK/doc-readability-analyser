import textstat

def coleman_liau(text):
    return textstat.coleman_liau_index(text)

def fkgl(text):
    return textstat.flesch_kincaid_grade(text)
