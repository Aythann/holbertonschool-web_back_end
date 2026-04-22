#!/usr/bin/env python3
"""Module that provides a function to update school topics."""


def update_topics(mongo_collection, name, topics):
    """Update all documents matching name with the new topics list."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
