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
from bookshelf import get_model
from flask import Blueprint, redirect, render_template, request, url_for


crud = Blueprint('crud', __name__)


@crud.route('/')
def home():
    """
    Returns home page
    for the application.
    """
    return render_template('home.html')



# [START list]
@crud.route("/list")
def list():
    """
    Returns the list 
    of movie reviews
    fetched from the datastore
    """
    token = request.args.get('page_token', None)
    reviews, next_page_token = get_model().list(cursor=token)
    return render_template(
        "list.html",
        reviews=reviews,
        next_page_token=next_page_token)
# [END list]



# [START add]
@crud.route('/add', methods=['GET', 'POST'])
def add():
    """
    Adds the movie review to the datastore
    """
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        review = get_model().create(data)
        return redirect(url_for('.list'))

    return render_template("form.html", action="Add", review={})
# [END add]
