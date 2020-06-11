You've successfully applied **Path Converters** to make sure that only integers get passed to a view function, which again allowed you to do an integer-based database lookup. Cool! But here's a new challenge. Your friend, who really _is_ thankful that you're helping them and assures you it's the last time they're gonna ask you anything about this portfolio app so you can go back to mushroom pickling or whatever it is you like to spend your time on, found out about [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization).

Somewhere they learned that a plain number isn't the greatest URL fragment if you want to become #1 on search result pages. Because your friend is very business-savvy, they ask you to improve their SEO-ranking by replacing the final parts of these URLs with [slugs](https://en.wikipedia.org/wiki/Clean_URL#Slug). No, not the slimy animals, they say, just some words instead of numbers!

### Your Task

Change the necessary files to allow for URL slugs, such as `localhost:8000/projects/your-project-name`. Django provides a method called `slugify` to convert text into web-safe slugs, however, all of this is already taken care of for you in `projects/models.py`.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> If you've been re-using the database from a previous lab, keep in mind that this challenge introduces changes to the database, so you will need to either struggle with migrations, or start a fresh one here.
</div>

Create a couple of projects through the **Django Shell** and notice how the slug gets automatically created. If you make the projects through Django's Admin interface, you will have to manually create the slugs.

Next, replace the `pk`-based URL setup with one that utilizes the `project.slug` attribute. A project with the title `"Helping A Friend"` should be accessible via the URL `localhost:8000/projects/helping-a-friend`, another one with the title `"Pickling Mushrooms"` via `localhost:8000/projects/pickling-mushrooms`. All the links from the projects overview page should still work as expected.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> Keep in mind you can search the Django docs and the internet for support, as well as ask and answer questions on our forum, if you get stuck. You got this! : )
</div>
