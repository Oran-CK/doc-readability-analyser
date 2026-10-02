import spacy
from functools import cached_property
from wordfreq import zipf_frequency

nlp = spacy.load("en_core_web_sm")

class TextComplexityAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    @cached_property
    def content_lemmas(self) -> list[str]:
        return [
            token.lemma_.lower()
            for token in self.doc
            if not token.is_punct and not token.is_space and not token.is_stop and not token.like_num
        ]

    @cached_property
    def zipf_scores(self) -> list[float]:
        return [zipf_frequency(lemma, "en") for lemma in self.content_lemmas]

    @property
    def mean_zipf(self) -> float:
        scores = self.zipf_scores
        return sum(scores) / len(scores) if scores else 0.0

    @property
    def rare_word_ratio(self) -> float:
        scores = self.zipf_scores
        if not scores:
            return 0.0
        return sum(1 for s in scores if s < 3.5) / len(scores)