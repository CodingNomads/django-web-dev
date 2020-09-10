### About The Django Twitter Clone Project

This is an application that models the basic functionality of Twitter. It was built following (more or less) the tutorial [How to Build a Twitter Clone using Django](https://ahackersday.com/blog/djitter-how-to-build-a-twitter-clone-using-django-2-0/).

<div class='alert alert-warning' role='alert'>
    <strong>Note:</strong> While it's generally a great tutorial, there are some subtle errors that make the project not work if you build it out as described. So you can use it as a reference, but stick with the code provided in here, which has those errors fixed.
</div>

You might notice that you are looking at a _more complex project_ that was built with a slightly different approach than you have seen so far. This project doesn't always follow the best-practices that you are learning to use in this course. That is okay, and it is _inevitable_ that you would eventually come across something like this. Welcome to the real world. ¯\\\_(ツ)\_/¯

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> There are many ways to structure a Django project, and over time you will encounter more of them. The app you are now looking at works fine despite the different structure, and you will see that it is after all relatively similar to what you've seen and built so far.
</div>

### Your Task

You only need to focus on _one thing_: **Fixing the Tweet submission form on a user's profile page**.

Currently you are able to display everything fine, but once you try to _submit a tweet_ ... nothing happens! This needs to be fixed for your Twitter clone to be of any interest and use. So let's get into it:

- Create a user profile (you can use the signup page)
- Navigate to your profile page (you'll be redirected there automatically if you sign up through the app interface)
- How would you submit a new tweet? There's no visible input fields, and if you click the button, nothing happens
- Dive into the Django code and fix the issue! Submitting tweets should make them display on your profile page

After applying the necessary changes, your profile page should look like below.

<img alt="alt" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/django/imgs/djitter_input_fixed.png?raw=true">

You should be able to add _djeets_ by writing something into the input box and pressing <kbd>Post djeet</kbd>. The message should then appear on your wall on the left.

### Some Guidance

There are **two files** you need to edit and fix:

- `djeeterprofile/views.py`: Specifically in the `profile()` function, where the app is handling tweet form submissions
- `djitter/templates/profile.html`: Which hosts the HTML form element and displays the profile page as well as successfully submitted tweets

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> You will notice that the structure of this app is not ideal and might feel messy. Your task is to <em>focus</em> on your <em>specific job</em> of fixing the tweet form submission and tune out the rest of the app.
</div>

The two files mentioned above have **code comments** that indicate the area where you need to correct some of the code in order to make the form submission work as expected. Dig in, and use the previous tutorial sections as a reference. You got this, and once you're done, have fun djeeting your success! :)

<div class='alert alert-warning' role='alert'>
    <strong>Note:</strong> This project is meant to be messy. You will likely keep running into an Error even when you got the requested functionality to work. That is alright and I want you to disregard it for now. In this project you are meant to be exposed to the messiness that some projects bring along. You'll see a cleaned-up version of this same project in the next exercise. For this one: Accept the messiness and do your duty :)
</div>
