# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import current_app
from google.appengine.datastore.datastore_query import Cursor
from google.appengine.ext import ndb


builtin_list = list


def init_app(app):
    pass


# [START model]
class Review(ndb.Model):
    movie_name = ndb.StringProperty()
    year_released = ndb.StringProperty()
    genre = ndb.StringProperty()
    rating = ndb.StringProperty()
    review = ndb.StringProperty()
    reviewer = ndb.StringProperty()
# [END model]



# [START from_datastore]
def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        {id: id, prop: val, ...}
    """
    if not entity:
        return None
    if isinstance(entity, builtin_list):
        entity = entity.pop()
    movie_review = {}
    movie_review['id'] = entity.key.id()
    movie_review['movie_name'] = entity.movie_name
    movie_review['year_released'] = entity.year_released
    movie_review['genre'] = entity.genre
    movie_review['rating'] = entity.rating
    movie_review['review'] = entity.review
    movie_review['reviewer'] = entity.reviewer
    return movie_review
# [END from_datastore]


# [START list]
def list(limit=10, cursor=None):
    """
    Fetches the movie review data
    from the datastore
    """
    if cursor:
        cursor = Cursor(urlsafe=cursor)
    query = Review.query().order(Review.movie_name)
    entities, cursor, more = query.fetch_page(limit, start_cursor=cursor)
    entities = builtin_list(map(from_datastore, entities))
    return entities, cursor.urlsafe() if len(entities) == limit else None
# [END list]


# [START update]
def update(data, id=None):
    if id:
        key = ndb.Key('Review', int(id))
        review = key.get()
    else:
        review = Review()
    review.movie_name = data['movie_name']
    review.year_released = data['year_released']
    review.genre = data['genre']
    review.rating = data['rating']
    review.review = data['review']
    review.reviewer = data['reviewer']
    review.put()
    return from_datastore(review)
 

create = update
# [END update]
