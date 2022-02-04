from django.shortcuts import redirect, render


def login_requierd(func):

    def wrap(*args, **kwargs ):
        if 'logged_in' in args[0].session:
            return func(*args, **kwargs)
        else:
            return redirect("/up")
    return wrap