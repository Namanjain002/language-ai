from typing import List

from core.error_categories import ErrorCategory
from session.state import ChatSession

_FRIENDLY_NAMES = {
    ErrorCategory.TENSE: "tenses",
    ErrorCategory.VERB_FORM: "verb forms",
    ErrorCategory.SUBJECT_VERB_AGREEMENT: "subject-verb agreement",
    ErrorCategory.AUXILIARY_VERBS: "auxiliary verbs",
    ErrorCategory.MODAL_VERBS: "modal verbs",
    ErrorCategory.ARTICLES: "articles",
    ErrorCategory.PREPOSITIONS: "prepositions",
    ErrorCategory.PRONOUNS: "pronouns",
    ErrorCategory.POSSESSIVES: "possessives",
    ErrorCategory.SINGULAR_PLURAL: "singular/plural agreement",
    ErrorCategory.COUNTABILITY: "countable vs uncountable nouns",
    ErrorCategory.DETERMINERS: "determiners",
    ErrorCategory.WORD_ORDER: "word order",
    ErrorCategory.ADJECTIVES_ADVERBS: "adjectives and adverbs",
    ErrorCategory.COMPARATIVES_SUPERLATIVES: "comparatives/superlatives",
    ErrorCategory.CONJUNCTIONS: "conjunctions",
    ErrorCategory.NEGATION: "negation",
    ErrorCategory.QUESTION_FORMATION: "question formation",
    ErrorCategory.CONDITIONALS: "conditionals",
    ErrorCategory.GERUND_INFINITIVE: "gerunds/infinitives",
    ErrorCategory.RELATIVE_CLAUSES: "relative clauses",
    ErrorCategory.CLAUSE_STRUCTURE: "clause structure",
    ErrorCategory.PASSIVE_VOICE: "passive voice",
    ErrorCategory.OTHER_GRAMMAR: "general grammar",
}


def generate_summary(session: ChatSession) -> List[str]:
    ranked = sorted(session.error_tally.items(), key=lambda pair: pair[1], reverse=True)
    return [_FRIENDLY_NAMES[category] for category, count in ranked if count > 0]

def clear_summary(session: ChatSession):
    session.error_tally.clear()

message = []
def context(text: str):
    message.append(text)

def get_context() -> str:
    return " ".join(message)
