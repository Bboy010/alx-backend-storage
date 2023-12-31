#!/usr/bin/env python3
""" function that returns all students sorted by average score
    Prototype: def top_students(mongo_collection)
    The top must be ordered
    The average score must be part of each item 
    returns with key = averageScore
"""


def top_students(mongo_collection):
   """ Prints all students in a collection sorted by average score.
    """
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
